import re
from os import getenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","27655384"))
API_HASH = getenv("API_HASH","a6a418b023a146e99af9ae1afd571cf4")
BOT_TOKEN = getenv("BOT_TOKEN","")
