import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from kelime_bot import kolge as client
 
 
 
 
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("⚡ Mən  𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ\n𝕏𝔸𝕆𝕊 Federasiyasının Rəsmi Tağ botuyam\n⚡ 𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ İlə Qrupunuzdakı Üyələri Etiket Edə Bilərəm\nƏmrlərlə Tanış Olmaq Üçün __ƏMRLƏR__ Butonuna Toxun",
                    buttons=(
                   
		      [Button.url('➕ ℚℝ𝕌𝕆𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Tagbot?startgroup=a')],
                      [Button.url('⚡ 𝕏𝔸𝕆𝕊 𝔽𝔹𝔸ℕ', f'https://t.me/XaosResmii')],
                      [Button.url('🇦🇿 𝕆𝕎ℕ𝔼ℝ 👨‍💻', f'https://t.me/sesizKOLGE')],
                      [Button.inline("⚙ Ə𝕄ℝ𝕃Ə𝕃", data="help")],
                    ),
                    link_preview=False
		   )
 
@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    await event.edit(f"**⚡ Mən  𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ\n**𝕏𝔸𝕆𝕊 Federasiyasının Rəsmi Tağ botuyam\n⚡ 𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ İlə Qrupunuzdakı Üyələri Etiket Edə Bilərəm\nƏmrlərlə Tanış Olmaq Üçün __ƏMRLƏR__ Butonuna Toxun**", buttons=(
                      
                      [Button.url('➕ ℚℝ𝕌𝕆𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Tagbot?startgroup=a')],
                      [Button.url('⚡ 𝕏𝔸𝕆𝕊 𝔽𝔹𝔸ℕ', f'https://t.me/XaosResmii')],
                      [Button.url('🇦🇿 𝕆𝕎ℕ𝔼ℝ 👨‍💻', f'https://t.me/sesizKOLGE')],
                      [Button.inline("⚙ Ə𝕄ℝ𝕃Ə𝕃", data="help")],
                    ),
                    link_preview=False)
 
			     
@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):
    await event.edit(f"⚡ 𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ İn Əmrləri \n\n➪ /sehidler <səbəb> Şəhid Adları İlə Tağ Edər\n➪ /tag <səbəb> - 5-li Tağ Edər\n➪ /etag <səbəb> - Emoji İlə Tağ Edər\n➪ /btag <səbəb> - Bayraqlarla Tağ Edər\n➪ /mtag <səbəb>  Mafia Rolları İlı Tağ Edər\n➪ /rtag <səbəb> Rayon Və Şəhər Adları İlə Tağ Edər\n➪ /ttag <səbəb> - Tək Teək Tağ Edər\n➪ /admins <səbəb> - Adminləri Tağ Edər\n➪ /cancel - Tağ Prosesin Saxlayar\n➪ /start - Botu Başladar", buttons=(
                      [Button.url('➕ ℚℝ𝕌ℙ𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Tagbot?startgroup=a')],
	              [Button.inline("ℹ 𝕀ℕ𝔽𝕆", data="info")],
                      [Button.inline("🗑 𝔹𝔸𝔾𝕃𝔸", data="start")],
                    ),
                    link_preview=False)
 
 
@client.on(events.callbackquery.CallbackQuery(data="info"))
async def handler(event):
    await event.edit(f"**Çox Özəllikli Tağ Botu Axtarmağa Çalışan Qrub Sahibləri  ⚡  𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ Bot Sizə Görə:\n\n☞︎︎︎ Şəhid Adları İlə Tağ Edər\n☞︎︎︎ 5-Li Tağ\n☞︎︎︎ Emojilərlə Tağ Edər\n☞︎︎︎ Bayraqlarla Tağ Edər\n☞︎︎︎ Mafia Rolları İlə Tağ Edər\n☞︎︎︎ Rayon Və Şəhər Adları İlə Tağ Edər\n☞︎︎︎ Təkli Tağ\n☞︎︎︎ Yalnız Admimləri Tağ\n\n\nBelə Çox Özəllikli @XAOS_Tagbot 'u Qrupunuza Yönətici Olaraq Alıb Rahatlıqla , Tağ edə bilirsiz**", buttons=(      
	              [Button.url('➕ ℚℝ𝕌ℙ𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Tagbot?startgroup=a')],
		      [Button.inline("⚙ 𝔼𝕊𝔸𝕊 𝕄𝔼𝕐ℕ𝕌", data="start")],
		    ),
                    link_preview=False)
                   
