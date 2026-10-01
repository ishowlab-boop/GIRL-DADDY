import os
from dotenv import load_dotenv

load_dotenv()

# -------------------------
# FIXED ADMIN IDS
# -------------------------
ADMIN_IDS = [1800295558]   # আপনার Telegram numeric ID

# Tokens / API
TELEGRAM_BOT_TOKEN = os.getenv("BOT_TOKEN", "")
FISH_AUDIO_API_KEY = os.getenv("VOICE_API_KEY", "")

# Fish Audio
FISH_AUDIO_BASE_URL = os.getenv("FISH_AUDIO_BASE_URL", "https://api.fish.audio")
FISH_AUDIO_BACKEND = os.getenv("FISH_AUDIO_BACKEND", "s1")
FISH_AUDIO_MP3_BITRATE = int(os.getenv("FISH_AUDIO_MP3_BITRATE", "128"))
FISH_AUDIO_OPUS_BITRATE = int(os.getenv("FISH_AUDIO_OPUS_BITRATE", "48000"))

# Misc
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "t.me/Ariyanfix")
WEBSITE_URL = os.getenv("WEBSITE_URL", "modelboxbd.com")

DB_PATH = os.getenv("DB_PATH", "file.db")
VOICES_DIR = os.getenv("VOICES_DIR", "voices")

COST_PER_VOICE = 1
REQUIRE_VALIDITY_FOR_TTS = False
MAX_TTS_CHARS = int(os.getenv("MAX_TTS_CHARS", "200"))

DEFAULT_MODELS = [
    {"id": "0f57b9f5c27e47f380193e4233126f5d", "name": "Mariya🤷‍♀️"},
    {"id": "89caeb03934840e791f7d13e9c03b6ef", "name": "Daisy🧕"},
    {"id": "8a7f5c27e2e04596b079e78a475d852b", "name": "Lacy🙇‍♀️"},

]

USE_CONFIG_MODELS_ONLY = True

PLANS = [
    {"name": "Starter", "credits": 50, "price": "$5", "validity_days": 30},
    {"name": "Pro", "credits": 200, "price": "$15", "validity_days": 30},
    {"name": "Unlimited-Day", "credits": 400, "price": "$30", "validity_days": 30},
]

USE_WEBHOOK = os.getenv("USE_WEBHOOK", "false").lower() == "true"
WEBHOOK_BASE_URL = os.getenv("WEBHOOK_BASE_URL", "")
PORT = int(os.getenv("PORT", "8000"))
