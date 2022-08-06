from pyrogram import Client, filters
from info import ADMINS
import os 
from PIL import Image, ImageDraw, ImageFont


@Client.on_message(filters.command('logo'))
async def lego(event):
 quew = event.pattern_match.group(100)
 if event.sender_id == ADMINS:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(100)
    img = Image.open('./plugins/resources/blackbg (1).jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./plugins/resources/Chopsic.otf", 330)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
    fname2 = "mysterious"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Mysterious")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'error, {e}')
