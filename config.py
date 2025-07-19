import os
from dotenv import load_dotenv

load_dotenv(".env")
class Config:
    BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = str(os.environ.get("API_HASH"))
    SOURCE_CHANNEL = int(os.environ.get("SOURCE_CHANNEL"))
    # DESTINATION_CHANNEL = int(os.environ.get("DESTINATION_CHANNEL"))
    LANGUAGE_CODE = str(os.environ.get("LANGUAGE_CODE", "si"))
    GEMINI_API_KEY = str(os.environ.get("GEMINI_API_KEY"))