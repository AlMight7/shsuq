import os
from pyrogram import Client
from telethon import TelegramClient


TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_NAME = os.environ.get("BOT_NAME")
DB_URL = os.environ.get("DB_URL")
SAUCE_API = os.environ.get("SAUCENAO_API")
ANILIST_CLIENT = os.environ.get("ANILIST_CLIENT")
ANILIST_SECRET = os.environ.get("ANILIST_SECRET")
ANILIST_REDIRECT_URL = os.environ.get("ANILIST_REDIRECT_URL", "https://anilist.co/api/v2/oauth/pin")
API_ID = int(os.environ.get("API_ID"))
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID"))
OWNER = list(filter(lambda x: x, map(int, os.environ.get("OWNER_ID").split())))  ## sudos can be included

DOWN_PATH = "Wolford/downloads/"
HELP_DICT = dict()

api_id = API_ID
api_hash = API_HASH
bot_token = BOT_TOKEN

tbot = TelegramClient('anon', api_id, api_hash).start(bot_token=bot_token)

plugins = dict(root="Wolford/plugins")
Wolford = Client("Wolford", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=plugins)
