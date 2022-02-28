from pyrogram import Client
from plugins.urlup.database.banned import clinton
from pyrogram.types import Message


async def BanUser(bot: Client, update: Message):
    if not await clinton.is_user_exist(update.from_user.id):
           await clinton.add_user(update.from_user.id)
