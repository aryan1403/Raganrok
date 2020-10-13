"""Emoji
Available Commands:
.server"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern=r"server"))
async def _(event):
    if event.fwd_from:
        return

    animation_interval = 1

    animation_ttl = range(0, 19)

    # input_str = event.pattern_match.group(1)

    # if input_str == "mtn":

    await event.edit("Connecting to the server 404....")

    animation_chars = [

        "`Checking server details....`",
        "`█ ▇ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▇ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
        "*Server get hacked...*",
        "`▁ ▒ ▒ ▒ ▒ `",
        "`▁ ▂ ▒ ▒ ▒ `",
        "`▁ ▂ ▄ ▒ ▒ `",
        "`▁ ▂ ▄ ▅ ▆ `",
        "**Connected to the server....**",
        "`▒ ▒ ▒`",
        "`▁ ▒ ▒ `",
        "`▁ ▂ ▒ `",
        "`▁ ▂ ▄ `",
        "**Congo! now we have the full access of the server....**"
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 19])
