from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "20031520"
# -------------------------------------------------------------
API_HASH = "a9bf896776df81c44f5b17ea535fb748"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "5923034665"))
SUPPORT_GRP = "RADHA_MUSIC_SUPPORT"
UPDATE_CHNL = "NAINCY_UPDATES"
OWNER_USERNAME = "Vishnusoni14"
