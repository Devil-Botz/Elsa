from googletrans import Translator
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Assuming 'list' contains language mappings

@Client.on_message(filters.command(["tr"]))
async def translate(client, message):
    if message.reply_to_message:
        try:
            lang_code = message.text.split("/tr")[1].strip().lower()
            tr_text = message.reply_to_message.text
            translator = Translator()
            translation = translator.translate(tr_text, dest=lang_code)

            from_lang = translation.src
            to_lang = translation.dest
            translated_text = translation.text

            print(f"Translated from {from_lang} to {to_lang}: {translated_text}")

            reply_text = f"Translated from {from_lang} to {to_lang}:\n\n{translated_text}"
            await message.reply_text(reply_text)

        except Exception as e:
            print("Error:", e)
            await message.reply_text("An error occurred during translation.")
    else:
        await message.reply_text("You can use this command by replying to a message.")
