"""
____________________________________________
# @sesizKOLGE                                  |
# Sahib @sesizKOLGE                            |
# Repo Açığdısa İcazəsis Götürmə Oğlum         |
# Oz adina cixardanin anasin sikim             |
# hecneye el vurma bele isled !                |
_______________________________________________

"""


from config import Config
from time import sleep
import logging
from dotenv import load_dotenv, set_key, unset_key
from os import getenv
import wget
import os, requests, time
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters, idle
import pyrogram
from pyrogram.errors import FloodWait
from datetime import datetime
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery, User
import random
import os
import logging
import asyncio
from telethon import Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import TelegramClient, events
from mesaj.chat import salam, necesen, getdim, geldim, sesizKOLGE, ban, emoji1, emoji2, fed, niye, ne, hay, mal, can, balam, xos, hara, gel, gordum











load_dotenv('config.env')

# THE LOGGING

  
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)
 
 # KOLGE 
bot = Client(
    'Pxaos',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)

# Telethon
api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
 
xaos = TelegramClient('Txaos', api_id, api_hash).start(bot_token=bot_token)







@bot.on_message(filters.command("start"))
async def start(_, message: Message):
                await message.reply_photo(
                f"{Config.START_IMG}",
                caption=(f"""**👋Salam {message.from_user.mention}\n💬Mən {Config.BOT_NAME} Rəsmi Chat botuyam Söhbət Botuyam.\nℹ Məlumat Üçün 🧩 Əmirlər Butonuna Toxun\n👉 Sahibim @{Config.OWNER_NAME}**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰  Məni Qrupa Əlavə Et  ❱ ➕", url=f"https://t.me/{Config.BOT_USERNAME}?startgroup=true"
                    )
                ],
                
                [
                    InlineKeyboardButton(
                        "🧩 Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Rəsmi Kanal ", url=f"https://t.me/{Config.KANAL}"
                    )
                ]
                
           ]
        ),
    )
  

@bot.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(f"{Config.BOT_NAME} İsdifadə Qaydaları\n\n/chatbot on - Söhbət Botun Aktiv Edər ✔\n/chatbot off - Söhbət Botun Deaktiv Edər\n/link_close [on / off]- Qrupa atılan icazəsiz linkləri silər✔\n/id - İD Məlumatların Atar 🆔\n\nSalam yazıldıqda Maraqlı Cavab verər)", 
    reply_markup=InlineKeyboardMarkup(
      [
        
        [
          InlineKeyboardButton(
            "🔄 Geri", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "Sahib 🇦🇿", url=f"https://t.me/{Config.OWNER_NAME}")
        ]
      ]
     ))
 
 

@bot.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**👋Salam {message.from_user.mention}\n💬Mən {Config.BOT_NAME} Rəsmi Chat botuyam Söhbət Botuyam.\nℹ Məlumat Üçün 🧩 Əmirlər Butonuna Toxun\n👉 Sahibim @{Config.OWNER_NAME}**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰  Məni Qrupa Əlavə Et  ❱ ➕", url=f"https://t.me/{Config.BOT_USERNAME}?startgroup=true"
                    )
                ],
                
                [
                    InlineKeyboardButton(
                        "🧩 Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Rəsmi Kanal ", url=f"https://t.me/{Config.KANAL}"
                    )
                ]
                
           ]
        ),
                                 )



# ~~~~~~~~~~~~~~~~~~~~~~ Poseidon song ~~~~~~~~~~~~~~~~~~~~~~

#alive mesajı#

@bot.on_message(filters.command("alive") & filters.user(Config.OWNER_ID))
async def live(client: Client, message: Message):
    livemsg = await message.reply_text('Aktivəm Sahibim..⚡️')










# Chatbot
 

isleyen = []
rxyzdev_tagTot = {}

@xaos.on(events.NewMessage(pattern="^[/.!]chatbot ?(.*)"))
async def chatbot(event):
    global isleyen
    rxyzdev_tagTot[event.chat_id] = 0
    if event.is_private:
      return await event.respond("❌ **ChatBot PM Də Qadağandır**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**", buttons=(
			                                 [
                                    Button.url('➕ QRUPA ƏLAVƏ ET ➕', f'https://t.me/{Config.BOT_USERNAME}?startgroup=a')
                                    ],
                                  ),
                                  link_preview=False)
 
    admins = []
    async for admin in xaos.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
      admins.append(admin.id)
    if not event.sender_id in admins:
      return await event.reply("**⛔ Siz Admin Deyilsiz!**\n✅ **Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
  
 
    emr = event.pattern_match.group(1)
    qrup = event.chat_id
    if emr == "ON" or emr == "on" or emr == "On":
        if qrup not in isleyen:
            isleyen.append(qrup)
            aktiv_olundu = "✅ **ChatBot Qrupda Aktiv Olundu !**"
            await event.reply(aktiv_olundu)
            return
        await event.reply("⚠️ **ChatBot Hal-hazırda Qrupda Aktivdir !**")
        return
    elif emr == "OFF" or emr == "off" or emr == "Off":
        if qrup in isleyen:
            isleyen.remove(qrup)
            await event.reply("⛔️ **ChatBot Qrupda Deaktiv Olundu !**")
            return # aykhan026 | aykhan_s
        await event.reply("⚠️ **ChatBot Hal-Hazırda Deaktivdir !**")
        return
    
    else:
        await event.reply("🤖 Chatbot u Aktiv Edmək Üçün On və  Off yazın")



        
        
@xaos.on(events.NewMessage)
async def chatbot(event):
    global isleyen
    mesaj = str(event.raw_text)
    qrup = event.chat_id
    if qrup not in isleyen:
        return
    if "Salam" in mesaj or "salam" in mesaj:
        await event.reply(f"{random.choice(salam)}")
    if "necesen" in mesaj or "necəsən" in mesaj or "netersen" in mesaj or "nətərsən" in mesaj or "Netersen" in mesaj:
        await event.reply(f"{random.choice(necesen)}")
    if "Getdim" in mesaj or "getdim" in mesaj or "getdım" in mesaj:
        await event.reply(f"{random.choice(getdim)}")
    if "Geldim" in mesaj or "geldim" in mesaj or "geldım" in mesaj or "Geldım" in mesaj:
        await event.reply(f"{random.choice(geldim)}")
    if "@sesızKOLGE" in mesaj or "kolge" in mesaj or "Kolge" in mesaj:
        await event.reply(f"{random.choice(sesizKOLGE)}")
    if "Xaos" in mesaj or "xaos" in mesaj:
        await event.reply(f"{random.choice(fed)}")
    if "Ban" in mesaj or "ban" in mesaj or "/gban" in mesaj or "gban" in mesaj in mesaj or "/ban" in mesaj:
        await event.reply(f"{random.choice(ban)}")
    if "😁" in mesaj or "😬" in mesaj or "😄" in mesaj or "🥶" in mesaj or "😌" in mesaj:
        await event.reply(f"{random.choice(emoji1)}")
    if "🤣" in mesaj or "😅" in mesaj in mesaj or "😂" in mesaj or "😄" in mesaj:
        await event.reply(f"{random.choice(emoji2)}")
    if "Niye" in mesaj or "niye" in mesaj or "Niyə" in mesaj or "niyə" in mesaj:
        await event.reply(f"{random.choice(niye)}")
    if "Nə" in mesaj or "nə" in mesaj or "Ne" in mesaj or "ne" in mesaj or "what" in mesaj in mesaj or "What" in mesaj:
        await event.reply(f"{random.choice(ne)}")
    if "Hay" in mesaj or "hay" in mesaj in mesaj or "haay" in mesaj:
        await event.reply(f"{random.choice(hay)}")
    if "Mal" in mesaj or "mal" in mesaj in mesaj or "Qoyun" in mesaj or "qoyun" in mesaj:
        await event.reply(f"{random.choice(mal)}")
    if "Can" in mesaj or "can" in mesaj or "Haycan" in mesaj or "haycan" in mesaj or "uss" in mesaj:
        await event.reply(f"{random.choice(can)}")
    if "Balam" in mesaj or "balam" in mesaj:
        await event.reply(f"{random.choice(balam)}")
    if "xos" in mesaj or "Xos" in mesaj in mesaj or "Xoş" in mesaj or "xoş" in mesaj:
        await event.reply(f"{random.choice(xos)}")
    if "Hara" in mesaj or "hara" in mesaj or "haraya" in mesaj or "Haraya" in mesaj or "haraki" in mesaj:
        await event.reply(f"{random.choice(hara)}")
    if "Gəl" in mesaj or "gəl" in mesaj or "Gel" in mesaj or "gel" in mesaj:
        await event.reply(f"{random.choice(gel)}")
    if "Gördüm" in mesaj or "gördüm" in mesaj or "Gordum" in mesaj or "gordum" in mesaj:
        await event.reply(f"{random.choice(gordum)}")
    if "Ok" in mesaj or "ok" in mesaj:
        await event.reply(f"OKDAAA OKKKKKKK")












# LİNK_CLOSE


CLOSE = f"🗑️**Qrupa Göndərilən Linki Sildim**\n---------------------------------------------------------\n❌** Bu Qrupa Hər Hansısa Link Göndərməyə  İcazə Yoxdu**"

NUMBER = f"🗑️**Qrupa Göndərilən Mobil Nömrəni Sildim**\n---------------------------------------------------------\n❌** Bu Qrupa Hər Hansısa Link Və Ya Mobil Nömrə Göndərməyə  İcazə Yoxdu**"

isleyen = []
rxyzdev_tagTot = {}
 
@xaos.on(events.NewMessage(pattern="^[/.!]link_close ?(.*)"))
async def chatbot(event):
    global isleyen
    rxyzdev_tagTot[event.chat_id] = 0
    if event.is_private:
      return await event.respond("❌ /link_close **Əmri PM Də Qadağandır**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**", buttons=(
			                                 [
                                    Button.url('➕ QRUPA ƏLAVƏ ET ➕', f'https://t.me/{Config.BOT_USERNAME}?startgroup=a')
                                    ],
                                  ),
                                  link_preview=False)
 
    admins = []
    async for admin in xaos.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
      admins.append(admin.id)
    if not event.sender_id in admins:
      return await event.reply("**⛔ Siz Admin Deyilsiz!**\n✅ **Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
  

 
    emr = event.pattern_match.group(1)
    qrup = event.chat_id
    if emr == "ON" or emr == "on" or emr == "On":
        if qrup not in isleyen:
            isleyen.append(qrup)
            aktiv_olundu = f"✅ **Tamamdır Paşam.!**\n🗑️ Artıq Qrupa Atılan Hər Bir Linki Siləcəm\n⛔ __YouTube, Whatsapp, Telegram, İnstagram, Facebook, Google, Mobil-Nömrə, Və S__.\n"
            await event.reply(aktiv_olundu)
            return
        await event.reply("⚠️ **LİNK_CLOSE Hal-Hazırda Qrupda Aktivdir !**")
        return
    elif emr == "OFF" or emr == "off" or emr == "Off":
        if qrup in isleyen:
            isleyen.remove(qrup)
            await event.reply("⛔️ **Tamamdır Paşam**\n🗑️ Artiq Qrupa Göndərilən Linkləri Silməyəcəm !**")
            return # aykhan026 | aykhan_s
        await event.reply("⚠️ **LİNK_CLOSE Hal-Hazırda Qrupda Deaktivdir !**")
        return
    
    else:
        await event.reply("✅ **LİNK_CLOSE ni Aktivləşdirmək Üçün link_close on Yazın**\n❌ **Söndürmək Üçün link_close off yazın**")
 
 
 
        
        
@xaos.on(events.NewMessage)
async def chatbot(event):
    global isleyen
    mesaj = str(event.raw_text)
    qrup = event.chat_id
    if qrup not in isleyen:
        return
      
    if "https://instagram.com/" in mesaj or "https://www.instagram.com/" in mesaj: #instagram
        await event.delete()
        await event.reply(f"{CLOSE}")
    if "https://chat.whatsapp.com/" in mesaj or "https://whatsapp.com/" in mesaj:# Whatsapp
        await event.delete()
        await event.reply(f"{CLOSE}")
    if "https://www.youtube.com/" in mesaj:# YouTube
        await event.delete()
        await event.reply(f"{CLOSE}")
    if "https://t.me/" in mesaj: # Telegram
        await event.delete()
        await event.reply(f"{CLOSE}")
    if "https://www.google.com/" in mesaj or "https://google.com/" in mesaj: # Google
        await event.delete()
        await event.reply(f"{CLOSE}")
    if "https://vt.tiktok.com/" in mesaj or "https://www.tiktok.com/" in mesaj or "https://tiktok.com/" in mesaj: # TikTok
        await event.delete()
        await event.reply(f"{CLOSE}")
    if "https://www.facebook.com/" in mesaj or "https://facebook.com/" in mesaj: # Facebook
        await event.delete()
        await event.reply(f"{CLOSE}")
    if "+99450" in mesaj or "+99451" in mesaj or "+99455" in mesaj or "+99470" in mesaj or "+99477" in mesaj: # Mobil nömrə
        await event.delete()
        await event.reply(f"{NUMBER}")
    if "051" in mesaj or "050" in mesaj or "055" in mesaj or "070" in mesaj or "077" in mesaj or "010" in mesaj: # Mobil nömrə
        await event.delete()
        await event.reply(f"{NUMBER}")




@xaos.on(events.NewMessage(pattern='salam'))
@xaos.on(events.NewMessage(pattern='Salam'))
async def bilgi(event):
    
    a = await event.reply("👋 Salam Aleykuma..")
    await asyncio.sleep(2)
    await a.edit("🌹 Xoş Gəldin")
    await asyncio.sleep(2)
    await a.edit("🤔 Necəsən?")
    await asyncio.sleep(2)
    await a.edit("❤️ Ümid Varam Yaxşısan...")
    await asyncio.sleep(9)
    await a.delete()




@bot.on_message(filters.command("id", ["/", "!", "@", "."]))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**{reply.from_user.first_name}'s ID**: `{reply.from_user.id}`\n**Söhbət ID**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**👤 Sənin ID**: `{message.from_user.id}`\n**🗨 Qrup ID**: `{message.chat.id}`"
        )



bot.run()



