from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import Config
from helper.database import AshutoshGoswami24

async def not_subscribed(_, client, message):
    await AshutoshGoswami24.add_user(client, message)
    if not Config.FORCE_SUB:
        return False
    try:             
        user = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id) 
        if user.status == enums.ChatMemberStatus.BANNED:
            return True 
        else:
            return False                
    except UserNotParticipant:
        pass
    return True


@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    buttons = [[InlineKeyboardButton(text="○ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴀʟ ○", url=f"https://t.me/{Config.FORCE_SUB}") ]]
    text = "<b>Hᴇʟʟᴏ Usᴇʀs \n\nIғ Yᴏᴜ Wᴀɴᴛ Tᴏ Usᴇ Mᴇ Tʜᴇɴ Jᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴀʟ Nᴏᴡ</b>"
    try:
        user = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id)    
        if user.status == enums.ChatMemberStatus.BANNED:                                   
            return await client.send_message(message.from_user.id, text="Sᴏʀʀʏ Yᴏᴜ Aʀᴇ Bᴀɴɴᴇᴅ Fʀᴏᴍ Usᴇɪɴɢ Mᴇ Cᴏɴᴛᴀᴄᴛ Oᴡɴᴇʀ")  
    except UserNotParticipant:                       
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          



# PandaWep
# Don't Remove Credit 🥺
# Telegram Channel @PandaWep
# Developer https://github.com/PandaWep
