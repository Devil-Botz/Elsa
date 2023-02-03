<p align="center">
  <img src="https://telegra.ph/file/930ff28f8e22e70b00cfa.jpg" alt="Devil Botz">
</p>
<h1 align="center">
  <b>Elsa</b>
</h1>

<p align="center">
    <img src="https://img.shields.io/github/license/Devil-Botz/Elsa?style=for-the-badge&logo=appveyor" alt="LICENSE" >
    <img src="https://img.shields.io/github/contributors/Devil-Botz/Elsa?style=for-the-badge&logo=appveyor" alt="Contributors">
    <img src="https://img.shields.io/github/repo-size/Devil-Botz/Elsa?style=for-the-badge&logo=appveyor" alt="Repository Size"> <br>
    <img src="https://img.shields.io/github/issues/Devil-Botz/Elsa?style=for-the-badge&logo=appveyor" alt="Issues">
    <img src="https://img.shields.io/github/forks/Devil-Botz/Elsa?style=for-the-badge&logo=appveyor" alt="Forks">
    <img src="https://img.shields.io/github/stars/Devil-Botz/Elsa?style=for-the-badge&logo=appveyor" alt="Stars">
</p>

## Features

- [x] Auto Filter
- [x] Manual Filter
- [x] IMDB
- [x] Admin Commands
- [x] Broadcast
- [x] Index
- [x] IMDB search
- [x] Inline Search
- [x] Random pics
- [x] ids and User info 
- [x] Stats, Users, Chats
- [x] Spelling Check Feature
- [x] File Store
- [x] 📂 PM & Channel 
- [x] Auto delete
- [x] 2GB+File Support
- [x] song video download
- [x] gfilter
- [x] group broadcast
- [x] telegraph
- [x] games
- [x] ping
- [x] pdf convert to voice
- [x] font
- [x] translate
- [x] PreDVD and CamRip Delete Mode
- [x] Multiple File Deletion

## Variables

### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com).
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). For more help watch this 
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.
* `SUPPORT_CHAT` : @Elsasupportgp
* `PICS`: Telegraph links of images to show in start message.( Multiple images can be used seperated by space )
* `FILE_FORWARD` : File redirect to channel telegram channel link eg: https://t.me/**************
* `DELETE_CHANNELS` : you can delete multiple files by forwarding those files into a private channel. Firstly make a private channel, add your bot as admin, add that channel's ID as a variable named DELETE_CHANNELS and forward the files to that private channel and the bot will delete those files from its database. You can check logs to confirm whether the file is deleted from the bot's database or not.
### Optional Variables

## Credits
<details>

 Thanks To [Mahesh](https://github.com/Mahesh0253/Media-Search-bot) MediaSearch

 Thanks To [Subinps](https://github.com/subinps/Media-Search-bot) AutoFilter & Base repo
 
 Thanks To [Joelkb](https://github.com/Joelkb) Collaborator [Add Redirect feature,Error fixed, Add new features]

 Thanks To [Devil-Botz](https://github.com/Devil-Botz) Owner,Add more features 


</details>

## Deploy
You can deploy this bot anywhere.


<details><summary>Deploy To Heroku</summary>
<br>
<p>
<a href="https://heroku.com/deploy?template=https://github.com/Devil-Botz/Elsa">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p></details>

<details><summary>Deploy To Koyeb</summary>
<br>
<p>
<a href="https://app.koyeb.com/deploy?type=git&repository=github.com/Devil-Botz/Elsa&env[BOT_TOKEN]&env[API_ID]&env[API_HASH]&env[CHANNELS]&env[ADMINS]&env[PICS]&env[LOG_CHANNEL]&env[AUTH_CHANNEL]&env[CUSTOM_FILE_CAPTION]&env[DATABASE_URI]&env[DATABASE_NAME]&env[COLLECTION_NAME]=Telegram_files&env[SUPPORT_CHAT]&env[IMDB]=True&env[IMDB_TEMPLATE]&env[SINGLE_BUTTON]=True&env[AUTH_GROUPS]&env[P_TTI_SHOW_OFF]=True&run_command=python%20bot.py&branch=main&name=Elsa">
 <img src="https://www.koyeb.com/static/images/deploy/button.svg">
</p>
</details>
<details><summary> Deploy To Okteto </summary>
<br>
<p>
<a href="https://cloud.okteto.com/deploy?repository=https://github.com/Devil-Botz/Elsa&branch=main">
  <img src="https://okteto.com/develop-okteto.svg" alt="Develop on Okteto">
</a>
</p>
</details>
<details><summary>Deploy To VPS</summary>
<p>
<pre>
git clone https://github.com/Devil-Botz/Elsa
# Install Packages
pip3 install -U -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>
</details>

## Commands

```
* /logs - to get the rescent errors
* /stats - to get status of files in db.
* /filter - add manual filters
* /filters - view filters
* /connect - connect to PM.
* /disconnect - disconnect from PM
* /del - delete a filter
* /delall - delete all filters
* /deleteall - delete all index(autofilter)
* /delete - delete a specific file from index.
* /info - get user info
* /id - get tg ids.* /imdb - fetch info from imdb.
* /users - to get list of my users and ids.
* /chats - to get list of the my chats and ids* /broadcast - to broadcast a message to all Elsa users
* /gfilter - group filter
* /grp_broadcast - broadcast to all group
* /song - get song
* /video - get video
* /setskip - used in index where indexing a specific number
* /font - fonts for your text
* /deletefiles - PreDvD CamRip deletion
```
<b> 😇CREATOR » [Aswin](https://t.me/Aswin_pm_Bot)</b>

## Disclaimer
[![GNU Affero General Public License 2.0](https://www.gnu.org/graphics/agplv3-155x51.png)](https://www.gnu.org/licenses/agpl-3.0.en.html#header)    
Licensed under [GNU AGPL 2.0.](https://github.com/Devil-Botz/Elsa-V3/blob/main/LICENSE)
Selling The Codes To Other People For Money Is *Strictly Prohibited*.

