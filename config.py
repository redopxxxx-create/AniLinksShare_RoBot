import logging
import os
from logging.handlers import RotatingFileHandler
from typing import List


def _get_int(name: str, default: int) -> int:
    value = os.environ.get(name)
    if value in (None, ""):
        return default
    try:
        return int(value)
    except ValueError:
        return default


def _get_int_list(name: str, default: List[int]) -> List[int]:
    raw = os.environ.get(name, "")
    if not raw.strip():
        return default
    output: List[int] = []
    for item in raw.replace(",", " ").split():
        try:
            output.append(int(item))
        except ValueError:
            continue
    return output or default




def _get_str(name: str, default: str) -> str:
    value = os.environ.get(name)
    if value is None:
        return default
    value = value.strip()
    return value or default
TG_BOT_TOKEN = _get_str("TG_BOT_TOKEN", "")
APP_ID = _get_int("APP_ID", 0)
API_HASH = _get_str("API_HASH", "")

OWNER_ID = _get_int("OWNER_ID", 7738104912)
PORT = _get_int("PORT", 8080)

DB_URI = _get_str("DB_URI", _get_str("MONGO_URI", _get_str("MONGODB_URI", "mongodb://localhost:27017")))
DB_NAME = _get_str("DB_NAME", "link")

CHAT_ID = _get_int_list("CHAT_ID", [])
TEXT = os.environ.get(
    "APPROVED_WELCOME_TEXT",
    "<b>{mention},\n\nAapka join request {title} ke liye approve ho gaya hai.\n\nPowered by bot.</b>",
)
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

TG_BOT_WORKERS = _get_int("TG_BOT_WORKERS", 40)

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg")
START_IMG = START_PIC
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Namaste! Yeh advanced link sharing bot hai. Isse aap Telegram channel links secure tareeke se share kar sakte ho.</b>",
)
HELP = os.environ.get(
    "HELP_MESSAGE",
    "<b>Help chahiye? /start karo, channel add karo, aur secure link generate karo. Agar issue aaye to admin se contact karein.</b>",
)
ABOUT = os.environ.get(
    "ABOUT_MESSAGE",
    "<b>Yeh bot temporary Telegram invite links banata hai taaki aapke channels safe rahein.</b>",
)

ABOUT_TXT = """<b>Community and updates links bot owner ke hisaab se configure kiye ja sakte hain.</b>"""
CHANNELS_TXT = """<b>Available channels ke links owner configure karega.</b>"""

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ Sirf owner/admin commands execute kar sakte hain."

LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = _get_int("DATABASE_CHANNEL", 0)

ADMINS = _get_int_list("ADMINS", [OWNER_ID])
if OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
