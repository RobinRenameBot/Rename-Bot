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
    FORCE_SUB   = os.environ.get("FORCE_SUB", "@abidabdullah199") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "@robinfilerenamelog"))
    

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

<b>○ Mʏ Bᴏᴛ Nᴀᴍᴇ</b> : {}
<b>○ Oᴡɴᴇʀ</b> : <a href=https://t.me/abidabdullah199>Mᴏɴᴋᴇʏ D Lᴜғғʏ</a> 
<b>○ Cʜᴀɴɴᴀʟ</b> : <a href=https://t.me/AnimeQuestX >Aɴɪᴍᴇ Qᴜᴇsᴛ</a>
<b>○ Hɪɴᴅɪ Cʜᴀɴɴᴀʟ</b> : <a href=https://t.me/AnimeQuestHindi>Jᴏɪɴ Nᴏᴡ</a>
<b>○ Oɴɢᴏɪɴɢ Cʜᴀɴɴᴀʟ</b> : <a href=https://t.me/OngoingAnimeQuest >Jᴏɪɴ Nᴏᴡ</a>
<b>○ Dɪsᴄᴜssᴛɪᴏɴ Gʀᴏᴜᴘ</b> : <a href=https://t.me/+r-x-wA4JT5gxZjVl>Jᴏɪɴ Nᴏᴡ</a>
<b>○ Eʀʀᴏʀ Rᴇᴘᴏʀᴛ</b> : <a href=https://t.me/abidabdullah199>Cʟɪᴄᴋ Hᴇʀᴇ</a></b>     

"""

    HELP_TXT = """
 <b>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ<u></u></b>
  
○ /Start - [Cʟɪᴄᴋ Hᴇʀᴇ Oʀ Sᴛᴀʀᴛ Tɢᴇ Bᴏᴛ Tʜᴇɴ Sᴇɴᴅ Aɴʏ Iᴍᴀɢᴇ Tᴏ Sᴇᴛ Fɪʟᴇ Tʜᴜᴍʙɴᴀɪʟ.]
○ /del_thumb - [Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Cᴜʀʀᴇɴᴛʟʏ Rᴜɴɴɪɴɢ Tʜᴜᴍʙɴᴀɪʟ.]
○ /view_thumb - [Tʜɪs Cᴏᴍᴍᴀɴᴅ Wɪʟʟ Sʜᴏᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ Yᴏᴜ Aʀᴇ Usɪɴɢ.]

 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴀᴘᴛɪᴏɴs</u></b>

○ /set_caption - [Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ A Nᴇᴡ Cᴀᴘᴛɪᴏɴ.]
○ /see_caption - [Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴇ Cᴀᴘᴛɪᴏɴ Wʜᴀᴛ ʏᴏᴜ ᴀʀᴇ ᴜsɪɴɢ.]
○ /del_caption - [Tʜɪs Cᴏᴍᴍᴀɴᴅ Wɪʟʟ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ.]

○ Qᴜɪᴄᴋ Tᴜᴛᴏʀɪᴀʟ -
Fɪʀsᴛ Sᴇɴᴅ Tʜᴜᴍʙɴᴀɪʟ ᴛʜᴇɴ Sᴇɴᴅ , Uᴘʟᴏᴀᴅ Oʀ Fᴏʀᴡᴀʀᴅ Aɴʏ Fɪʟᴇ Tʜᴇɴ Cʜᴏᴏᴄᴇ Vɪᴅᴇᴏ Oʀ Dᴏᴄᴜᴍᴇɴᴛ Fɪʟᴇ Aғᴛᴇʀ Wᴀɪᴛɪɴɢ Sᴏᴍᴇᴛʜɪᴍᴇs Yᴏᴜ Wɪʟʟ Gᴇᴛ Rᴇsᴜʟᴛ.         

○ Fᴏʀ Mᴏʀᴇ Hᴇʟᴘ Sᴇɴᴅ Mᴇ A Qᴜɪᴄᴋ Mᴇssᴀɢᴇ :- <a href=https://t.me/abidabdullah199>Aᴅᴍɪɴ</a>
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ Pʀᴏɢʀᴇss Bᴀʀ ❱
┣○ 🗃️ Sɪᴢᴇ: {1} | {2}
┣○ ⏳️ Dᴏɴᴇ: {0}%
┣○ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣○ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━ </b>"""
#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot
    DONATE_TXT = """
<b>Dᴏɴᴀᴛᴇ Tʜᴏᴏsᴇ Wʜᴏ Rᴇᴀʟʟʏ Nᴇᴇᴅ Nᴏᴛ Mᴇ! ❤️</b>

#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot
