
from config import Config
from plugins.urlup.database.database import Database

clintob = Database(Config.DATABASE_URL, "banned")
