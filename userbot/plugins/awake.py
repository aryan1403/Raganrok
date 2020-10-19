
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
   ALIVE_PIC = "https://telegra.ph/file/f34675b4e94d4290c0b6b.mp4"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

ALIVE_MESSAGE = Config.ALIVE_MSG
ALIVE_MESSAGE = "**🔱Ɽǟɢǟռօʀӄɮð† Zinda Tha....Zinda Hai....Aur Zinda Rahega🔱 \n\n\n**"
ALIVE_MESSAGE += "`My Bot Status \n\n\n`"
ALIVE_MESSAGE += f"`Telethon: TELETHON-15.0.9 \n\n`"
ALIVE_MESSAGE += f"`Python: PYTHON-3.8.6 \n\n`"
ALIVE_MESSAGE += "`My Master I Will Serve You Till My Dyno Ends!!☠ \n\n`"
ALIVE_MESSAGE += f"`Support Channel` : @Raganork_Official \n\n"
if ALIVE_MESSAGE is None:
   ALIVE_MESSAGE = "**🔱Ɽǟɢǟռօʀӄɮð† Zinda Tha....Zinda Hai....Aur Zinda Rahega🔱 \n\n\n**"
   ALIVE_MESSAGE += "`My Bot Status \n\n\n`"
   ALIVE_MESSAGE += f"`Telethon: TELETHON-16.0.1 \n\n`"
   ALIVE_MESSAGE += f"`Python: PYTHON-3.8.6 \n\n`"
   ALIVE_MESSAGE += "`Sir I Will Serve You Till My Dyno Ends!!☠ \n\n`"
   ALIVE_MESSAGE += f"`Support Channel` : @Raganork_Official \n\n"
   ALIVE_MESSAGE += f"`ᎷᎽ ᏰᏫᏕᏕ`: {DEFAULTUSER} \n\n "
                
            
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete() 
    await borg.send_file(awake.chat_id, ALIVE_PIC,caption=ALIVE_MESSAGE)
