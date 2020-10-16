import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Raganork User"
PM_IMG = "https://telegra.ph/file/0e00f9e103c4a21ed35a5.jpg"
pm_caption = "🔥 **Ɽǟɢǟռօʀӄɮð† Is Online**  ⁪⁬⁮⁮⁮⁮🔥\n"

pm_caption += f"⚡️ **ᎷᎽ ℓσя∂**       :   {DEFAULTUSER}⚡️\n"

pm_caption += "🔥 𝙎𝙮𝙨𝙩𝙚𝙢 𝙎𝙩𝙖𝙩𝙨 🔥\n"

pm_caption += "✨ Os                  :Kali Linux 😈😈\n"

pm_caption += "💫 тєℓєтнσи νєяѕισи    : 1.15.1 \n"

pm_caption += "💫 Ɽǟɢǟռօʀӄɮð† νєяѕισи : 2.0 \n"

pm_caption += "💫 ρунтσи              : 3.8.5\n"

pm_caption += "✨ σffι¢ιαℓ ¢нαииєℓ    : [ᴊᴏɪɴ](https://t.me/Raganork_Official)\n"

pm_caption += "✨ σffι¢ιαℓ gяσυρ      : [ᴊᴏɪɴ](https://t.me/Raganork_bot_chat)\n"

pm_caption += "✨ ℓι¢єиѕє             : [ӀíϲҽղՏҽ](https://github.com/HellBoy-Aaryan/Raganork/blob/master/LICENSE)\n"

pm_caption += "✨ ¢σρуяιgнт           : [Raganork-Owner](https://github.com/HellBoy-Aaryan)\n"

pm_caption += "🔥 Database Functionality:   All Set 👌 \n"

pm_caption += " [...▄███▄███▄\n....█████████\n.......▀█████▀\n............▀█▀\n](https://t.me/HELLBOY_OP)\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
