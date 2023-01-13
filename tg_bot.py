from aiogram.utils import executor
from create_bot import dp
from handler import client_h, admin_h, other_h
from data_base import sqlite_db


async def on_startup(_):
    print("Online")
    sqlite_db.sql_start()

client_h.register_handlers_client(dp)
admin_h.register_handlers_admin(dp)
other_h.register_handlers_other(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
