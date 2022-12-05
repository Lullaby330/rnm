 import os

class Config(object):    
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("5880563885:AAHf0Fi8x_iNDfHmpL0y03KO3sUxnn_ZlE0")

    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("6216349"))

    API_HASH = os.environ.get("5c7418e9f3df6db931caa7354521c55f")

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1823080600").split())

    # Channels to forward the formatted video (Optional, Prefix: "-100", Bot should be an admin of the channels)
    CHANNEL1_ID = os.environ.get("-1001854758671")

    CHANNEL1_NAME = os.environ.get("File Renamer")

    CHANNEL2_ID = os.environ.get("CHANNEL2_ID")

    CHANNEL2_NAME = os.environ.get("CHANNEL2_NAME")

    CHANNEL3_ID = os.environ.get("CHANNEL3_ID")

    CHANNEL3_NAME = os.environ.get("CHANNEL3_NAME")

    CHANNEL4_ID = os.environ.get("CHANNEL4_ID")

    CHANNEL4_NAME = os.environ.get("CHANNEL4_NAME")

    CHANNEL5_ID = os.environ.get("CHANNEL5_ID")

    CHANNEL5_NAME = os.environ.get("CHANNEL5_NAME")
