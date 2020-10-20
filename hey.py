# creator: @HELLBOY_OP
# Take credits if u gonna kang this LOL u noobs
# pic is inserted by @NOOB_GUY_OP
# Kangers stay away
from userbot.utils import admin_cmd, edit_or_reply
import asyncio


@borg.on(admin_cmd(pattern="hey (.*)", outgoing=True))
async def _(event):
    name = event.pattern_match.group(1)
    HEll = await edit_or_reply(event, "Hey")
    await asyncio.sleep(1)
    await HEll.edit("H")
    await asyncio.sleep(1)
    await HEll.edit("E")
    await asyncio.sleep(1)
    await HEll.edit("Y")
    msg = f"HEY {name}"
    if name is None:
        await HEll.client.send_message(event.chat_id, "HEY", file="http://telegra.ph/file/49156add028cb998291a8.jpg")
    elif name is not None:
        await HEll.client.send_message(event.chat_id, msg, file="http://telegra.ph/file/49156add028cb998291a8.jpg")
