from utils import temp
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters, enums
from info import *
import openai
import asyncio
openai.api_key = OPENAI_API


@Client.on_message(filters.private & filters.command('openai'))
async def openai_answer(client, message):
    if AI == True:
        user_id = message.from_user.id
        if user_id:
            try:
                users_message = message.text.split(" ", 1)[1]
            except:
                return await message.reply_text("use in this format-\n\n<code>/openai how to create a telegram bot</code> <br> Sorry openai quota completed")
            try:
                user_id = message.from_user.id
                response = openai.Completion.create(
                    model = "text-davinci-003",
                    prompt = users_message,
                    temperature = 0.5,
                    max_tokens = 1000,
                    top_p=1,
                    frequency_penalty=0.1,
                    presence_penalty = 0.0,
                )
                btn=[
                        [InlineKeyboardButton(text=f"👀 ᴛᴀᴋᴇ ᴀᴄᴛɪᴏɴ 👀", url=f'https://t.me/{temp.U_NAME}')],
                        [InlineKeyboardButton(text=f"🦅 ᴅᴇʟᴇᴛᴇ ʟᴏɢ 🦅", callback_data=f'close_data')],
                    ]
                reply_markup=InlineKeyboardMarkup(btn)
                header_credit = f"<b>User:-</b> {message.from_user.mention}\n<b>Query:-</b> {users_message}\n\n<b>📄 Answer:-</b> 👇"
                ai_response = response.choices[0].text
                await client.send_message(AI_LOGS, text=f"⚡️⚡️#AI_Query \n\n• A user named **{message.from_user.mention}** with user id - `{user_id}`. Asked me this query...\n\n**{users_message}**\n\nHere is what i responded:-\n\n`{ai_response}`\n\n\n❚═User ID:- `{user_id}` \n❚═User Name:- `{message.from_user.mention}`" , reply_markup = reply_markup)
                heh=await message.reply("🔎")
                await asyncio.sleep(2)
                await heh.edit(f"{header_credit}\n\n<code>{ai_response}</code>")
            except Exception as error:
                print(error)
    else:
        return