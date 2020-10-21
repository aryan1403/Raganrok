import os
import time
import asyncio
import io
from userbot.uniborgConfig import Config
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, errors, functions, types
from userbot import ALIVE_NAME, CUSTOM_PMPERMIT
from userbot.utils import admin_cmd
from userbot import CMD_HELP

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
  WARN_PIC = "https://telegra.ph/file/db92ed3d77377856ef911.mp4"
else:
  WARN_PIC = PMPERMIT_PIC

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}


PM_ON_OFF = Config.PM_DATA


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
CUSTOM_MIDDLE_PMP = str(CUSTOM_PMPERMIT) if CUSTOM_PMPERMIT else "**ᴡʜᴏ ᴀʀᴇ ʏᴏᴜ ᴡʜᴏ ᴀʟʟᴏᴡᴇᴅ ʏᴏᴜ ᴛᴏ ᴘᴍ ᴍʏ ᴍᴀsᴛᴇʀ** \n`ᴍʏ ᴍᴀsᴛᴇʀ ᴡɪʟʟ ᴅᴇᴄɪᴅᴇ ᴡʜᴀᴛ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ʏᴏᴜ ᴛɪʟʟ ᴛʜᴇɴ ᴡᴀɪᴛ`"
USER_BOT_WARN_ZERO = "`ʏᴏᴜ ᴅɪᴅ'ɴᴛ sᴇᴇ ᴡʜᴀᴛ ɪ sᴀɪᴅ ᴍʏ ᴍᴀsᴛᴇʀ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴏғғʟɪɴᴇ ᴅᴏɴᴛ sᴘᴀᴍ.`\n**ɴᴏᴡ sʜᴜᴛ ᴜᴘ.... ᴀɴᴅ ɢᴇᴛ ʟᴏsᴛ**"
USER_BOT_NO_WARN = ("`ʜᴇʏ, ɪ ᴀᴍ ʀᴀɢᴀɴᴏʀᴋ😈.sᴏʀʀʏ ʙᴜᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴀʀʀɪᴠᴇᴅ ᴀ ᴡʀᴏɴɢ ᴡᴀʏ,`"
                   f"{DEFAULTUSER}'s `sᴏʀʀʏ, ɪ ᴅᴏɴᴛ ᴋɴᴏᴡ ʜᴏᴡ ᴘᴇᴏᴘʟᴇ ᴀʀᴇ sᴏ ғʀᴇᴇ ᴛʜᴀᴛ ᴛʜᴇʏ ɢᴇᴛ ᴛʜᴇ ᴛɪᴍᴇ ᴛᴏ ᴅᴏ ᴜsᴇʟᴇss ᴄʜᴀᴛs sᴇᴇ ᴍʏ ᴍᴀsᴛᴇʀ's ɪɴʙᴏx ɪᴛ ɪs ғɪʟʟᴇᴅ ᴡɪᴛʜ ɪᴍᴘᴏʀᴛᴀɴᴛ ᴍᴀɪʟs ɢᴏ ᴀɴᴅ ᴅᴏ ʏᴏᴜʀ ᴡᴏʀᴋ ᴅᴏɴ'ᴛ ᴅɪsᴛᴜʀʙ ᴍʏ ᴍᴀsᴛᴇʀ...\n"
                    "ɪғ ɪᴛ ɪs ᴜʀɢᴇɴᴛ ʟᴇᴀᴠᴇ ʏᴏᴜʀ ᴄʜᴀᴛ ɪᴅ ,ᴅᴇsᴄɪᴘᴛɪᴏɴ ᴀɴᴅ ʀᴇᴀsᴏɴ...ᴀɴᴅ ɪ ʜᴏᴘᴇ ɪғ ʏᴏᴜ ᴀʀᴇ ᴀ ɢᴏᴏᴅ ᴘᴇʀsᴏɴ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴀ ʀᴇᴘʟʏ ʙᴜᴛ ɪ ᴀᴍ ɴᴏᴛ sᴜʀᴇ ᴀʙᴏᴜᴛ ᴛʜᴀᴛ`⭕️\n\n"
                  

    @borg.on(admin_cmd(pattern="approve ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
           return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if chat.id in PM_WARNS:
                    del PM_WARNS[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]
                pmpermit_sql.approve(chat.id, reason)
                await event.edit("Approved to pm [{}](tg://user?id={})".format(firstname, chat.id))
                await asyncio.sleep(3)
                await event.delete()

    @bot.on(events.NewMessage(outgoing=True))
    async def you_dm_niqq(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if not chat.id in PM_WARNS:
                    pmpermit_sql.approve(chat.id, "outgoing")
                    bruh = "__Added user to approved pms cuz outgoing message >~<__"
                    rko = await borg.send_message(event.chat_id, bruh)
                    await asyncio.sleep(3)
                    await rko.delete()


    @command(pattern="^.block ?(.*)")
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
          if chat.id == -438670332:
            await event.edit("ʜᴇʏ, ʏᴏᴜ ɴᴏᴏʙ ʏᴏᴜ  ᴀʀᴇ ᴛʀʏɪɴɢ ᴛᴏ ʙʟᴏᴄᴋ ᴍʏ ᴄʀᴇᴀᴛᴏʀ😡 , sᴇɴᴅɪɴɢ ʏᴏᴜʀ ʀᴇᴘᴏʀᴛ ᴛᴏ ᴍʏ ᴄʀᴇᴀᴛᴏʀ @ʜᴇʟʟʙᴏʏ_ᴏᴘ ʏᴏᴜ ᴀʀᴇ ᴅɪsᴀʙʟᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ ғᴏʀ 𝟼𝟶𝟶 sᴇᴄᴏɴᴅs 😴 ᴅᴏɴ'ᴛ ᴅᴏ ᴛʜᴀᴛ ᴀɢᴀɪɴ ᴏʀ ᴇʟsᴇ ʏᴏᴜ ᴡɪʟʟ ʙᴇ ʙᴀɴ ғᴏʀ ᴜsɪɴɢ ᴍᴇ! ᴀsᴋ ᴍʏ ᴄʀᴇᴀᴛᴏʀ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ @ʜᴇʟʟʙᴏʏ_ᴏᴘ ")
            await asyncio.sleep(600)
          else:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit("ᴛᴜ..😒 ɴɪᴋᴀʟ ᴘᴇʜʟɪ ғᴜʀsᴀᴛ ᴍᴇ ʏᴏᴜ ᴀʀᴇ ʙʟᴏᴄᴋᴇᴅ ɴᴏᴡ..😠 !!**[{}](tg://user?id={})".format(firstname, chat.id))
                await asyncio.sleep(3)
                await event.client(functions.contacts.BlockRequest(chat.id))

    @command(pattern="^.disapprove ?(.*)")
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
          if chat.id == -438670332:
            await event.edit("ᴡʜᴀᴛ ᴀʀᴇ ʏᴏᴜ ᴅᴏɪɴɢ ʏᴏᴜ ᴋɴᴏᴡ ᴛʜɪs ᴘᴇʀsᴏɴ ʜᴇ ɪs ᴍʏ ᴄʀᴇᴀᴛᴏʀ ɪ ᴄᴀɴ'ᴛ ᴅɪsᴀᴘᴘʀᴏᴠᴇ ᴍʏ ᴄʀᴇᴀᴛᴏʀ")
            await asyncio.sleep(5)
            await event.edit("sᴏ, ʏᴏᴜ ᴀʀᴇ ʀᴇsᴛʀɪᴄᴛᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ ғᴏʀ 𝟷𝟶𝟶 sᴇᴄᴏɴᴅs sᴀʏ sᴏʀʀʏ ᴛᴏ ᴍʏ ᴄʀᴇᴀᴛᴏʀ ᴀɴᴅ ʜᴇɴᴄᴇ ᴜ ᴡɪʟʟ ʙᴇ ʀᴇʟᴇᴀsᴇᴅ")
            await asyncio.sleep(100)
          else:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit("Disapproved [{}](tg://user?id={})".format(firstname, chat.id))
                
    

    @command(pattern="^.listapproved")
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Current Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
        else:
            APPROVED_PMs = "no Approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)


    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if event.from_id == bot.uid:
            return

        if Var.PRIVATE_GROUP_ID is None:
            return

        if not event.is_private:
            return

        message_text = event.message.message
        chat_id = event.from_id

        current_message_text = message_text.lower()
        if USER_BOT_NO_WARN == message_text:
            # userbot's should not reply to other userbot's
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        sender = await bot.get_entity(chat_id)

        if chat_id == bot.uid:

            # don't log Saved Messages

            return

        if sender.bot:

            # don't log bots

            return

        if sender.verified:

            # don't log verified accounts

            return
          
        if PM_ON_OFF == "DISABLE":
            return

        if not pmpermit_sql.is_approved(chat_id):
            # pm permit
            await do_pm_permit_action(chat_id, event)



    async def do_pm_permit_action(chat_id, event):
        if chat_id not in PM_WARNS:
            PM_WARNS.update({chat_id: 0})
        if PM_WARNS[chat_id] == 5:
            r = await event.reply(USER_BOT_WARN_ZERO)
            await asyncio.sleep(3)
            await event.client(functions.contacts.BlockRequest(chat_id))
            if chat_id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_id].delete()
            PREV_REPLY_MESSAGE[chat_id] = r
            the_message = ""
            the_message += "#BLOCKED_PMs\n\n"
            the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
            the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
            # the_message += f"Media: {message_media}"
            try:
                await event.client.send_message(
                    entity=Var.PRIVATE_GROUP_ID,
                    message=the_message,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True
                )
                return
            except:
                return
        r = await event.client.send_file(event.chat_id, WARN_PIC, caption=USER_BOT_NO_WARN)
        PM_WARNS[chat_id] += 1
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r

from userbot.utils import admin_cmd
import io
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon import events
@bot.on(events.NewMessage(incoming=True, from_users=(-438670332)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "**ᴍʏ ʙᴏss ɪs ʟᴇɢᴇɴᴅᴀʀʏ🔥**")
            await borg.send_message(chat, "**ᴍᴇᴇᴛ ʙʏ ʙᴏss @ʜᴇʟʟʙᴏʏ_ᴏᴘ ʜᴇ ᴄʀᴇᴀᴛᴇᴅ ᴍᴇ...... **")
            
            
            
CMD_HELP.update({
    "pmpermit":
    "\
.approve\
\nUsage: Approves the mentioned/replied person to PM.\
.disapprove\
\nUsage: dispproves the mentioned/replied person to PM.\
\n\n.block\
\nUsage: Blocks the person.\
\n\n.listapproved\
\nUsage: To list the all approved users.\
"
})
