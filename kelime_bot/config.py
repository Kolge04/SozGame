import os
 
class Config:
 
   API_ID = int(os.getenv("API_ID", "12210813"))  # API-ID YAZ
   API_HASH = os.getenv("API_HASH", "e42eeae11a2f96bcfc5ec3b46a30adad") # API-HASH YAZ
   BOT_TOKEN = os.getenv("BOT_TOKEN", "5884794395:AAGXZ25-4BvlJzw2HB08TbwrJPbFwljl2Q8") # BOT-TOKEN YAZ
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "XAOS_Chatbot") # BOT-TAG ADIN YAZ
   OWNER_ID = int(os.environ.get("OWNER_ID","5663585448")) # OZ ID NI YAZ
   OWNER_NAME = os.environ.get("OWNER_NAME", "sesizKOLGE") # OZ TAG ADINI YAZ
   KANAL = os.environ.get("KANAL", "sesizKOLGE") #  KANALIN TAGİN YAZ
   KANAL_ADI = os.environ.get("KANAL", "♥🌹💸") #  KANALIN ADIN YAZ
   BOT_NAME = os.environ.get("BOT_NAME", "𝕏𝔸𝕆𝕊 ℂℍ𝔸𝕋 𝔹𝕆𝕋") # BOT ADINI YAZ
