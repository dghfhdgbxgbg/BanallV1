import re
from os import getenv
from pyrogram import Client, filters
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","27655384"))
API_HASH = getenv("API_HASH","a6a418b023a146e99af9ae1afd571cf4")
BOT_TOKEN = getenv("BOT_TOKEN","7779804166:AAG-93Bw1D0hbuuwLf1LErxQPmBAa59Dhwg")
BANALL = list(map(int, getenv("BANALL", "7137269276 7045191057 7091230649").split()))
