import os

class Config(object):

    API_ID = int(os.environ.get("API_ID", ""))

    API_HASH = str(os.environ.get("API_HASH", ""))

    BOT_TOKEN = str(os.environ.get("BOT_TOKEN", ""))
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "7158245271"))

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6405622540 6529179563").split())

    START = str(os.environ.get("START_TEXT", "wassup testing"))

    HELP = str(os.environ.get("HELP_TEXT", "help test"))

    DONATE = str(os.environ.get("DONATE_TEXT", "donation test"))

    DONATE_LINK = str(os.environ.get("DONATE_LINK", "https://t.me/Titan_Cinemas"))

    UPDATE_CHANNEL = str(os.environ.get("UPDATE_CHANNEL", "https://t.me/Titan_Cinemas"))

    SUPPORT_GROUP = str(os.environ.get("SUPPORT_GROUP", "https://t.me/Titan_Cinemas"))

    DB_URL = str(os.environ.get("DB_URL", ""))
    
    DB_NAME = str(os.environ.get("DB_NAME", "Cluster0"))
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))

