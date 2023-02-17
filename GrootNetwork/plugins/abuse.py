import asyncio
from pyrogram import *
from pyrogram.types import *
from GrootNetwork.modules.helpers.basics import edit_or_reply
from GrootNetwork.modules.helpers.command import commandpro
from GrootNetwork.utilities.misc import SUDOERS


GALINAKODUKU = "𝗡𝗶 𝗽𝗲𝗹𝗹𝗮𝗺 𝗴𝘂𝗱𝗱𝗵𝗮𝗹𝗮 𝘀𝘂𝗹𝗹𝗶 𝗹𝗮𝗻𝗷𝗮𝗸𝗼𝗱𝗮𝗸𝗮, 𝘃𝗮𝗰𝗵𝗶 𝗻𝗮 𝘀𝘂𝗹𝗹𝗶 𝗰𝗵𝗶𝗸𝘂, 𝗸𝗼𝗷𝗷𝗮 𝗻𝗮 𝗸𝗼𝗱𝗮𝗸𝗮, 𝘀𝗶𝗴𝗴𝘂𝗹𝗲𝗻𝗶 𝘆𝗮𝗱𝗵𝗮𝘃𝗮, 𝗻𝗶 𝗮𝗸𝗸𝗮 𝗴𝘂𝗱𝗱𝗵𝗮𝗹𝗮 90𝗺𝗺 𝗿𝗼𝗱 𝗽𝗲𝘁𝘁𝗶 𝗱𝗲𝗻𝗴𝘂𝘁𝗵𝗮 , 𝗻𝗶 𝗽𝗲𝗹𝗹𝗮𝗺 𝗽𝘂𝗸𝘂𝗹𝗮 𝗺𝗼𝗱𝗱𝗮, 𝗻𝗶 𝗮𝗺𝗺𝗮 𝗻𝗶 𝗱𝗲𝗻𝗴𝗶𝘁𝗲 𝗽𝘂𝘁𝘆𝗮𝘃𝗿𝗮, 𝘃𝗲𝗹𝗹𝗶 𝗮𝗱𝘂𝗴𝘂 𝗻𝗶 𝗮𝗺𝗺𝗮 𝗻𝗶 𝗻𝗮 𝗺𝗼𝗱𝗱𝗮 𝗸𝗶 𝗽𝘂𝘁𝘆𝗮𝘃 𝗮𝗻𝗶 𝗰𝗵𝗲𝗽𝘁𝗵𝗮𝗱𝗶, 𝗸𝗼𝗷𝗷𝗮 𝗺𝘂𝗻𝗱𝗮 𝗸𝗼𝗱𝗮𝗸𝗮, 𝘃𝗮𝗰𝗵𝗶 𝗻𝗮𝗱𝗶 𝗻𝗶 𝗻𝗼𝘁𝗹𝗮 𝗽𝗲𝘁𝘁𝘂𝗸𝗼...𝗹𝗮𝗻𝗷𝗮 𝗽𝘂𝘁𝘁𝗶𝗻𝗼𝗱𝗮, 𝘀𝗶𝗴𝗴𝘂 𝗿𝗮𝗱𝗲𝗻𝘁𝗿𝗮 𝗻𝗶𝗸𝘂, 𝗻𝗶 𝗺𝗼𝗸𝗮𝗺 𝗹𝗼 𝗻𝗮 𝗮𝘁𝗵𝘂𝗹𝘂, 𝘀𝗶𝗴𝗴𝘂𝗹𝗲𝗻𝗶 𝘆𝗮𝗱𝗵𝗮𝘃𝗮 𝘁𝗵𝘂 𝗻𝗶 𝗯𝗮𝘁𝗵𝘂𝗸𝘂𝗹𝗮 𝗻𝗮 𝘀𝗮𝗻𝗮 𝗽𝗲𝘁𝘁𝗶𝗻𝗮 𝘀𝘂𝗹𝗹𝗶 ,𝗻𝗶 𝗽𝗲𝗹𝗹𝗮𝗻𝗶 ,𝗻𝗶 𝗮𝗸𝗸𝗮 𝗻𝗶 𝗼𝗸𝗲𝘆 𝘀𝗮𝗿𝗶 𝗱𝗲𝗻𝗴𝘂𝘁𝗵𝗮..𝗸𝗼𝗷𝗷𝗮 𝗻𝗮 𝗸𝗼𝗱𝗮𝗸𝗮!"



@Client.on_message(commandpro(["lanjapuk"]) & SUDOERS)
async def lanja_puk(client: Client, message: Message):
    Groot = await edit_or_reply(message, "🤣 Arey Thammudu Agara 😁 ...")
    await asyncio.sleep(2)
    await Groot.edit(GALINAKODUKU)
    
    
__MODULE__ = "☆ ᴀʙᴜsᴇ ☆"
__HELP__ = f"""
**🌱 Hᴇʏ Hᴇʀᴇ Is Aʟʟ Aʙᴜsᴇ 😒**

**Cᴏᴍᴍᴀɴᴅs:**

`lanjapuk` - **Rᴇᴘʟʏ Tᴏ Aɴʏ Usᴇʀ Tᴏ Gɪᴠᴇ Bᴀɴᴅᴀ Bᴏᴏᴛʜᴜʟᴜ**
"""
