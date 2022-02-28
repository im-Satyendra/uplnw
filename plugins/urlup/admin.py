
from pyrogram import Client as Clinton
from pyrogram import filters
from config import Config
from database.user import clinton
from database.banned import clintob
from database.banuser import BanUser
from plugins.urlup.buttons import *
@Clinton.on_message(filters.private & filters.command('total'))
async def sts(c, m):
    if m.from_user.id != Config.OWNER_ID:
        return 
    all_users = await clinton.get_all_users()
    total_users = await clinton.total_users_count()
    allb_users = await clintob.get_all_users()
    totalb_users = await clintob.total_users_count()
    h="""total users {}
    totalusers count {}
    bannedusers {}
    banneduserscount {}
    """
    await m.reply_text(text=h.format(all_users,total_users,allb_users,totalb_users), quote=True)


@Clinton.on_message(filters.private & filters.command("search"))
async def serc(bot, update):

      await bot.send_message(chat_id=update.chat.id, text="🔍 TORRENT SEARCH", 
      parse_mode="html", reply_markup=Button.BUTTONS01)
@Clinton.on_message(filters.private & filters.command(["ban"]))
async def ban(bot, update):
    if update.from_user.id != Config.OWNER_ID:
        return 
    await BanUser(bot, update)
    all_users = await clinton.get_all_users()
    total_users = await clinton.total_users_count()
    allb_users = await clintob.get_all_users()
    totalb_users = await clintob.total_users_count()
    h="""total users {}
    totalusers count {}
    bannedusers {}
    banneduserscount {}
    """
    await update.reply_text(text=h.format(all_users,total_users,allb_users,totalb_users), quote=True)