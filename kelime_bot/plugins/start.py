
# @sesizKOLGE
# Sahib @sesizKOLGE
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Oz adina cixardanin anasin sikim
# hecneye el vurma bele isled !


import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from kelime_bot import txaos as client
from kelime_bot.config import Config
 
 
 
 
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("● Salam Mənin adım  {Config.BOT_NAME}\n● Qruplar Üçün yaradılmış ÇhatBotuyam\n● Əmrlərlə Tanış Olmaq Üçün __ƏMRLƏR__ Butonuna Toxun",
                    buttons=(
                   
		      [Button.url('➕ QRUPA ƏLAVƏ ET ➕', 'https://t.me/{Config.BOT_USERNAME}?startgroup=a')],
                      [Button.url('⚡ {Config.KANAL_ADI}', f'https://t.me/{Config.KANAL}')],
                      [Button.url('🇦🇿 𝕆𝕎ℕ𝔼ℝ 👨‍💻', f'https://t.me/{Config.OWNER_NAME}')],
                      [Button.inline("⚙ ƏMRLƏR", data="help")],
                    ),
                    link_preview=False
		   )
 
@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    await event.edit(f"● Salam Mənin adım  {Config.BOT_NAME}\n● Qruplar Üçün yaradılmış ÇhatBotuyam\n● Əmrlərlə Tanış Olmaq Üçün __ƏMRLƏR__ Butonuna Toxun", buttons=(
                      
                      [Button.url('➕ QRUPA ƏLAVƏ ET ➕', 'https://t.me/{Config.BOT_USERNAME}?startgroup=a')],
                      [Button.url('⚡ {Config.KANAL_ADI}', f'https://t.me/{Config.KANAL}')],
                      [Button.url('🇦🇿 𝕆𝕎ℕ𝔼ℝ 👨‍💻', f'https://t.me/{Config.OWNER_NAME}')],
                      [Button.inline("⚙ ƏMRLƏR", data="help")],
                    ),
                    link_preview=False)
 
			     
@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):
    await event.edit(f"⚡ {Config.BOT_NAME} İn Əmrləri \n\n➪/start - Botu Başladar\n➪/chatbot on ChatBot u Başladar\n➪ /chatbot off ChatBot u Dayandırar\n➪ /link_close on Atılan linkləri və Mobil Nömrələri Silər\n➪ /link_close off Link Silmə Özəlliyin Bağlayar\n➪ /ID ID Verer", buttons=(
                      [Button.url('➕ QRUPA ƏLAVƏ ET ➕', 'https://t.me/{Config.BOT_USERNAME}?startgroup=a')],
                      [Button.inline("◀ GERİ", data="start")],
                    ),
                    link_preview=False)
 
 

                   
