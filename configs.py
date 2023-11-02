import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "21980035"))
  API_HASH = os.environ.get("API_HASH", "667aba805ed82b19ec391bfaeafa69e4")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6734665765:AAFGHU2MGaTCiQMOQmwEH93WLtWfkHEbtw4")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Public_File_Storage_Bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001991993757"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "MoneyKamalo.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "0eefb93e1e3ce9470a7033115ceb1bad13a9d674")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6483776439"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://FileStore:FileStore@cluster0.8vuxedr.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001682319978")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001991993757"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent File Store Bot!
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add/save Uploaded File in Channel and Share a Shareable Link. 

⍟──────[ File Store Bot]──────⍟

🔸 My Name: [File Store Bot](https://t.me/{BOT_USERNAME})

🔸 Language: [Python 3](https://www.python.org)

🔸 Library: [Pyrogram](https://docs.pyrogram.org)

"""
  ABOUT_DEV_TEXT = f"""
Developer: @MExAkib

Telegram: (https://t.me/MExAkib)

Facebook: (https://www.facebook.com/MExAk1b)

Instagram: (https://www.instagram.com/ig_4k1b)

Twitter: (https://www.twitter.com/__4k1b__)

GitHub: (https://www.github.com/kmzakarialam)

"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **File Store Bot**

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link(s).

⚠️ Benefits: If you have a Telegram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File(s) & I will Send Permanent Link(s) to You & Channel will be Safe from **Copygight Infringement Issues**. Checkout **About Bot** Section For More Details.
"""
