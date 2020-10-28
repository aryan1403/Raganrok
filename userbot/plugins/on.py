import asyncio



import random



from telethon import events



from userbot.utils import admin_cmd



from userbot import ALIVE_NAME



from telethon.tl.types import ChannelParticipantsAdmins



DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Raganork user"



#Social_distancing

s_random = random.SystemRandom

imgs = ["http://telegra.ph/file/a4ef33e7ce73ae9558330.jpg", "http://telegra.ph/file/fbf8619abb11516420145.jpg", "http://telegra.ph/file/efadde4adf9674be0ea38.jpg", "http://telegra.ph/file/353837fb6dad1a7aa44c0.jpg"]
    
    
    

    
PM_IMG = s_random.choice(imgs)




#Social_distancing



pm_caption = "This is **Raganork userbot !**\n\n"


pm_caption += f"✨Servant of my master \n  : {DEFAULTUSER} \n"


pm_caption += "✨**My Os**   ☞ ʟɪɴᴜx ᴍᴀɴᴅʀɪᴠᴀ  \n"


pm_caption += "**✨Mandriva Version**  : 1.07.3 \n"


pm_caption += "✨**Support Channel**   : [ᴊᴏɪɴ](https://t.me/Raganork_Official)\n"


pm_caption += "✨**Support group** : [ᴊᴏɪɴ](https://t.me/Raganork_bot_chat)\n"


pm_caption += "✨**Developer** :  [@HELLBOY_OP](https://t.me/Hellboy_Pikachu)  \n\n"




#Social_distancing




@borg.on(admin_cmd(pattern=r"on"))
async def amireallyalive(yes):
    chat = await yes.get_chat()
    await yes.delete()
    """ For .on command, check if I am on(alive) fire or not.  """
    await borg.send_file(yes.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
