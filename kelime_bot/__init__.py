
# @sesizKOLGE
# Sahib @sesizKOLGE
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Oz adina cixardanin anasin sikim
# hecneye el vurma bele isled !

from time import sleep
from pyrogram import Client
import logging
from dotenv import load_dotenv, set_key, unset_key
from os import getenv
from kelime_bot.config import Config
from telethon import TelegramClient

load_dotenv('config.env')

# THE LOGGING

  
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)
 
 # KOLGE 
pxaos = Client(
    'AylinRobot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)

# Telethon
api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
 
txaos = TelegramClient('Xaos', api_id, api_hash).start(bot_token=bot_token)


