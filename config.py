import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6667689198:AAEVoU3UBenOeMzSPFZj7-81HVS5v5GjKVc")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "27284732"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8d242ebf776e7d3c487b97cf3951cb9c")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002108053748"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1163318744"))

# Port
PORT = os.environ.get("PORT", "8141")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://naibansari987:Yuuichi@cluster0.o0uekd9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

# Force sub channel id, if you want enable force sub
FORCE_CHANNEL = int(os.environ.get("FORCE_CHANNEL", "-1002441248860"))
FORCE_CHANNEL2 = int(os.environ.get("FORCE_CHANNEL2", "-1001567633045"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Mainly add graph else telegraph link
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/08580b534ac313cc6b379.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/08580b534ac313cc6b379.jpg")

# Add your text according to you
HELP_TXT = "<b>Hi Dude!\nThis is an file to link bot work for @Animes_VQ\n\n❏ Bot Cammands\n├/start : start the bot\n├/about : Our Information\n└/help : Help related Bot\n\n💥 Simply click on link and start the bot join both channels and try again thats it.....!\n\n🧑‍💻Owned By <a href=https://t.me/Yuuich1_Sama>𓆰𝒀𝒖𝒖𝒊𝒄𝒉𝒊~𝑺𝒂𝒎𝒂𓂀</a></b>"
ABOUT_TXT = "<b>⟦⟧ Hi There {first}!💫\n┏━━━━━━━❪❂❫━━━━━━━━\n◈ ᴏᴡɴᴇʀ: <a href=https://t.me/Yuuich1_Sama>𓆰𝒀𝒖𝒖𝒊𝒄𝒉𝒊~𝑺𝒂𝒎𝒂𓂀</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/the_vanquishers>ᴛʜᴇ ᴠᴀɴϙᴜɪsʜᴇʀs</a>\n◈ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/animes_vq>ᴀɴɪᴍᴇ ᴜɴɪᴛʏ</a>\n◈ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>\n◈ ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://dashboard.heroku.com>Heroku</a>\n┗━━━━━━━❪❂❫━━━━━━━━</b>"

# start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ ᴛʜᴇʀᴇ... {first}! 💥\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\nᴘᴏᴡᴇʀᴇᴅ ʙʏ - @Animes_VQ</b>")
try:
    ADMINS=[5090651635]
    for x in (os.environ.get("ADMINS", "6159157391 1733067205 2067141797 1163318744 5734659617 6105051472").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Owner list does not contain valid integers.")

# Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>👋 ʜᴇʟʟᴏ {first}!\nᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs [ ᴛᴀᴘ ᴏɴ ᴊᴏɪɴ ⚡️] ᴛʜᴇɴ\nᴅᴏᴡɴʟᴏᴀᴅ ʙʏ ᴛᴀᴘᴘɪɴɢ ᴏɴ ⚡️ᴛʀʏ ᴀɢᴀɪɴ\nᴛʜᴀɴᴋ ʏᴏᴜ ❤️</b>")

# set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "​🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ​ - @Animes_VQ"

ADMINS.append(OWNER_ID)
ADMINS.append(5090651635)

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "600"))
DEL_MSG = "<b>This File is deleting automatically in {time}. Forward in your Saved Messages..!</b>"

LOG_FILE_NAME = "filesharingbot.txt"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# Hi There My Name is Sahil and if you like this repo make sure to give it a thumbs up and don't Remove my credit....
