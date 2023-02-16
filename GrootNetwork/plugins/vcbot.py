# 𝐆𝐫𝐨𝐨𝐭 𝐌𝐮𝐬𝐢𝐜 // @RJbr0

import os
import sys
import json
import time
import aiofiles
import aiohttp
import ffmpeg
import requests
from os import path
from asyncio.queues import QueueEmpty
from typing import Callable
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from GrootNetwork.modules.cache.admins import set
from GrootNetwork.modules.clientbot import clientbot, queues
from GrootNetwork.modules.clientbot.clientbot import client as USER
from GrootNetwork.modules.helpers.admins import get_administrators
from GrootNetwork.modules import converter
from GrootNetwork.modules.downloaders import youtube
from GrootNetwork.config import que
from GrootNetwork.modules.cache.admins import admins as a
from GrootNetwork.modules.helpers.command import commandpro
from GrootNetwork.modules.helpers.filters import command, other_filters
from GrootNetwork.modules.helpers.decorators import SUDO_USERS, errors, sudo_users_only
from GrootNetwork.modules.helpers.errors import DurationLimitError
from GrootNetwork.modules.helpers.gets import get_url, get_file_name
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.exceptions import GroupCallNotFound, NoActiveGroupCall
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
from yt_dlp.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)
from GrootNetwork.utilities.misc import SUDOERS
# plus
chat_id = None
useer = "NaN"


def transcode(filename):
    ffmpeg.input(filename).output(
        "input.raw", format="s16le", acodec="pcm_s16le", ac=2, ar="48k"
    ).overwrite_output().run()
    os.remove(filename)


# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))



@Client.on_message(
    commandpro([".play", "play"]) & SUDOERS)
async def play(_, message: Message):
    global que
    global useer
    await message.delete()
    lel = await message.reply("**😏 ప్రాసెసింగ్ ...**")

    administrators = await get_administrators(message.chat)
    chid = message.chat.id


    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://te.legra.ph/file/43eb81b7a99092f9a3197.jpg"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Locally added"


        requested_by = message.from_user.first_name
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

            
        except Exception as e:
            title = "NaN"
            thumb_name = "https://te.legra.ph/file/0a87707652242961c79f2.jpg"
            duration = "NaN"
            views = "NaN"

        requested_by = message.from_user.first_name
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
           return await lel.edit(
                "**😒 ఏం కావాలి రా నీకు \n😏 చెప్పరా ❓**"
            ) and await lel.delete()

        await lel.edit("**🔎 వెతుకుతున్న ఉండరా 😑 ...**")
        query = message.text.split(None, 1)[1]
        # print(query)
        await lel.edit("**😑 సర్ సర్ లే పో 😒 ...**")
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await lel.edit(
                "**😒 పాట దొరకడం లేదురా..❗️\n🤨 సరిగ్గా ప్లే చెయ్. 😡...**"
            ) and await lel.delete()
            print(str(e))
            return


        requested_by = message.from_user.first_name
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        await lel.edit("**😏 ఈ పాట అయిపోయాక నువ్వే..\n😊 వెనక ఉండు పో.. » `{}` 😒 ...**".format(position),
    )
    else:
        await clientbot.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )

        await lel.edit("**💃 𝐁𝐡𝐚𝐧𝐮𝐦𝐚𝐭𝐡𝐢 𝐌𝐮𝐬𝐢𝐜 𝐍𝐨𝐰 \n 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 𝐎𝐏 😌 ...**".format(),
        )

    return await lel.delete()
    
    
    
@Client.on_message(commandpro([".pause", "pause"]) & SUDOERS)
async def pause(_, message: Message):
    await message.delete()
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        noac = await message.reply_text("**😑 ప్లే అవ్వడం లేదు..😏...**")
        await noac.delete()
    else:
        await clientbot.pytgcalls.pause_stream(message.chat.id)
        pase = await message.reply_text("**😑 ఆగిపోయింది 🤨 ...**")
        await pase.delete()

@Client.on_message(commandpro([".resume", "resume"]) & SUDOERS)
async def resume(_, message: Message):
    await message.delete()
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        noac = await message.reply_text("**🤨 ప్లే అవ్వడం లేదు.. 😒 ...**")
        await noac.delete()
    else:
        await clientbot.pytgcalls.resume_stream(message.chat.id)
        rsum = await message.reply_text("**😏 పునఃప్రారంభించబడింది 😌 ...**")
        await rsum.delete()


