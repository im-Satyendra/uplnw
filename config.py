import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = "2124088863:AAGPhAjBec8pUGTEKJOpsGErxmnVQb__Ook"
    # The Telegram API things
    API_ID = 2171111
    API_HASH = "fd7acd07303760c52dcc0ed8b2f73086"
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 2097152000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 2097152000    
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = 1089528685
    SESSION_NAME = "UPLOADER"
    # database uri (mongodb)
    DATABASE_URL = "mongodb+srv://satya:s4tya@cluster0.rrqhs.mongodb.net/utyfky?retryWrites=true&w=majority"
    MAX_RESULTS = "50"
