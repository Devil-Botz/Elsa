from pyrogram import Client, filters, enums
from pyrogram.types import *
from pymongo import MongoClient
from info import DATABASE_URl
import requests
import os
import re


API_ID = environ.get("API_ID", None) 
API_HASH = environ.get("API_HASH", None) 
BOT_TOKEN = environ.get("BOT_TOKEN", None) 
KUKI_API = environ.get("KUKI_API", None) 
ERROR_LOG = environ.get("ERROR_LOG", None) 
DATABASE_URI = environ.get("DATABASE_URI", None)


elsa = Client(
    "KukiBot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)

async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter=enums.ChatMemberStatus.ADMINISTRATOR
        )
    ]


@bot.on_message(
    filters.command("setupchat", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def addchat(_, message): 
    kukidb = MongoClient(DATABASE_URI)
    
    kuki = kukidb["KukiDb"]["Kuki"]
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_kuki = kuki.find_one({"chat_id": message.chat.id})
    if not is_kuki:
        kuki.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"✅ | Successfully\nElsa Chatbot of this Group is set to @{message.chat.username}\n Requested by [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n© @cinemala_com1)
    else:
        await message.reply_text(f"Already Setup Elsa Chatbot of this Group Is @{message.chat.username}")


@elsa.on_message(
    filters.command("removechat", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def rmchat(_, message): 
    kukidb = MongoClient(DATABASE_URI)
    
    kuki = kukidb["KukiDb"]["Kuki"] 
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_kuki = kuki.find_one({"chat_id": message.chat.id})
    if not is_kuki:
        await message.reply_text("Already Elsa ChatBot Disable")
    else:
        kuki.delete_one({"chat_id": message.chat.id})
        await message.reply_text("✅ | Elsa Chatbot is disable!")





@elsa.on_message(
    filters.text
    & filters.reply
    & ~filters.private
    & ~filters.bot
    
)
async def elsaai(client: Client, message: Message):

   kukidb = MongoClient(MONGO_URL)
    
   kuki = kukidb["KukiDb"]["Kuki"] 

   is_kuki = kuki.find_one({"chat_id": message.chat.id})
   if is_kuki:
       if message.reply_to_message:      
           botget = await bot.get_me()
           botid = botget.id
           if not message.reply_to_message.from_user.id == botid:
               return
           await bot.send_chat_action(message.chat.id, "typing")
           if not message.text:
               msg = "/"
           else:
               msg = message.text
           try: 
               x = requests.get(f"https://kukiapi.xyz/api/apikey={KUKI_API}/message={msg}").json()
               x = x['reply']
               await asyncio.sleep(1)
           except Exception as e:
               error = str(e)
           await message.reply_text(x)
           await bot.send_message(
           ERROR_LOG, f"""{error}""")
           await bot.send_chat_action(message.chat.id, "cancel") 
   


@elsa.on_message(
    filters.text
    & filters.reply
    & filters.private
    & ~filters.bot
    
)
async def elsaai(client: Client, message: Message):
    await bot.send_chat_action(message.chat.id, "typing")
    if not message.text:
        msg = "/"
    else:
        msg = message.text
    try:
        x = requests.get(f"https://kukiapi.xyz/api/apikey={KUKI_API}/message={msg}").json()
        x = x['reply']
        await asyncio.sleep(1)
    except Exception as e:
        ERROR = str(e)
    await message.reply_text(x)
    await bot.send_message(
           ERROR_LOG, f"""{ERROR}""")
    await bot.send_chat_action(message.chat.id, "cancel")



@elsa.on_message(
    filters.command("chat", prefixes=["/", ".", "?", "-"]))
async def elsaai(client: Client, message: Message):
    await bot.send_chat_action(message.chat.id, "typing")
    if not message.text:
        msg = "/"
    else:
        msg = message.text.replace(message.text.split(" ")[0], "")
    try:
        x = requests.get(f"https://kukiapi.xyz/api/apikey={KUKI_API}/message={msg}").json()
        x = x['reply']
        await asyncio.sleep(1)
    except Exception as e:
        ERROR = str(e)
    await bot.send_message(
           ERROR_LOG, f"""{ERROR}""")
    await message.reply_text(x)
    





@elsa.on_message(filters.command(["aimode"], prefixes=["/", "!"]))
async def aimode(client, message):
    self = await bot.get_me()
    busername = self.username
    if message.chat.type != "private":
        buttons = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Click here",
                url=f"t.me/ElsaAutofilter_bot?aimode")]])
        await message.reply("Contact me in PM",
                            reply_markup=buttons)
        
    else:
        buttons = [[InlineKeyboardButton("Support", url="https://t.me/Elsasupportgp"),
                    InlineKeyboardButton("Channel", url="https://t.me/cinemala_com1"),
                    InlineKeyboardButton("Repo", url="https://github.com/Devil-Botz/Elsa")
                    ]]
        Photo = "https://telegra.ph/file/5246027a503f37a897c62.jpg"
        await message.reply_photo(Photo, caption=f"Hello [{message.from_user.first_name}](tg://user?id={message.from_user.id}), Machine Learning Chat Bot that can talk about any topic in any language\n /aihelp - Help Commands\n Powered By @cinemala_com1", reply_markup=InlineKeyboardMarkup(buttons))



@elsa.on_message(filters.command(["aihelp"], prefixes=["/", "!"]))
async def aihelp(client, message):
    self = await bot.get_me()
    busername = self.username
    if message.chat.type != "private":
        buttons = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Click here",
                url=f"t.me/ElsaAutofilter_bot?start=aihelp_")]])
        await message.reply("Contact me in PM",
                            reply_markup=buttons)
        
    else:    
        await message.reply_text("/aimod - Start The Bot\n/chat - Send a message to this bot\n/setupchat - Active Elsa Chatbot In Group\n/removechat - Disable Elsa Chatbot In Group")






elsa.run()
