import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
BOT_NAME = getenv("BOT_NAME", "") 
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "")
TAG_AD = getenv("TAG_AD", "")
