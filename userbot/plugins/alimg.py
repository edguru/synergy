

import asyncio
import random
import re
import time
from userbot import ALIVE_NAME

from collections import deque

import requests

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from cowpy import cow

from userbot import CMD_HELP,YOUTUBE_API_KEY
from userbot.utils import register,admin_cmd

# ================= CONSTANT =================
IMAGE_PACK = [
    "https://telegra.ph/file/b2c76ef1d0a772cba9443.jpg",
    "https://telegra.ph/file/62f0d475ab6cfa7136d01.jpg",
    "https://telegra.ph/file/bd32c699e7f3d45d159ca.jpg",
    "https://telegra.ph/file/4b5eeae024918d1ef1e71.jpg",
    "https://telegra.ph/file/dc254dfc4fabc3223bb36.jpg",
    "https://telegra.ph/file/1ab92cc6f82851b0a7106.jpg",
    "https://telegra.ph/file/e8437f5d755735e66dc88.jpg",
    "https://telegra.ph/file/6015c38ff8ac04b0852e1.jpg",
    "https://telegra.ph/file/79b85e6fe298fbd4b9aba.jpg",
    "https://telegra.ph/file/3cfc5220a29d0cfda889b.jpg",
    "https://telegra.ph/file/bfaad699de64bb30cde81.jpg",
    "https://telegra.ph/file/e89d4e34f6a458766f51d.jpg",
]
POTO = random.choice(IMAGE_PACK)
@borg.on(admin_cmd(pattern=r"alimg"))
async def amireallyaliveimg(alimg):
    chat = await alimg.get_chat()
    await alimg.delete()
    """ For .alimg command, check if the bot is alive.  """
    await borg.send_file(alimg.chat_id, POTO,caption="**LOVE YOU SYNERGY**")
    await alimg.delete()