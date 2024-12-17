import wget
import os, requests, time
from kelime_bot.config import Config
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery 
from kelime_bot import pxaos as bot
from kelime_bot import LOGGER



@bot.on_message(filters.command("start"))
async def start(_, message: Message):
                await message.reply_photo(
                "https://te.legra.ph/file/7c24db2c84218935a8ac4.jpg",
                caption=(f"""**Salam {message.from_user.mention} 🎵\nMən əsli söhbətlərdə musiqi oxuyan botam. Ban yetkisiz, Səs yetkisi verib, Asistanı qrupa əlavə edin.\n\nSahibim👉 )**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Məni Qrupa Əlavə Et ❱ ➕", url=f"https://t.me/Morfin_Music_Bot?startgroup=true"
                    )
                ],
                
                [
                    InlineKeyboardButton(
                        "🧩 Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Rəsmi Kanal ", url=f"https://t.me/UlviiBlogs"
                    )
                ]
                
           ]
        ),
    )
  

@bot.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text("/song (musiqi adı)\n/video (video adı)\n/lyrics (musiqi adı)", 
    reply_markup=InlineKeyboardMarkup(
      [
        
        [
          InlineKeyboardButton(
            "🔄 Geri", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "Sahib 🇦🇿", url="https://t.me/nnn")
        ]
      ]
     ))
 
 

@bot.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Salam {query.from_user.mention} **""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Məni Qrupa Əlavə Et ❱ ➕", url=f"https://t.me/Morfint?startgroup=true"
                    )
                ],
                
                [
                    InlineKeyboardButton(
                        "🧩 Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Rəsmi Kanal ", url=f"https://t.me/UBlogs"
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



bot.start()
LOGGER.info(f"{Config.BOT_USERNAME} Uğurla Başladı Sahibim {Config.OWNER_NAME}")
idle()
