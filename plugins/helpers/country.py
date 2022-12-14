from countryinfo import CountryInfo
from pyrogram import filters, Client 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Script import script

@Client.on_message(filters.command(["country"]))
async def country_info(bot, update):
    country = update.text.split(" ", 1)[1]
    country = CountryInfo(country)
    info = f"""π’ππππππ π¨ππΏππππΊππππ
π­πΊππΎ : {country.name()}
π­πΊππππΎ π­πΊππΎ : {country.native_name()}
π’πΊππππΊπ : {country.capital()}
Population : <code>{country.population()}</code>
π±πΎππππ : {country.region()}
π²ππ» π±πΎππππ : {country.subregion()}
π³ππ π«πΎππΎπ π£πππΊπππ : {country.tld()}
π’πΊπππππ π’ππ½πΎπ : {country.calling_codes()}
π’ππππΎππΌππΎπ : {country.currencies()}
π±πΎπππ½πΎππΌπΎ : {country.demonym()}
π³πππΎππππΎ : <code>{country.timezones()}</code>
"""
    country_name = country.name()
    country_name = country_name.replace(" ", "+")
    buttons=[[
      InlineKeyboardButton("α΄‘Ιͺα΄Ιͺα΄α΄α΄Ιͺα΄", url=f"{country.wiki()}"),
      InlineKeyboardButton("Ι’α΄α΄Ι’Κα΄", url=f"https://www.google.com/search?q={country_name}")
    ],[
       InlineKeyboardButton('α΄Κα΄sα΄', callback_data='close_data')
    ]]
    try:
        await update.reply_photo(
            photo="https://telegra.ph/file/834750cfadc32b359b40c.jpg",
            caption=info,
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
    except Exception as error:
        await update.reply_text(
            text=error,
            disable_web_page_preview=True,
            quote=True
        )
