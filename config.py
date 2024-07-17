import os, time

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "26254064")
    API_HASH  = os.environ.get("API_HASH", "72541d6610ae7730e6135af9423b319c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7269172401:AAFA4yLE41qefijtSBTCIUhhwxfqzDNVXLg") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","renamerobin1")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://abidabdullahown2:fvAc5i50qYp6XG4t@cluster0.htgtti7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/3eccd2f7861028d08db2d.jpg")
    ADMIN = int(os.environ.get("ADMIN", "5296584067"))

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "-1002125561929") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002172487703"))
    

    # wes response configuration     
    PORT = int(os.environ.get("PORT", "8000"))
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))

#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot

class Txt(object):
    # part of text configuration
    START_TXT = """Hᴇʟʟᴏ {}
Iᴀᴍ Kᴀᴡᴀɪ Nɪᴄᴏ Rᴏʙɪɴ! I ᴄᴀɴ Rᴇɴᴀᴍᴇ , Aᴅᴅ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Aʟsᴏ Cᴏɴᴠᴇʀᴛ Yᴏᴜʀ Fɪʟᴇs Iɴᴛᴏ Vɪᴅᴇᴏ Oʀ Aᴅᴠᴀɴᴄᴇᴅ Fɪʟᴇ Fᴏʀᴍᴀᴛ Aɴᴅ I Hᴀᴠᴇ Aʟsᴏ Fᴀsᴛ Sᴘᴇᴇᴅ. Tʀʏ Usɪɴɢ Mᴇ!
#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot
    ABOUT_TXT = """

<b>Mʏ Bᴏᴛ Nᴀᴍᴇ</b> : {}
<b>Oᴡɴᴇʀ</b> : <a href=https://t.me/abidabdullah199>Mᴏɴᴋᴇʏ D Lᴜғғʏ</a> 
<b>Cʜᴀɴɴᴀʟ</b> : <a href=https://t.me/AnimeQuestX >Aɴɪᴍᴇ Qᴜᴇsᴛ</a>
<b>Hɪɴᴅɪ Cʜᴀɴɴᴀʟ</b> : <a href=https://t.me/AnimeQuestHindi>Jᴏɪɴ Nᴏᴡ</a>
<b>Oɴɢᴏɪɴɢ Cʜᴀɴɴᴀʟ</b> : <a href=https://t.me/OngoingAnimeQuest >Jᴏɪɴ Nᴏᴡ</a>
<b>Dɪsᴄᴜssᴛɪᴏɴ Gʀᴏᴜᴘ</b> : <a href=https://t.me/+r-x-wA4JT5gxZjVl>Jᴏɪɴ Nᴏᴡ</a>
<b>Eʀʀᴏʀ Rᴇᴘᴏʀᴛ</b> : <a href=https://t.me/abidabdullah199>Cʟɪᴄᴋ Hᴇʀᴇ</a></b>     

"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/AshutoshGoswami24>Developer</a>
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼ 🥺 joine Plz: @PandaWep
╰━━━━━━━━━━━━━━━➣ </b>"""
#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot
    DONATE_TXT = """
<b>𝗧𝗵𝗮𝗻𝗸𝘀 𝗙𝗼𝗿 𝗦𝗵𝗼𝘄𝗶𝗻𝗴 𝗜𝗻𝘁𝗲𝗿𝗲𝘀𝘁 𝗜𝗻 𝗗𝗼𝗻𝗮𝘁𝗶𝗼𝗻! ❤️</b>

𝐈𝐟 𝐘𝐨𝐮 𝐋𝐢𝐤𝐞 𝐌𝐲 𝐁𝐨𝐭𝐬 & 𝐏𝐫𝐨𝐣𝐞𝐜𝐭𝐬, 𝐘𝐨𝐮 𝐂𝐚𝐧 🎁 𝐃𝐨𝐧𝐚𝐭𝐞 𝐌𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐅𝐫𝐨𝐦 𝟏𝟎𝐌 𝐑𝐬 😁 𝐔𝐩𝐭𝐨 𝐘𝐨𝐮𝐫 𝐂𝐡𝐨𝐢𝐜𝐞.

<b>🛍 𝗨𝗣𝗜 𝗜𝗗:</b> `PandaWep@ybl`
"""

#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot
