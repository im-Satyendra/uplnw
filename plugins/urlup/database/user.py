
from config import Config
from plugins.urlup.database.database import Database

clinton = Database(Config.DATABASE_URL, "user")
