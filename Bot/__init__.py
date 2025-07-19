from pyrogram import *
from config import Config 
import google.generativeai as genai



genai.configure(api_key=Config.GEMINI_API_KEY)
ai = genai.GenerativeModel("gemini-1.5-flash")


bot = Client("Bot",
              api_hash=Config.API_HASH,
              api_id=Config.API_ID,
              bot_token=Config.BOT_TOKEN)

