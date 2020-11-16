
"""Check if userbot awake or not . 

"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PIC = Config.ALIVE_PHOTTO
if ALIVE_PIC is None:
   ALIVE_PIC = ""


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = Config.ALIVE_MSG
if ALIVE_MESSAGE is None:

   ALIVE_MESSAGE = "**THE DEVIL HAS BEEN AWAKEN BY**"

   ALIVE_MESSAGE += f"**M̴y̴ ̴̴̴̴̴̴̴̴̴̴̴̴̴̴̴̴MA⃨s̤̈T̰̃E̫尺**            : {DEFAULTUSER}\n"


   ALIVE_MESSAGE += "ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ        :  15.0.0 \n"


   ALIVE_MESSAGE += "MAGIC CHANNEL          : [ᴊᴏɪɴ](https://t.me/SynergysupportOfficial)\n"


   ALIVE_MESSAGE += "DARKEST GROUP        : [ᴊᴏɪɴ](https://t.me/synergyOT)\n"


   ALIVE_MESSAGE += "ʟɪᴄᴇɴꜱᴇ                 : [ᴍɪᴛ ʟɪᴄᴇɴꜱᴇ](https://github.com/edguru/synergy/blob/master/LICENSE)\n"


   ALIVE_MESSAGE += "ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ            : [gym2105](https://t.me/Gym2105)\n"


   ALIVE_MESSAGE += "Wooshhh💨💨💨 /n Looks like my master {DEFAULTUSER} HAS SUMMONED ME. /n It's time for me to perform my duties . /n hey those who go against my master's will fear my eye of thousand years of death👁️. And those in the good book thanks for being with my master . You Are a true friend🤝"


   ALIVE_MESSAGE +=" [synergy](https://t.me/synergyOT)"
                
            
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete() 
    await borg.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)
