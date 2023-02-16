# GrootNetwork
import asyncio
from pyrogram import *
from pyrogram.types import *
from GrootNetwork.modules.helpers.basics import edit_or_reply
from GrootNetwork.modules.helpers.filters import command
from GrootNetwork.utilities.misc import SUDOERS


@Client.on_message(command(["Groot"]) & SUDOERS)
async def lanja_puk(client: Client, message: Message):
    await edit_or_reply(message, "**🌱 I Aᴍ Aʟɪᴠᴇ Mʏ Dᴇᴀʀ Pɪʀᴏ Mᴀsᴛᴇʀ 🙂 ...**")



__MODULE__ = "☆ ᴀʟɪᴠᴇ ☆"
__HELP__ = f"""
**🌱 Tᴇsᴛ Yᴏᴜʀ Bᴏᴛ Wᴏʀᴋɪɴɢ Oʀ Nᴏᴛ.**

`.Groot` - **Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Cʜᴇᴄᴋ**
"""
