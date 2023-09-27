class script(object):
    START_TXT = """<b>𝙷𝙴𝙻𝙻𝙾 {},
ഞാൻ ഒരു 𝐆𝐑𝐎𝐔𝐏 𝐌𝐀𝐍𝐀𝐆𝐈𝐍𝐆 𝐁𝐎𝐓 ആണ്, എന്നെ നിങ്ങളുടെ ഗ്രൂപ്പിൽ ആഡ് ചെയ്യാൻ നോക്കി സമയം കളയണ്ട, എന്നെ 𝗔𝗥𝗔𝗞𝗔𝗟 𝗧𝗛𝗘𝗥𝗔𝗩𝗔𝗗 𝗠𝗢𝗩𝗜𝗘𝗦  𝗧𝗘𝗔𝗠  ഗ്രൂപ്പിൽ മാത്രമേ ആഡ് ചെയ്യാൻ കഴിയൂ...!!!

    HELP_TXT = "Hᴇʏ {}\nHᴇʀᴇ Mꜱ Mʏ Hᴇʟᴩ"
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂.</b>"""


# ⚠️ Please don't change our credits 𝚃𝙷𝙰𝙽𝙺𝚂 𝚃𝙾 & 𝙳𝙴𝚅 👇🏻

    ABOUT_TXT = """<b> 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a https://t.me/ARAKAL_THERAVAD_MOVIES>ARAKAL_THERAVAD_MOVIES.𝙲𝙾𝙼</a>
 𝚃𝙷𝙰𝙽𝙺𝚂 𝚃𝙾: <a href=https://t.me/OTT_ARAKAL_THERAVAD_MOVIES>ARAKAL_THERAVAD_MOVIES</a>
 𝙳𝙴𝚅: <a https://t.me/ARAKAL_THERAVAD_MOVIES> ARAKAL_THERAVAD_MOVIES </a>
 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: ARAKAL_THERAVAD_MOVIES
 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: ARAKAL_THERAVAD_MOVIES
 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: ARAKAL_THERAVAD_MOVIES
 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: ARAKAL_THERAVAD_MOVIES
 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v2.0.1 [ 𝙱𝙴𝚃𝙰 ]</b>"""

    SOURCE_TXT = """<b>NOTE:</b>
<b>- 𝙴𝙻𝚂𝙰 𝙸𝚂 𝙾𝙿𝙴𝙽 𝚂𝙾𝚄𝚁𝙲𝙴 𝙿𝚁𝙾𝙹𝙴𝙲𝚃. 
- 𝚂𝙾𝚄𝚁𝙲𝙴 - 𝙲𝙻𝙸𝙲𝙺 𝚁𝙴𝙿𝙾 𝙱𝚄𝚃𝚃𝙾𝙽</b>
<b>DEVS:</b>
- <a href=https://t.me/ARAKAL_THERAVAD_MOVIES>ARAKAL_THERAVAD_MOVIES.𝙲𝙾𝙼</a>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

<b>- 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝚂 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝚆𝙴𝚁𝙴 𝚄𝚂𝙴𝚁𝚂 𝙲𝙰𝙽 𝚂𝙴𝚃 𝙰𝚄𝚃𝙾𝙼𝙰𝚃𝙴𝙳 𝚁𝙴𝙿𝙻𝙸𝙴𝚂 𝙵𝙾𝚁 𝙰 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻𝙰𝚁 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙰𝙽𝙳 𝙴𝙻𝚂𝙰 𝚆𝙸𝙻𝙻 𝚁𝙴𝚂𝙿𝙾𝙽𝙳 𝚆𝙷𝙴𝙽𝙴𝚅𝙴𝚁 𝙰 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙸𝚂 𝙵𝙾𝚄𝙽𝙳 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴</b>

<b>NOTE:</b>
<b> 𝙴𝙻𝚂𝙰 𝚂𝙷𝙾𝚄𝙻𝙳 𝙷𝙰𝚅𝙴 𝙰𝙳𝙼𝙸𝙽 𝙿𝚁𝙸𝚅𝙸𝙻𝙻𝙰𝙶𝙴.
 𝙾𝙽𝙻𝚈 𝙰𝙳𝙼𝙸𝙽𝚂 𝙲𝙰𝙽 𝙰𝙳𝙳 𝙵𝙸𝙻𝚃𝙴𝚁𝚂 𝙸𝙽 𝙰 𝙲𝙷𝙰𝚃.
 𝙰𝙻𝙴𝚁𝚃 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝙷𝙰𝚅𝙴 𝙰 𝙻𝙸𝙼𝙸𝚃 𝙾𝙵  𝙲𝙷𝙰𝚁𝙰𝙲𝚃𝙴𝚁𝚂.</b>

<b>Commands and Usage:</b>
 /filter - <code>add a filter in chat</code>
 /filters - <code>list all the filters of a chat</code>
 /del - <code>delete a specific filter in chat</code>
 /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

<b>𝙴𝙻𝚂𝙰 𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝚂 𝙱𝙾𝚃𝙷 𝚄𝚁𝙻 𝙰𝙽𝙳 𝙰𝙻𝙴𝚁𝚃 𝙸𝙽𝙻𝙸𝙽𝙴 𝙱𝚄𝚃𝚃𝙾𝙽𝚂.</b>
<b>NOTE:</b>
<b> 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚆𝙸𝙻𝙻 𝙽𝙾𝚃 𝙰𝙻𝙻𝙾𝚆𝚂 𝚈𝙾𝚄 𝚃𝙾 𝚂𝙴𝙽𝙳 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚆𝙸𝚃𝙷𝙾𝚄𝚃 𝙰𝙽𝚈 𝙲𝙾𝙽𝚃𝙴𝙽𝚃, 𝚂𝙾 𝙲𝙾𝙽𝚃𝙴𝙽𝚃 𝙸𝚂 𝙼𝙰𝙽𝙳𝙰𝚃𝙾𝚁𝚈.
 𝙴𝙻𝚂𝙰 𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝚂 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚆𝙸𝚃𝙷 𝙰𝙽𝚈 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙼𝙴𝙳𝙸𝙰 𝚃𝚈𝙿𝙴.
 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚂𝙷𝙾𝚄𝙻𝙳 𝙱𝙴 𝙿𝚁𝙾𝙿𝙴𝚁𝙻𝚈 𝙿𝙰𝚁𝚂𝙴𝙳 𝙰𝚂 𝙼𝙰𝚁𝙺𝙳𝙾𝚆𝙽 𝙵𝙾𝚁𝙼𝙰𝚃</b>
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Example...)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>

 𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙳𝙾𝙴𝚂 𝙽𝙾𝚃 𝙲𝙾𝙽𝚃𝙰𝙸𝙽𝚂 𝙲𝙰𝙼𝚁𝙸𝙿𝚂, 𝙿𝙾𝚁𝙽 𝙰𝙽𝙳 𝙵𝙰𝙺𝙴 𝙵𝙸𝙻𝙴𝚂.
 𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝚃𝙷𝙴 𝙻𝙰𝚂𝚃 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝙼𝙴 𝚆𝙸𝚃𝙷 𝚀𝚄𝙾𝚃𝙴𝚂.
<b> /set_template - 𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙵𝙾𝚁 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁.</b>
<b> /get_template - 𝙶𝙴𝚃 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙾𝙵 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁.</b>
<b> /autofilter on - 𝙴𝙽𝙰𝙱𝙻𝙴 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿𝚂.</b>
<b> /autofilter off - 𝙳𝙸𝚂𝙰𝙱𝙻𝙴𝙳 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿𝚂.</b>"""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
 Only admins can add a connection.
 Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
 /connect  - <code>connect a particular chat to your PM</code>
 /disconnect  - <code>disconnect from a chat</code>
 /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Elsa

