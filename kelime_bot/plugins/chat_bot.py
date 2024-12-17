
import random
import os
import logging
import asyncio
from telethon import Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import TelegramClient, events
from kelime_bot import txaos
from mesaj.chat import salam, necesen, getdim, geldim, sesizKOLGE, ban, emoji1, emoji2, fed, niye, ne, hay, mal, can, balam, xos, hara, gel, gordum
from kelime_bot.config import Config





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




