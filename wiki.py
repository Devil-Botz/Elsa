import os
import logging

from collections import defaultdict

import telegram
import wikipedia

from telegram.ext.filters import Filters
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler
)
from telegram.error import TelegramError


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)


CHAT_QUERY = {}
SEARCH_HISTORY = defaultdict(list)


class BotError(TelegramError):
    pass


def make_wiki_query(wiki_results):
    try:
        page = wikipedia.page(wiki_results[0])
        return page, wiki_results
    except wikipedia.DisambiguationError as e:
        return make_wiki_query(e.options)


def get_search_results(search):
    wiki_results = wikipedia.search(search, results=4)
    if not wiki_results:
        raise BotError(message='Empty search results')

    page, wiki_results = make_wiki_query(wiki_results)

    return {
        'header': wiki_results[0],
        'summary': page.summary,
        'link': 'http://wikipedia.org/wiki/{}'.format(page.title),
        'extra': wiki_results[1:4] if len(wiki_results) > 1 else []
    }


def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Wikipedia bot! Type /search %query%"
    )


def initial_search(bot, update):
    chat_id = update.message.chat_id
    query = update.message.text
    reply_to_user(bot, chat_id, query, hide_back=True)


def query_update_handler(bot, update):
    chat_id = update.callback_query.message.chat.id
    query = update.callback_query.data
    message_id = update.callback_query.message.message_id
    if query == '_back':
        if SEARCH_HISTORY[chat_id]:
            query = SEARCH_HISTORY[chat_id].pop()
        else:
            query = CHAT_QUERY[chat_id]

        reply_to_user(
            bot, chat_id, query, message_id,
            skip_history=True, hide_back=len(SEARCH_HISTORY[chat_id]) == 0
        )
    else:
        reply_to_user(bot, chat_id, query, message_id)


def reply_to_user(
        bot, chat_id, query,
        message_id=None, skip_history=False, hide_back=False
):
    bot.send_chat_action(
        chat_id=chat_id,
        action=telegram.ChatAction.TYPING
    )
    search_results = get_search_results(query)
    summary = '{}\n{}'.format(
        search_results['summary'],
        search_results['link']
    )
    reply_markup = [
            [telegram.InlineKeyboardButton(item, callback_data=item)]
            for item in search_results['extra']
    ]
    if not hide_back:
        reply_markup += [[
            telegram.InlineKeyboardButton(
                'back', callback_data='_back'
            )
        ]]

    reply_markup = telegram.InlineKeyboardMarkup(reply_markup)

    if message_id:
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=summary,
            reply_markup=reply_markup
        )
    else:
        bot.send_message(
            chat_id=chat_id,
            text=summary,
            reply_markup=reply_markup
        )

    if not skip_history:
        if chat_id in CHAT_QUERY:
            SEARCH_HISTORY[chat_id].append(CHAT_QUERY[chat_id])

        CHAT_QUERY[chat_id] = search_results['header']

        if len(SEARCH_HISTORY[chat_id]) > 10:
            SEARCH_HISTORY[chat_id] = SEARCH_HISTORY[chat_id][-10:]


def error_handler(bot, update, error):
    try:
        raise error
    except BotError as e:
        chat_id = update.callback_query.message.chat.id
        bot.send_message(
            chat_id=chat_id,
            text=e.message,
        )


def main():
    bot_token = os.environ.get('BOT_TOKEN')
    if not bot_token:
        raise RuntimeError('No auth token for bot')

    updater = Updater(token=bot_token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, initial_search))
    dispatcher.add_handler(CallbackQueryHandler(query_update_handler))
    dispatcher.add_error_handler(error_handler)
    try:
        updater.start_polling()
    except KeyboardInterrupt:
        updater.stop()


if __name__ == '__main__':
    main()
