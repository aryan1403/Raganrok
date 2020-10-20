"""Emoji

Available Commands:

.wtf"""
#Creator:@HELLBOY_OP 
#Kangers stay away!
from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern="wtf (.*)", outgoing=True))
async def _(event):
    name = event.pattern_match.group(1)
    HEll = await edit_or_reply(event, "wtf")
    await asyncio.sleep(1)
    await HEll.edit("What ")
    await asyncio.sleep(1)
    await HEll.edit("The F")
    await asyncio.sleep(1)
    await HEll.edit("What the f ")
    msg = f"WTF {name}"
    if name is None:
        await HEll.client.send_message(event.chat_id, "Wtf", file="https://telegra.ph/file/75a42ef6c5d04719ff494.png")
    elif name is not None:
        await HEll.client.send_message(event.chat_id, msg, file="https://telegra.ph/file/75a42ef6c5d04719ff494.png")
