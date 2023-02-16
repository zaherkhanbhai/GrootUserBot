import asyncio
from pyrogram import Client, filters 
from pyrogram.types import Message
from GrootNetwork.modules.helpers.basics import edit_or_reply
from GrootNetwork.modules.helpers.filters import command
from GrootNetwork.modules.helpers.command import commandpro
from GrootNetwork.utilities.misc import SUDOERS


@Client.on_message(command(["addall", "kidnapall"]) & SUDOERS)
async def inviteall(client: Client, message: Message):
    Groot = await edit_or_reply(message, "Processing ...")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    await Groot.edit_text(f"**🌱 Iɴᴠɪᴛɪɴɢ Usᴇʀs Fʀᴏᴍ {chat.username} 😌 ...**")
    async for member in client.iter_chat_members(chat.id):
        user= member.user
        Groot= ["online", "offline" , "recently", "within_week"]
        if user.status in Groot:
           try:
            await client.add_chat_members(tgchat.id, user.id)
           except Exception as e:
            mg= await client.send_message("me", f"error-   {e}")
            await asyncio.sleep(0.3)
            await mg.delete()



__MODULE__ = "☆ ᴀᴅᴅ ᴀʟʟ ☆"
__HELP__ = f"""
`.kidnapall [@groupusername]` **- Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Aᴅᴅ Mᴇᴍʙᴇʀs Iɴ Yᴏᴜʀ Cʜᴀᴛ**

**Ex:-** `.kidnapall @RJbr0`
"""
