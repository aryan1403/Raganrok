#BY SIPAKISKING
#BY @NOOB_GUY_OP actually thought for Dark Cobra


import asyncio



import random



from telethon import events



from userbot.utils import admin_cmd



from userbot import ALIVE_NAME



from telethon.tl.types import ChannelParticipantsAdmins



DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Raganork user"



ani_interval = 1



#Social_distancing



file1 = "http://telegra.ph/file/efadde4adf9674be0ea38.jpg"


file2 = "http://telegra.ph/file/353837fb6dad1a7aa44c0.jpg"


file3 = "http://telegra.ph/file/fbf8619abb11516420145.jpg"


file4 = "http://telegra.ph/file/e0df8ad07c2586b61bad7.jpg"






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
    
    """ For .on command, check if I am on(alive) fire or not.  """
    aluve = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(ani_interval)
    ok = await borg.edit_message(yes.chat_id, aluve, file=file2) 

    await asyncio.sleep(ani_interval)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(ani_interval)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(ani_interval)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(ani_interval)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(ani_interval)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(ani_interval)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)
    await yes.delete()
