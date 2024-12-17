# @sesizKOLGE
# Sahib @sesizKOLGE
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Oz adina cixardanin anasin sikim
# hecneye el vurma bele isled !

from kelime_bot import pxaos as app
from pyrogram import Client, filters
import pyrogram
from pyrogram.errors import FloodWait
from datetime import datetime
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery, User

@app.on_message(filters.command("id", ["/", "!", "@", "."]))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**Sənin ID**: `{message.from_user.id}`\n**{reply.from_user.first_name}'s ID**: `{reply.from_user.id}`\n**Söhbət ID**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**👤 Sənin ID**: `{message.from_user.id}`\n**🗨 Qrup ID**: `{message.chat.id}`"
        )
