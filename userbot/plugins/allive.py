import os
import requests
import time
from PIL import Image
from io import BytesIO
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
from datetime import datetime

ALIVE_PHOTTO = os.environ.get("ALIVE_PHHOTO" , None)

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "This user"

@borg.on(admin_cmd(outgoing=True, pattern="allive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    if ALIVE_PHOTTO:
        pm_caption = "**Synergy 匣嘯 ��酒氤ｽ����1､7**\n"
        pm_caption += f"**符分 隼腹弗弗**            : {DEFAULTUSER}\n"
        pm_caption += "噬匐匳匐噬匚卆區 嚆匐噤嘯匣卆區        : 15.0\n"
        pm_caption += "卅嚠噬匚卆區 嚆匐噤嘯匣卆區          : 3.8.5\n"
        pm_caption += "嘯噪卅卅卆噤噬 甸匚匆區區匐匳         : [盒眼ｴ硝ｪﾉｴ](https://t.me/synergyOT)\n"
        pm_caption += "嘯噪卅卅卆噤噬 匕噤卆噪卅           : [盒眼ｴ硝ｪﾉｴ](https://t.me/synergyOT)\n"
        pm_caption += "仞刳刹剩剄刋凾刄剌 仗剩            : [ @The_Lone_Boy121 ](https://t.me/gym2105)\n"
        pm_caption += "笏鞘箔笏≫拍笏凪煤笏≫煤笏≫拍笏凪煤笏鞘箔\n 笏�買笏≫買笏�煤笏≫煤笏≫買笏�煤笏�買\n笏�迫笏≫縛笏�拍笏≫煤笏凪買笏�煤笏�買\n笏�迫笏≫縛笏�拍笏≫煤笏凪買笏�煤笏�買\n笏�買笏≫買笏�買笏�煤笏ｫ笏�迫笏凪買笏冷箔\n笏冷縛笏≫迫笏帚迫笏≫煤笏帚迫笏≫縛笏冷煤笏1､7"
        chat = await alive.get_chat()
        await alive.delete()
        """ For .allive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALIVE_PIC,caption=pm_caption, link_preview = False)
        await allive.delete()
        return
    req = requests.get("https://telegra.ph/file/d7cbffcb6bae55874b1c2.jpg")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(alive.chat_id, file=sticker)
        await borg.send_message(alive.chat_id,"**Synergy 匣嘯 ��酒氤ｽ����1､7**\n"
                      f"**符分 隼腹弗弗**            : {DEFAULTUSER}\n"
                      "噬匐匳匐噬匚卆區 嚆匐噤嘯匣卆區        : 15.0\n"
                      "卅嚠噬匚卆區 嚆匐噤嘯匣卆區          : 3.8.5\n"
                      "嘯噪卅卅卆噤噬 甸匚匆區區匐匳         : [盒眼ｴ硝ｪﾉｴ](https://t.me/synergyOT)\n"
                      "嘯噪卅卅卆噤噬 匕噤卆噪卅           : [盒眼ｴ硝ｪﾉｴ](https://t.me/synergyOT)\n"
                      "仞刳刹剩剄刋凾刄剌 仗剩           : [ @The_Lone_boy121 ](https://t.me/gym2105)\n"
                                "笏鞘箔笏≫拍笏凪煤笏≫煤笏≫拍笏凪煤笏鞘箔\n 笏�買笏≫買笏�煤笏≫煤笏≫買笏�煤笏�買\n 笏�迫笏≫縛笏�拍笏≫煤笏凪買笏�煤笏�買\n 笏�拍笏≫箔笏�買笏鞘箔笏�買笏�煤笏�買笏1､7 \n 笏�買笏≫買笏�買笏�煤笏ｫ笏�迫笏凪買笏冷売1､7 \n 笏冷縛笏≫迫笏帚迫笏≫煤笏帚迫笏≫縛笏冷煤笏1､7" , link_preview = False) 
        await alive.delete()
