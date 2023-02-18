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
BOT_TOKEN = getenv("BOT_TOKEN", "6283163238:AAE6T-KjsbVR9QDWD3GakTdnL0Ju28LkFZw")
STRING_SESSION = getenv("STRING_SESSION", "BQA4GzgPejirax8FMB2NHtVE3d8fxfzYqcaTt9YukSZofHB1PG6YeInwMx-e9gcwnRtgPgXVI-cv5TjA1tGsCDtSif0ftPUcSrgYgU0KItHgAJ_KUkIdT3jZnkrNjjtnlhPMYl45SsQyNI-eetJjgHK1_owJEHeHbAiVZyc8MduKURJ3SOyyeDth15Tzy2Oxp8mHUU8JOAI0gGnE6WdZYXY5E9TFDH4IE7C4ulOLXzlj7QGgmyOFCOSzPML3hC2hXz6j-MUaWOktzmNLHtT6FnafNuIsK4dsU1JvaNEufSTqmYNo7wOkEpqL0vEgOU0YEvjVD-kbW0IQYOKggd0SCuRMAAAAAVVad90A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! /").split())
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Amala203145:Amala2031456@cluster0.t9ibfge.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5726959581").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001446681008"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5726959581").split()))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/zaherkhanbhai/GrootUserBot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
