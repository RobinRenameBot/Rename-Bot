import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","AshutoshGoswami24")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    PORT = int(os.environ.get("PORT", ""))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 
    I ᴀᴍ Nᴇᴄᴏ Rᴏʙɪɴ I Cᴀɴ Rᴇɴᴀᴍᴇ Fɪʟᴇ Wɪᴛʜ Pᴀʀᴍᴀɴᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Mᴀᴋᴇ Oᴜᴛᴘᴜᴛ Wɪᴛʜ Yᴏᴜʀ Dᴇsɪʀᴇᴅ Fᴏʀᴍᴀᴛ Tʀʏ Tᴏ Usᴇ Mᴇ Oʀ Sᴇɴᴅ /ʜᴇʟᴘ Fᴏʀ Mᴏʀᴇ Assɪsᴛᴇɴᴛs.
"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ episode :- To Replace Episode Number
✓ quality :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename Naruto Shippuden S02 - EPepisode - quality  [Dual Audio] - @PandaWep </code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""
<b>○ Cʜᴀɴɴᴀʟ :</b> <a href='https://t.me/AnimeQuestX'>Aɴɪᴍᴇ Qᴜᴇsᴛ</a>
<b>○ Hɪɴᴅɪ Cʜᴀɴɴᴀʟ :</b> <a href='https://t.me/AnimeQuestHindi'>Jᴏɪɴ Nᴏᴡ</a>
<b>○ Oɴɢᴏɪɴɢ Cʜᴀɴɴᴀʟ :</b> <a href='https://t.me/OngoingAnimeQuest'>Jᴏɪɴ Nᴏᴡ</a>
<b>○ Dɪsᴄᴜssᴛɪᴏɴ Gʀᴏᴜᴘ :</b> <a href='https://t.me/+r-x-wA4JT5gxZjVl'>Jᴏɪɴ Nᴏᴡ</a>
<b>○ Oᴡɴᴇʀ :</b> <a href='https://t.me/abidabdullah199'>Mᴏɴᴋᴇʏ D Lᴜғғʏ</a>
"""

    
    THUMBNAIL_TXT = """<b><u>  Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>  Hᴏᴡ Tᴏ Sᴇᴛ Cᴀᴘᴛɪᴏɴ</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣ 🗃️ Sɪᴢᴇ: {1} | {2}
┣ ⏳️ Dᴏɴᴇ : {0}%
┣ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣ ⏰️ Eᴛᴀ: {4}
┣ 🥺 Join: @AnimeQuestX
╰━━━━━━━━━━━━━━━ </b>"""
    
    
    DONATE_TXT = """<b>Dᴏɴᴀᴛᴇ Tʜᴏᴏsᴇ Wʜᴏ Rᴇᴀʟʟʏ Nᴇᴇᴅ Iᴛ ❤️</b>
    
 """
    
    HELP_TXT = """Iɴʙᴏx Mᴇ @abidabdullah199 """





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @PandaWep
# Developer @AshutoshGoswami24
