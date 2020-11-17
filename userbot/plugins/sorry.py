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

SORRY_STRING = [
        "'I overlooked your happiness in an attempt to make myself happy, only to realize that my happiness lies in yours. I am sorry, please forgive me.'",
        "'Never forget the nine most important words of any family: I love you. You are beautiful. Please forgive me.'",
        "'An apology is a good way to have the last word.'",
        "'Forgiveness does not change the past, but it does enlarge the future.'",
        "'How do I say the words, ‘I’m sorry’ when I know that words are not enough? And how can I ask you to forgive me when I know I can’t forgive myself?'",
        "'I don’t know why, I made you cry I’m sorry sweetheart and yet Though you shouldn’t be lenient with me I hope you’ll forgive and forget'",
        "'It is never too late to make things right.'",
        "'Oh I’m sorry for blaming you For everything I just couldn’t do And I’ve hurt myself from hurting you'",
        "'The homepage of our relationship cannot be currently displayed because of a server error. Can we please click on the refresh button and start over again? I am sorry.'",
        "'With a bruised heart and a deflated ego, with sad soul and a head hung low. I apologize to you unconditionally.'",
        "'I have more issues then I could possibly count. And on my worse days, I’ll go from happy to sad in seconds. I won’t always like myself, and sometimes I’ll even assume you don’t like me either. I’ll push you away and I might even drive you insane. But I promise you this, nobody could ever even think about loving you as much as I do.'",
        ]
@register(outgoing=True, pattern="^.sry$")
async def insult(e):
    """ I make you cry !! """
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(random.choice(SORRY_STRING))