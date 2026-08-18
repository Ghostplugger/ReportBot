import os

BOT_TOKEN = os.environ.get("8874711768:AAEKxg9vMqhrxoatpKkh0iN9lhd-N0_E8ts")
API_ID = int(os.environ.get("38884525", 0))
API_HASH = os.environ.get("ffad13e71c9fcff37b5fef790ae0fda8")
OWNER_ID = int(os.environ.get("7380059056", 0))
MONGO_URL = os.environ.get("MONGO_URL")
DB_NAME = "startlove"

SUDO_USERS = []
if sudo_str := os.environ.get("SUDO_USERS"):
    SUDO_USERS = [int(x.strip()) for x in sudo_str.split(",") if x.strip().isdigit()]
