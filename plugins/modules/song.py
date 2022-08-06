from __future__ import unicode_literals
import asyncio
import re
import math
import os
import time
import ffmpeg
import aiofiles
import aiohttp
import wget
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from youtubesearchpython import SearchVideos
import yt_dlp
from youtube_search import YoutubeSearch
import requests

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

@Client.on_message(filters.command(["song"]) & ~filters.channel)
def a(update, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply("**🎵 Processing**")
    ydl_opts = {
        "format": "bestaudio",
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ],
        "outtmpl": "downloads/%(track)s.mp3" ,
    }
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]

            if time_to_seconds(duration) >= 1800:  # duration limit
                 m.edit("Exceeded 30mins cap")
                 return

            performer = f"[Anything]" 
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True) 
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit("Server busy due to overload, Please try again later.")
            return
    except Exception as e:
        m.edit("Use a valid command , /song song name")
        print(str(e))
        return
    m.edit("**⬆️ Uploading**")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict) 
            ydl.process_info(info_dict)
        rep = f"""
♬ <b>Title : {title}</b>
♬ <b>Duration : {duration}</b>
♬ <b>Link : <a href='{link}'>Click here</a></b>
♬ <b>Requested By : {message.from_user.mention}</b>
        """
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(
        audio_file,
        caption=rep,
        parse_mode='HTML',
        quote=False,
        title=title,
        duration=dur,
        performer=performer,
        thumb=thumb_name,
        reply_to_message_id=message.message_id
        )
        m.delete()
    except Exception as e:
        m.edit(
          text='There is an error while processing your request.')  
        print(e)
    try: 
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
        
@Client.on_callback_query(filters.regex(r'verify\(.+\)'))
async def verify():
    id = int(re.findall(r'verify\(.+\)', update.data))
    if id!=update.from_user.id:
         update.answer("Sorry, I'm afraid that this button is not for you", show_alert=True)
    else: 
         update.answer("Please use the proper format for request a song", show_alert=True)
