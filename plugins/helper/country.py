from countryinfo import CountryInfo
from pyrogram import Client, filters, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["country"]))
async def country_info(update: Message):
    country = update.text.split(" ", 1)[1]
    country = CountryInfo(country)
    info = f"""--**Country Information**--

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

©CINEMALA.COM """
    country_name = country.name()
    country_name = country_name.replace(" ", "+")
    reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Wikipedia', url=f'{country.wiki()}'),
        InlineKeyboardButton('Google', url=f'https://www.google.com/search?q={country_name}')
        ]]
    )
    try:
        await update.reply_text(
            text=info,
            reply_markup=reply_markup,
            disable_web_page_preview=True,
            quote=True
        )
    except Exception as error:
        await update.reply_text(
            text=error,
            disable_web_page_preview=True,
            quote=True
        )
