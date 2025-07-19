from Bot import bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import Config   
from. import *


@bot.on_message(filters.incoming & filters.chat(Config.SOURCE_CHANNEL))
async def translate(client, message: Message):
    if message.automatic_forward:
        try:
            text =   message.caption.html if message.caption else message.text.html
        except:
            text = None
        print(text)
        if not text:
            return
        translated_text = translate_text(text, lang_code=Config.LANGUAGE_CODE)
        if not translated_text:
            return await bot.send_message("Translation failed or no text to translate.")
        else:
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton(message.sender_chat.title, callback_data="none")],
                [InlineKeyboardButton("𝗖𝘆𝗯𝗲𝗿𝗹𝗶𝗻𝗲 🇱🇰", url="t.me/Cyberline_official")],
            ])
            await message.reply_text(
                translated_text,
                reply_markup=reply_markup,
                disable_web_page_preview=True
            )