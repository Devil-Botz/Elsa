from countryinfo import CountryInfo
from pyrogram import Client, filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["country"]))
async def countryinfo(bot, update):
    
    country = CountryInfo(update.text)
    
    info = f"""**Country Information**

Name : ```{country.name()}```
Native Name : ```{country.native_name()}```
Capital : ```{country.capital()}```
Population : ```{country.population()}```
Region : ```{country.region()}```
Sub Region : ```{country.subregion()}```
Top Level Domains : ```{country.tld()}```
Calling Codes : ```{country.calling_codes()}``|
Currencies : ```{country.currencies()}```
Residence : ```{country.demonym()}```
Timezone : ```{country.timezones()}```

©CINEMALA.COM"""
    
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('Wikipedia', url=country.wiki()),
                InlineKeyboardButton('Google', url=country.google())
            ]
        ]
    )
    
    try:
        await update.reply_text(
            text=info,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    except Exception as error:
        print(error)
