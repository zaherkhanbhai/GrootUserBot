import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
if os.path.exists("Internal"):
    load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
admins = {}
que = {}

API_ID = int(getenv("API_ID", "26305268"))
API_HASH = getenv("API_HASH", "4e385c619185805f48427df36458d056")
BOT_TOKEN = getenv("BOT_TOKEN", " ")
STRING_SESSION = getenv("STRING_SESSION", "session")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! /").split())
MONGO_DB_URL = getenv("MONGO_DB_URL", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5726959581").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5726959581").split()))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/zaherkhanbhai/GrootUserBot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
