"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio
from userbot.utils import admin_cmd




@borg.on(admin_cmd(pattern=r"call"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

   # input_str = event.pattern_match.group(1)

   # if input_str == "call":

    await event.edit("Calling")

    animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: Yo this is` [RaganorkBot User](t.me/Raganork_Official) ,`Please Connect me to my master, 𝙃𝙚𝙡𝙡𝙗𝙤𝙮 🇽‌̸̵𝖃 𝕱𝖎𝖌𝖍𝖙𝖊𝖗🇽‌̸̵ 𝖃₱ⱤØ₲Ɽ₳₥₥ɆⱤ?🇭‌🇦‌🇨‌🇰‌🇪‌🇷`",
            "`User Authorised.`",
            "`Calling`  `At +916969696969`",
            "`Private  Call Connected...`",
            "`Me: Hello Sir, Please Ban This Telegram Account.`",    
            "`HellBoy: May I Know Who Is This?`",
            "`Me: Yo Brah, itz me RaganorkBot`  ",
            "`HellBoy: ohh!! After a long time....., Wassup Brother...\nI'll Make Sure That Guy Account Will be Blocked Within 24Hrs.`",
            "`Me: Thanks, See You Later Brah.`",
            "`HellBoy: Please Don't Thank Brah`",
            "`Me: Sure Sur \nTC Bye Bye :)`",
            "`Private Call Disconnected`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 18])
