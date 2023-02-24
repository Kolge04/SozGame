from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕𝐌ə𝐧𝐢 𝐪𝐫𝐮𝐩𝐚 ə𝐥𝐚𝐯ə 𝐞𝐭➕", url=f"http://t.me/XAOS_Gamebot?startgroup=new")
    ],
    [
        InlineKeyboardButton(" 𝐎𝐰𝐧𝐞𝐫 🇦🇿 ", url="t.me/sesizKOLGE"),
        InlineKeyboardButton("𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="t.me/XaosResmii"),
    ]
])


START = """
**👋 Salam 𝕏𝔸𝕆𝕊 𝔾𝔸𝕄𝔼 Söz Oyun Botuna xoş gəldin.**\n🤖** Bu Bot İlə Qarışıq Həriflərdən İbarət Söz Tapmaq Oyunu Oynaya Bilərsiniz..**

➤ Oyun Qaydaları üçün 👉 /help Üzərinə Klikləyin. 📚 Əmrlər Asan və Sadədir.
"""

HELP = """
** Əmrlər menyusuna xoş gəldin.**


✅ /start - Botu Başladar..
🎮 /oyna - Söz Tap Oyunu Başladar.. 
➡️ /kec - Növbəti Sözə Keçər..
🏆 /reytinq - Oyunçular Arasında Qrup reyrinqi..
⛔ /dayan - Söz Tap Oyununu Sonlandırar
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://telegra.ph/file/7770592d74a8bf3236382.jpg",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("help", [".", "!", "/", "@"]))
async def help(bot, message):
  await message.reply_photo("https://telegra.ph/file/7770592d74a8bf3236382.jpg",caption=HELP) 

# Oyunu başlat. 
@Client.on_message(filters.command("oyna", ["!", "/", "@", "."])) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗ Hal-Hazırda Qrupunuzda  Oyun Davam Edir ✍🏻 \n Oyunu Sonlandırmaq Üçün /dayan Əmrindəm İsdifadə Edin")
    else:
        await m.reply(f"**{m.from_user.mention}** Tərəfindən! \nSöz Tapma Oyunu Başladı .\n\nUğurlar !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/100 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazandığın Xal: 50
🔎 İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarışıq Hərflərdən İbarət Sözü Tapın 
        """
        await c.send_message(m.chat.id, text)
        
