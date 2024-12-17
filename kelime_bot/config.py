import os
 
class Config:
 
   API_ID = int(os.getenv("API_ID", "12210813"))  # API-ID YAZ
   API_HASH = os.getenv("API_HASH", "e42eeae11a2f96bcfc5ec3b46a30adad") # API-HASH YAZ
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6062022905:AAF3kB_R5vLKt6HyZfkHx8NcLaMtG9Hji8I") # BOT-TOKEN YAZ
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "") # BOT-TAG ADIN YAZ
   OWNER_ID = int(os.environ.get("OWNER_ID","")) # OZ ID NI YAZ
   OWNER_NAME = os.environ.get("OWNER_NAME", "sesizKOLGE") # OZ TAG ADINI YAZ
   SUPPORT = os.environ.get("SUPPORT", "") # SPORT KANALI YAZ
   BOT_NAME = os.environ.get("BOT_NAME", "") # BOT ADINI YAZ