<b>Commands and Usage:</b>
 /id - <code>get id of a specified user.</code>
 /info  - <code>get information about a user.</code>
 /imdb  - <code>get the film information from IMDb source.</code>
 /search  - <code>get the film information from various sources.</code>"""

    SONG_TXT = """<b>𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴</b>

<i>𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴, 𝙵𝙾𝚁 𝚃𝙷𝙾𝚂𝙴 𝚆𝙷𝙾 𝙻𝙾𝚅𝙴 𝙼𝚄𝚂𝙸𝙲. 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙵𝙴𝙰𝚃𝚄𝙴 𝙵𝙾𝚁 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚂𝙾𝙽𝙶 𝚆𝙸𝚃𝙷 𝚂𝚄𝙿𝙴𝚁 𝙵𝙰𝚂𝚃 𝚂𝙿𝙴𝙴𝙳.𝚆𝙾𝚁𝙺𝚂 𝙾𝙽𝙻𝚈 𝙾𝙽 𝙶𝚁𝙾𝚄𝙿𝚂../</i>

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂</b>

 /song 𝚂𝙾𝙽𝙶 𝙽𝙰𝙼𝙴 

<b>𝚆𝙾𝚁𝙺𝚂 𝙱𝙾𝚃𝙷 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙿𝙼</b>
@ARAKAL_THERAVAD_MOVIES"""

    VIDEO_TXT ="""𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴.
 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦
𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (https://youtu.be/example...)
 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
<code>/mp4 https://youtu.be/example...</code>
<code>/video https://youtu.be/example...</code>"""

    TTS_TXT = """Help: <b> TTS  module:</b>
Translate text to speech
<b>Commands and Usage:</b>
 /tts <text> : convert text to speech"""

    GTRANS_TXT = """ 𝐇𝐞𝐥𝐩: 𝖦𝗈𝗈𝗀𝗅𝖾 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋
𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚝𝚛𝚊𝚗𝚜𝚕𝚊𝚝𝚎 𝚊 𝚝𝚎𝚡𝚝 𝚝𝚘 𝖺𝗇𝗒 𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎𝚜 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝. 𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚠𝚘𝚛𝚔𝚜 𝚘𝚗 𝚋𝚘𝚝𝚑 𝚙𝚖 𝚊𝚗𝚍 𝚐𝚛𝚘𝚞𝚙 
 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾
 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾
𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    TELE_TXT = """<b>HELP: Telegraph </b>
Do as you wish with telegra.ph module!
</b>USAGE:</b>
<b>NOTE:</b>
 This Command Is Available in goups and pms
 This Command Can be used by everyone"""

    CORONA_TXT = """ 𝐇𝐞𝐥𝐩: 𝖢𝗈𝗏𝗂𝖽
𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚔𝚗𝚘𝚠 𝚍𝚊𝚒𝚕𝚢 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝚌𝚘𝚟𝚒𝚍 
 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
 /covid - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾 𝗍𝗈 𝗀𝖾𝗍 𝖼𝗈𝗏𝗂𝖽𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇
𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/covid 𝖨𝗇𝖽𝗂𝖺</code>

 This service has been stopped"""

    ABOOK_TXT = """ 𝐇𝐞𝐥𝐩: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄
𝚈𝚘𝚞 𝚌𝚊𝚗 𝚌𝚘𝚗𝚟𝚎𝚛𝚝 𝚊 𝙿𝙳𝙵 𝚏𝚒𝚕𝚎 𝚝𝚘 𝚊 𝚊𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚝𝚑 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 
 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
 /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""

    DEPLOY_TXT= """𝙸𝙵 𝚈𝙾𝚄 𝙵𝙰𝙲𝙸𝙽𝙶 𝙰𝙽𝚈 𝙸𝚂𝚂𝚄𝙴 𝙸𝙽 𝚃𝙷𝙴 𝚁𝙴𝙿𝙾 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙼𝙴..."""
   
    PINGS_TXT = """<b>Ping Testing:</b>
Helps you to know your ping 
<b>Commands:</b>
 /alive - To check you are alive.
 /help - To get help.

 /ping - <b>To get your ping.</b>

<b> Usage :</b>
 This commands can be used in pm and groups
 This commands can be used buy everyone in the groups and bots pm
 Share us for more features"""
 
    STICKER_TXT = """<b>𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚃𝙾 𝙵𝙸𝙽𝙳 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁𝚂 𝙸𝙳.</b>
 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID
 
   𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
 
 Reply To Any Sticker [/stickerid]"""

    FONT_TXT= """ 𝐔𝐒𝐀𝐆𝐄

𝐘𝐎𝐔 𝐂𝐀𝐍 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐌𝐎𝐃𝐔𝐋𝐄 𝐓𝐎 𝐂𝐇𝐀𝐍𝐆𝐄 𝐅𝐎𝐍𝐓 𝐒𝐓𝐘𝐋𝐄 

<b>COMMAND</b> : /font your text (optional)
        <b> Eg:- /font Hello</b>

 <i>This feature added by @ARAKAL_THERAVAD_MOVIES"""
    JSON_TXT = """<b>JSON:</b>
Bot returns json for all replied messages with /json or /js
<b>Features:</b>
Message Editting JSON
Pm Support
Group Support
<b>Note:</b>
<b>Everyone can use this command , if spaming happens bot will automatically ban you from the group.</b>"""

    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- <b>Give a user details</b>

/whois :-give a user full details 📑"""

    URLSHORT_TXT = """ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋
<i><b>𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 </i></b>
 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
 /short: <b>𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌</b>
𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/example...</code>"""

    FUN_TXT ="""<b>Gᴀᴍᴇs</b> 
    
<b>⚡ 𝙹𝚄𝚂𝚃 𝚂𝙾𝙼𝙴 𝙺𝙸𝙽𝙳 𝙾𝙵 𝙵𝚄𝙽 𝚃𝙷𝙸𝙽𝙶'𝚂 ⚡</b>
 
 /dice - 𝚁𝙾𝙻𝙴 𝚃𝙷𝙴 𝙳𝙸𝙲𝙴 
 /Throw 𝗈𝗋 /Dart - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙳𝙰𝚁𝚃 
 /Runs - 𝚂𝙾𝙼𝙴 𝚁𝙰𝙽𝙳𝙾𝙼 𝙳𝙸𝙰𝙻𝙾𝙶𝚄𝙴𝚂 
 /Goal or /Shoot - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙰 𝙶𝙾𝙰𝙻 𝙾𝚁 𝚂𝙷𝙾𝙾𝚃
 /luck or /cownd - 𝚂𝙿𝙸𝙽 𝙰𝙽𝙳 𝚃𝚁𝚈 𝚈𝙾𝚄𝚁 𝙻𝚄𝙲𝙺"""

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
 /logs - <code>to get the rescent errors</code>
 /stats - <code>to get status of files in db.</code>
 /delete - <code>to delete a specific file from db.</code>
 /users - <code>to get list of my users and ids.</code>
 /chats - <code>to get list of the my chats and ids </code>
 /leave  - <code>to leave from a chat.</code>
 /disable  -  <code>do disable a chat.</code>
 /ban  - <code>to ban a user.</code>
 /unban  - <code>to unban a user.</code>
 /channel - <code>to get list of total connected channels</code>
 /broadcast - <code>to broadcast a message to all users</code>
 /grp_broadcast - <code>to broadcast a message to all groups</code>
 /gfilter - <code>To add global filter</code>
 /gfilters - <code>To view global filters</code>
 /delallg - <code>To delete all global filters from database</code>
 /delg - <code>To delete a specific global filter</code>
 /setskip - <code>Skip no of files before indexing</code>
 /send - <code>Send any message through bot to users. /send (username/userid) reply with message </code>
 /deletefiles - <code>Delete CamRip and PreDvD files delete from database </code>"""
    
    STATUS_TXT = """<b> 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱</b>"""

    CARB_TXT = """<b>Help</b> : 𝗖𝗔𝗥𝗕𝗢𝗡
𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝚂 𝙰 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝙾 𝙼𝙰𝙺𝙴 𝚃𝙷𝙴 𝙸𝙼𝙰𝙶𝙴 𝙰𝚂 𝚂𝙷𝙾𝚆𝙽 𝙸𝙽 𝚃𝙷𝙴 𝚃𝙾𝙿 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁𝙴 𝚃𝙴𝚇𝚃𝚂.
𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙴 𝙼𝙾𝙳𝚄𝙻𝙴 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝚃𝙴𝚇𝚃 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙸𝚃 𝚆𝙸𝚃𝙷 /carbon 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚁𝙴𝙿𝙻𝚈 𝚆𝙸𝚃𝙷 𝚃𝙷𝙴 𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝙼𝙰𝙶𝙴"""


    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
Elsa
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
Elsa
"""
    FILE_MSG = """
<b>Hai 👋 {} </b>😍

<b>📫 Your File is Ready</b>

<b>📂 Fɪʟᴇ Nᴀᴍᴇ</b> : <b><code><b>{}</b></code></b>              
                       
<b>⚙️ Fɪʟᴇ Sɪᴢᴇ</b> : <b>{}</b>
"""
    CHANNEL_CAP = """
<b>Hai 👋 {}</b> 😍

<b><code>{}</code></b>

⚠️ <b>ഇവിടെ നിന്നും വേറെ എവിടേലും മാറ്റിയതിന് ശേഷം ഡൗൺലോഡ് ചെയ്യുക... !!!</b>

<b>കോപ്പി റൈറ്റ് ഉള്ളത് കൊണ്ട് ഈ ഒരു ഫയൽ 10 മിനിറ്റ് കൊണ്ട് ഇവിടെ നിന്നും ഡിലേറ്റാവും...!!!</b>

<b>╔════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
♻️ 𝙅𝙊𝙄𝙉 :- <a href="https://t.me/OTT_ARAKAL_THERAVAD_MOVIES">OTT UPDATES</a>
♻️ 𝙅𝙊𝙄𝙉 :- <a href="t.me/ARAKAL_THERAVAD_GROUP_LINKS">CHANNEL</a>
♻️ 𝙅𝙊𝙄𝙉 :- <a href="t.me/ARAKAL_THERAVAD_MOVIES">GROUP</a>
╚════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝</b>
"""
    SUR_TXT = """
<b>
𝙷𝙴𝙻𝙻𝙾 {},

 ഞാൻ ഒരു 𝐆𝐑𝐎𝐔𝐏 𝐌𝐀𝐍𝐀𝐆𝐈𝐍𝐆 𝐁𝐎𝐓 ആണ്, എന്നെ നിങ്ങളുടെ ഗ്രൂപ്പിൽ ആഡ് ചെയ്യാൻ നോക്കി സമയം കളയണ്ട, എന്നെ 𝗔𝗥𝗔𝗞𝗔𝗟 𝗧𝗛𝗘𝗥𝗔𝗩𝗔𝗗 𝗠𝗢𝗩𝗜𝗘𝗦  𝗧𝗘𝗔𝗠  ഗ്രൂപ്പിൽ മാത്രമേ ആഡ് ചെയ്യാൻ കഴിയൂ...!!!
</b>"""

    IMDB_TEMPLATE_TXT = """
<b>🔖 ᴛɪᴛʟᴇ :<a href={url}>{title}</a>

🎭 ɢᴇɴʀᴇs : {genres}
🎖 ʀᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a> / 10 (ʙᴀsᴇᴅ ᴏɴ {votes} ᴜsᴇʀ ʀᴀᴛɪɴɢ.)

📆 ʏᴇᴀʀ : {release_date}
🗞 ʟᴀɴɢᴜᴀɢᴇ : {languages}
🌎 ᴄᴏᴜɴᴛʀʏ : {countries}

©{message.chat.title}</b>
"""

    CUSTOM_FILE_CAPTION = """<b>📂Fɪʟᴇɴᴀᴍᴇ : {file_name}



╔════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
▫️<a href=https://t.me/ARAKAL_THERAVAD_MOVIES> ᴄʜᴀɴɴᴇʟ </a>

▫️<a href=https://t.me/OTT_ARAKAL_THERAVAD_MOVIES> sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ </a>
╚════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝</b>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !
📅 Dᴀᴛᴇ : <code>{}</code>
⏰Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️"""

    ALRT_TXT = """ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏʏ ꜱɪʀ"""

    OLD_ALRT_TXT = """𝐘𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐨𝐧𝐞 𝐨𝐟 𝐦𝐲 𝐨𝐥𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐠𝐚𝐢𝐧 """

    TOP_ALRT_MSG = """♻️ ᴄʜᴇᴄᴋɪɴɢ ꜰɪʟᴇ ᴏɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ... ♻️"""

    MVE_NT_FND = """<b>‼️ FILE NOT FOUND ? ‼️

1️⃣ സിനിമയുടെ സ്പെല്ലിങ്ങ് ഗൂഗിളിൽ ഉള്ളത് പോലെ ആണോ നിങ്ങൾ അടിച്ചത് എന്ന് ഉറപ്പ് വരുത്തുക..!!

 2️⃣ നിങ്ങൾ ചോദിച്ച സിനിമ OTT റിലീസ് ആയതാണോ എന്ന് @https:@OTT_ARAKAL_THERAVAD_MOVIES യിൽ ചെക്ക് ചെയ്യുക..!!

3️⃣ മൂവിക്ക് വേണ്ടി മെസ്സേജ് അയക്കുമ്പോൾ മൂവിയുടെ പേര് ഇറങ്ങിയ വർഷം മാത്രം അയക്കുക..!!

4⃣ ‼ 𝖱𝖾𝗉𝗈𝗋𝗍 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 ▶ @ARAKAL_THERAVAD_MOVIES_02_bot</b> """

    NORSLTS = """ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 
𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>
𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    I_CUDNT = """<b>ʜᴇʟʟᴏ {} ‼️ FILE NOT FOUND ? ‼️

1️⃣ സിനിമയുടെ സ്പെല്ലിങ്ങ് ഗൂഗിളിൽ ഉള്ളത് പോലെ ആണോ നിങ്ങൾ അടിച്ചത് എന്ന് ഉറപ്പ് വരുത്തുക..!!

 2️⃣ നിങ്ങൾ ചോദിച്ച സിനിമ OTT റിലീസ് ആയതാണോ എന്ന്  @OTT_ARAKAL_THERAVAD_MOVIES യിൽ ചെക്ക് ചെയ്യുക..!!

3️⃣ മൂവിക്ക് വേണ്ടി മെസ്സേജ് അയക്കുമ്പോൾ മൂവിയുടെ പേര് ഇറങ്ങിയ വർഷം മാത്രം അയക്കുക..!!</b>"""

    I_CUD_NT = """ʜᴇʟʟᴏ {} ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ.ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴘᴇʟʟɪɴɢ."""
    
    CUDNT_FND = """<b>ʜᴇʟʟᴏ {} BRO നിങ്ങള് ഉദ്ദേശിച്ച മൂവി താഴെക്കൊടുത്തിരിക്കുന്നതിൽ ഏതാണെന്ന് SPELLING നോക്കി CURRET ആയി  CLICK ചെയ്യുക...</b>👇🏻"""

    REPRT_MSG = """ Reported To Admin"""

    CON_TXT = """<b><u>ᴄᴏᴜɴᴛʀʏ ɪɴғᴏ</b></u>
<b>Tʜɪs ᴍᴏᴅᴜʟᴇ ɪs ᴛᴏ ғɪɴᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴄᴏᴜɴᴛʀɪᴇs</b>
 /country [𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾] 
𝖤𝗑𝖺𝗆𝗉𝗅𝖾 :- <code>/country India</code>"""
