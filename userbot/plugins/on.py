import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Raganork User"
PM_IMG = "https://telegra.ph/file/0e00f9e103c4a21ed35a5.jpg"
pm_caption = "🔥🔥**Ɽǟɢǟռօʀӄɮð† IS ON🔥🔥\n\n"

pm_caption += f"⚔️⚔️**му ℓσя∂**⚔️⚔️   : {DEFAULTUSER}\n"

pm_caption += "⚡️⚡️**тєℓєтнσи**⚡️⚡️   : 1.15.0 \n"

pm_caption += "⚡️⚡️**Os[Linux]**⚡️⚡️   : ʟɪɴᴜx ᴍᴀɴᴅʀɪᴠᴀ \n"

pm_caption += "😈😈**Ɽǟɢǟռօʀӄɮð†**😈😈   : 2.0\n"

pm_caption += "✨✨**¢нαииєℓ**✨✨   : [ᴊᴏɪɴ](https://t.me/Raganork_Official)\n"

pm_caption += "⚜️⚜️**gяσυρ**⚜️⚜️   : [ᴊᴏɪɴ](https://t.me/Raganork_bot_chat)\n"

pm_caption += "💫💫**ᴄᴜʀʀᴇɴᴛ ᴅɪʀᴇᴄᴛᴏʀʏ**💫💫   : ᴋᴀʟɪ_ᴘᴀʀʀᴏᴛ_ᴛᴇʀᴍɪɴᴀʟ\n"

pm_caption += "🔥🔥**ᴅᴇᴠᴇʟᴏᴘᴇʀ 🔥🔥   : [Raganork-Owner](https://t.me/HELLBOY_OP)\n"


pm_caption += " [...▄███▄███▄\n....█████████\n.......▀█████▀\n............▀█▀\n](https://t.me/HELLBOY_OP)\n"
@borg.on(admin_cmd(pattern=r"on"))
async def amireallyalive(lol):
    chat = await lol.get_chat()
    await lol.delete()
    """ For .on command, check if the bot is running.  """
    await borg.send_file(lol.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
