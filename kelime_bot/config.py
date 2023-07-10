import os
 
class Config:
 
   API_ID = int(os.getenv("API_ID", "12210813"))
   API_HASH = os.getenv("API_HASH", "e42eeae11a2f96bcfc5ec3b46a30adad")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6062022905:AAF3kB_R5vLKt6HyZfkHx8NcLaMtG9Hji8I")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "***")
   OWNER_ID = int(os.environ.get("OWNER_ID","12345678"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "sesizKOLGE")
   SUPPORT = os.environ.get("SUPPORT", "salamsagil")
   BOT_NAME = os.environ.get("BOT_NAME", "test")
