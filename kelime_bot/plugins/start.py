import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from kelime_bot import kolge as client
 
 
 
 
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("● Salam Mənin adım  {BOT_NAME}\n● Qruplar Üçün yaradılmış ÇhatBotuyam\n● Əmrlərlə Tanış Olmaq Üçün __ƏMRLƏR__ Butonuna Toxun",
                    buttons=(
                   
		      [Button.url('➕ QRUPA ƏLAVƏ ET ➕', 'https://t.me/{BOT_USERNAME}?startgroup=a')],
                      [Button.url('⚡ {KANAL_ADI}', f'https://t.me/{KANAL}')],
                      [Button.url('🇦🇿 𝕆𝕎ℕ𝔼ℝ 👨‍💻', f'https://t.me/{OWNER_NAME}')],
                      [Button.inline("⚙ ƏMRLƏR", data="help")],
                    ),
                    link_preview=False
		   )
 
@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    await event.edit(f"● Salam Mənin adım  {BOT_NAME}\n● Qruplar Üçün yaradılmış ÇhatBotuyam\n● Əmrlərlə Tanış Olmaq Üçün __ƏMRLƏR__ Butonuna Toxun", buttons=(
                      
                      [Button.url('➕ QRUPA ƏLAVƏ ET ➕', 'https://t.me/{BOT_USERNAME}?startgroup=a')],
                      [Button.url('⚡ {KANAL_ADI}', f'https://t.me/{KANAL}')],
                      [Button.url('🇦🇿 𝕆𝕎ℕ𝔼ℝ 👨‍💻', f'https://t.me/{OWNER_NAME}')],
                      [Button.inline("⚙ ƏMRLƏR", data="help")],
                    ),
                    link_preview=False)
 
			     
@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):
    await event.edit(f"⚡ {BOT_NAME} İn Əmrləri \n\n➪ /chatbot on ChatBot u Başladar\n➪ /chatbot off ChatBot u Dayandırar\n➪ /link_close on Atılan linkləri və Mobil Nömrələri Silər\n➪ /link_close off Link Silmə Özəlliyin Bağlayar /start - Botu Başladar", buttons=(
                      [Button.url('➕ QRUPA ƏLAVƏ ET ➕', 'https://t.me/{BOT_USERNAME}?startgroup=a')],
                      [Button.inline("◀ GERİ", data="start")],
                    ),
                    link_preview=False)
 
 

                   
