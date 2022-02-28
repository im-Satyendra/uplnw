
from config import Config
from database.database import Database

clintob = Database(Config.DATABASE_URL, "banned")