@Client.on_message(commandpro([".skip", "skip"]) & SUDOERS)
async def skip(_, message: Message):
    global que
    await message.delete()
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
       novc = await message.reply_text("**😒 ప్లే అవ్వడం లేదు 😑...**")
       await novc.delete()
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            empt = await message.reply_text("**🌱 ఏం లేదు సదురు కోని పోవడమే..🤨 ...**")
            await empt.delete()
            await clientbot.pytgcalls.leave_group_call(chat_id)
        else:
            next = await message.reply_text("**😑 దాటవేశారు 🤨 ...**")
            await next.delete()
            await clientbot.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        clientbot.queues.get(chat_id)["file"],
                    ),
                ),
            )
             


@Client.on_message(commandpro([".stop", ".end", "end", "stop"]) & SUDOERS)
async def stop(_, message: Message):
    await message.delete()
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        noac = await message.reply_text("**🌱 ప్లే అవ్వడం లేదు 🤨 ...**")
        await noac.delete()
        return
    else:
        try:
            clientbot.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

    await clientbot.pytgcalls.leave_group_call(message.chat.id)
    leav = await message.reply_text("**❌ డేటా బొక్క రా మీకు 🤨 ...**")
    await leav.delete()


@Client.on_message(commandpro([".song", "song", ".song", ".music", "music"]) & SUDOERS)
async def song(client, message):
    cap = "**🌱యజమాని ː [ɪᴀᴍ ɢʀᴏᴏᴛ](https://t.me/mynameisgroot)**"
    rkp = await message.reply("**🔄 ప్రాసెసింగ్ ...**")
    
    if len(message.command) < 2:
            return await rkp.edit(
                "**🌱 పాట పేరు చెప్పు 🤨  ...**"
            )
    url = message.text.split(None, 1)[1]
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await rkp.edit("**🌱 పాట దొరకడం లేదు 😔 ...**")
    type = "audio"
    if type == "audio":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
        song = True
    try:
        await rkp.edit("**😑 డౌన్‌లోడ్ చేస్తోంది ...**")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await rkp.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await rkp.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await rkp.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await rkp.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await rkp.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await rkp.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await rkp.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await rkp.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await rkp.edit(f"{str(type(e)): {str(e)}}")
        return
    time.time()
    if song:
        await rkp.edit("**😌 అప్‌లోడ్ చేస్తోంది ...**")
        lol = "./AdityaHalder/resource/logo.jpg"
        lel = await message.reply_audio(
                 f"{rip_data['id']}.mp3",
                 duration=int(rip_data["duration"]),
                 title=str(rip_data["title"]),
                 performer=str(rip_data["uploader"]),
                 thumb=lol,
                 caption=cap) 
        await rkp.delete()


@Client.on_message(commandpro([".reload", "reload"]) & SUDOERS)
async def update_admin(client, message):
    global a
    await message.delete()
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    a[message.chat.id] = new_admins
    cach = await message.reply_text("**😌 రీలోడ్ చేయబడింది 😁 ...**")
    await cach.delete()


__MODULE__ = "☆ Vᴄ Bᴏᴛ ☆"
__HELP__ = f"""
**Yᴏᴜ Cᴀɴ Pʟᴀʏ Mᴜsɪᴄ Oɴ VC**

`.play` - Pʟᴀʏ Mᴜsɪᴄ Oɴ Vᴄ
`.pause` - Pᴀᴜsᴇ Yᴏᴜʀ Mᴜsɪᴄ
`.resume` - Rᴇsᴜᴍᴇ Yᴏᴜʀ Mᴜsɪᴄ
`.skip` - Sᴋɪᴘ Tᴏ Tʜᴇ Nᴇxᴛ Sᴏɴɢ
`.stop` - Sᴛᴏᴘ Pʟᴀʏɪɴɢ Aɴᴅ Lᴇᴀᴠᴇ
`.song` - Dᴏᴡɴʟᴏᴀᴅ Sᴏɴɢ Yᴏᴜ Wᴀɴᴛ
`.reload` - Rᴇʟᴏᴀᴅ Yᴏᴜʀ VC Cʟɪᴇɴᴛ
"""
