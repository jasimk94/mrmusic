import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 24662602
API_HASH = "680d30125e0ecf7c79b99b8a1a6d038c"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7495084986:AAHRzgba8D_fY6BsrL_5ncFL8bD03SrMJ9E"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://dmcapbd:Bk7HZXaXDUDNKMqo@cluster0.v2fw9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002281566445

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 1621509785

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/PremiumNetworkCommunity"
SUPPORT_GROUP = "https://t.me/PremiumNetworkCommunity"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQF4UkoAVtsN7tjQ-MFk51jTLnuydgsaCns_LQqTeP-z19ms12ah1skjpUZWHHWBLYadUdGVpA8eWtF-yuu0jUKRHSzdSnpUWRdEwWZamQWoMjfj4LE6LCSv0fL4JKh09VXKykhoLjClX-ErVGmHxbTKMC498V_qXRaBpae1S8sdgHv65KETOey2HiPIN2WyzGIeHzY_CrUoIcE223PcJ1kiuy7qLIvGljqBgi3eiYEQWhe8otk_4vJy7AgCxwoEhXi2sWjyk94zwMRON5Mg7pzfQRLBR5s_D0-Z_ZRc3Dr6DKCcLsbLMpJXgEtypggKKdlCr977zDEu7q9BAXC1AQlJcvcgTAAAAAGzKkBcAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/eb9931c46524594abaa06-6bfe0d0ba54e214020.jpg"

PING_IMG_URL = "https://graph.org/file/eb9931c46524594abaa06-6bfe0d0ba54e214020.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/6fe211cdac8e7c06d28f1-eff94e60b520bb9af9.jpg"
STATS_IMG_URL = "https://graph.org/file/bdfce6cefd1c71566c687-0c18ec38c8177529dd.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
