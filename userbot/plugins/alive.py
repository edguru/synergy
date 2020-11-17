import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from userbot.plugins.alimg import POTO
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "My Boss"
IMAGE_PAC = [

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



POTTO = random.choice(IMAGE_PAC)
PM_IMG = POTTO
pm_caption = "**Synergy ɪꜱ ON IT'S TOES**\n"

pm_caption += f"**M̴y̴ ̴̴̴̴̴̴̴̴̴̴̴̴̴̴̴̴MA⃨s̤̈T̰̃E̫尺**            : {DEFAULTUSER}\n"

pm_caption += "ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ        :  15.0.0 \n"

pm_caption += "ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ          : [ᴊᴏɪɴ](https://t.me/SynergysupportOfficial)\n"

pm_caption += "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ        : [ᴊᴏɪɴ](https://t.me/synergyOT)\n"

pm_caption += "ʟɪᴄᴇɴꜱᴇ                 : [ᴍɪᴛ ʟɪᴄᴇɴꜱᴇ](https://github.com/edguru/synergy/blob/master/LICENSE)\n"

pm_caption += "ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ            : [gym2105](https://t.me/Gym2105)\n"
pm_caption += f"I am the **DEVIL KNIGHT**. Sleeping for 100 of years finally I have been awaken by my [creator](https://t.me/Gym2105). \n **HE GAVE ME THE DUTY TO PROTECT MY MASTER** :{DEFAULTUSER}\n So beware of my wrath and my hidden hunger of thousand years of sleep"
pm_caption += " [synergy](https://t.me/synergyOT)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is alive.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
