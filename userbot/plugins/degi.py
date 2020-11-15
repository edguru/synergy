"""Fun pligon...for @PepeB0t
\nCode by @kirito6969 , ©[Eyepatch](https://t.me/NeoMatrix90)
type `.degi` and `.nahi` to see the fun.
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="degi ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("wo")
        await asyncio.sleep(0.7)
        await event.edit("zarur")
        await asyncio.sleep(1)
        await event.edit("degi")
        await asyncio.sleep(0.8)
        await event.edit("ekbar")
        await asyncio.sleep(0.9)
        await event.edit("maang")
        await asyncio.sleep(1)
        await event.edit("ker")
        await asyncio.sleep(0.8)
        await event.edit("to")
        await asyncio.sleep(0.7)
        await event.edit("dekho")
        await asyncio.sleep(1)
        await event.edit("`wo zaru degi ekbar mang ker to dekho`")

@borg.on(events.NewMessage(pattern=r"\.nahi", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`wo zarur degi ekbar mang ker to dekho`")
    await asyncio.sleep(999)
