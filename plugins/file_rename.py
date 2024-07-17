from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from helper.utils import progress_for_pyrogram, convert, humanbytes
from helper.database import AshutoshGoswami24
from asyncio import sleep
from PIL import Image
import os, time


@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name  
    if file.file_size > 2000 * 1024 * 1024:
         return await message.reply_text("Tʜɪs Bᴏᴛ Dɪᴅɴ'ᴛ Sᴜᴘᴘᴏʀᴛ Mᴏʀᴇ Tʜᴀɴ 2GB Sɪᴢᴇ Fɪʟᴇs.")

    try:
        await message.reply_text(
            text=f"**Eɴᴛᴇʀ Yᴏᴜʀ Nᴇᴡ Fɪʟᴇ Nᴀᴍᴇ **\n\n**Pʀᴇᴠɪᴏᴜs Fɪʟᴇ Nᴀᴍᴇ** - `{filename}`",
	    reply_to_message_id=message.id,  
	    reply_markup=ForceReply(True)
        )       
        await sleep(3)
    except FloodWait as e:
        await sleep(e.value)
        await message.reply_text(
            text=f"**Eɴᴛᴇʀ Yᴏᴜʀ Nᴇᴡ Fɪʟᴇ Nᴀᴍᴇ**\n\n**Pʀᴇᴠɪᴏᴜs Fɪʟᴇ Nᴀᴍᴇ** :- `{filename}`",
	    reply_to_message_id=message.id,  
	    reply_markup=ForceReply(True)
        )
    except:
        pass



@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    reply_message = message.reply_to_message
    if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
        new_name = message.text 
        await message.delete() 
        msg = await client.get_messages(message.chat.id, reply_message.id)
        file = msg.reply_to_message
        media = getattr(file, file.media.value)
        if not "." in new_name:
            if "." in media.file_name:
                extn = media.file_name.rsplit('.', 1)[-1]
            else:
                extn = "mkv"
            new_name = new_name + "." + extn
        await reply_message.delete()

        button = [[InlineKeyboardButton("📁 Dᴏᴄᴜᴍᴇɴᴛ Fᴏʀᴍᴀᴛ",callback_data = "upload_document")]]
        if file.media in [MessageMediaType.VIDEO, MessageMediaType.DOCUMENT]:
            button.append([InlineKeyboardButton("🎥 Vɪᴅᴇᴏ Fᴏʀᴍᴀᴛ", callback_data = "upload_video")])
        elif file.media == MessageMediaType.AUDIO:
            button.append([InlineKeyboardButton("🎵 Oʀ Aᴜᴅɪᴏ Fᴏʀᴍᴀᴛ", callback_data = "upload_audio")])
        await message.reply(
            text=f"**Select The Output File Type**\n\n**File Name :-** `{new_name}`",
            reply_to_message_id=file.id,
            reply_markup=InlineKeyboardMarkup(button)
        )



@Client.on_callback_query(filters.regex("upload"))
async def doc(bot, update):    
    prefix = await AshutoshGoswami24.get_prefix(update.message.chat.id)
    suffix = await AshutoshGoswami24.get_suffix(update.message.chat.id)
    new_name = update.message.text
    new_filename_ = new_name.split(":-")[1]

    try:
        if prefix and suffix:
            shorted = new_filename_[:-4:]
            extension = new_filename_[-4::]
            new_filename = f"{prefix} {shorted} {suffix}{extension}"
        
        elif prefix:
            shorted = new_filename_[:-4:]
            extension = new_filename_[-4::]
            new_filename = f"{prefix} {shorted}{extension}"
        
        elif suffix:
            shorted = new_filename_[:-4:]
            extension = new_filename_[-4::]
            new_filename = f"{shorted} {suffix}{extension}"
        
        else:
            new_filename = new_filename_
    except:
        await update.message.edit("⚠️  Cᴀɴ'ᴛ Sᴇᴛ Sᴜғғɪx Pʀᴇғɪx \n\n**Sᴇɴᴅ Rᴇᴘᴏʀᴛ Tᴏ ** : @abidabdullah199")
    
        
    file_path = f"downloads/{new_filename}"
    file = update.message.reply_to_message

    ms = await update.message.edit("Rᴏʙɪɴ ɪs Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ Fɪʟᴇ")    
    try:
     	path = await bot.download_media(message=file, file_name=file_path, progress=progress_for_pyrogram,progress_args=("Rᴏʙɪɴ Sᴛᴀʀᴛᴇᴅ Dᴏᴡɴʟᴏᴀᴅɪɴɢ", ms, time.time()))                    
    except Exception as e:
     	return await ms.edit(e)
     	     
    duration = 0
    try:
        metadata = extractMetadata(createParser(file_path))
        if metadata.has("duration"):
           duration = metadata.get('duration').seconds
    except:
        pass
    ph_path = None
    user_id = int(update.message.chat.id) 
    media = getattr(file, file.media.value)
    c_caption = await AshutoshGoswami24.get_caption(update.message.chat.id)
    c_thumb = await AshutoshGoswami24.get_thumbnail(update.message.chat.id)

    if c_caption:
         try:
             caption = c_caption.format(filename=new_filename, filesize=humanbytes(media.file_size), duration=convert(duration))
         except Exception as e:
             return await ms.edit(text=f"ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ ᴇʀʀᴏʀ ᴇxᴄᴇᴘᴛ ᴋᴇʏᴡᴏʀᴅ ᴀʀɢᴜᴍᴇɴᴛ: ({e})")             
    else:
         caption = f"**{new_filename}**"
 
    if (media.thumbs or c_thumb):
         if c_thumb:
             ph_path = await bot.download_media(c_thumb) 
         else:
             ph_path = await bot.download_media(media.thumbs[0].file_id)
         Image.open(ph_path).convert("RGB").save(ph_path)
         img = Image.open(ph_path)
         img.resize((320, 320))
         img.save(ph_path, "JPEG")

    await ms.edit("𝗣𝗮𝗻𝗱𝗮𝗪𝗲𝗽 𝗧𝗿𝘆𝗶𝗻𝗴 𝗧𝗼 𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴")
    type = update.data.split("_")[1]
    try:
        if type == "document":
            await bot.send_document(
                update.message.chat.id,
                document=file_path,
                thumb=ph_path, 
                caption=caption, 
                progress=progress_for_pyrogram,
                progress_args=("Rᴏʙɪɴ Sᴛᴀʀᴛᴇᴅ Uᴘʟᴏᴀᴅɪɴɢ Fɪʟᴇs", ms, time.time()))
        elif type == "video": 
            await bot.send_video(
		update.message.chat.id,
	        video=file_path,
	        caption=caption,
		thumb=ph_path,
		duration=duration,
	        progress=progress_for_pyrogram,
		progress_args=("Uᴘʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ ", ms, time.time()))
        elif type == "audio": 
            await bot.send_audio(
		update.message.chat.id,
		audio=file_path,
		caption=caption,
		thumb=ph_path,
		duration=duration,
	        progress=progress_for_pyrogram,
	        progress_args=("Uᴘʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ", ms, time.time()))
    except Exception as e:          
        os.remove(file_path)
        if ph_path:
            os.remove(ph_path)
        return await ms.edit(f" Error {e}")
 
    await ms.delete() 
    os.remove(file_path) 
    if ph_path: os.remove(ph_path) 







#ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
#ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot
