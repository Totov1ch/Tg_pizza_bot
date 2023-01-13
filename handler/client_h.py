from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
from data_base import sqlite_db
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


# ''' CLIENT '''
# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Жрите не обляпойтесь", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Раз на раз в личке давай выскочим?\nhttps://t.me/Pizza_AntoBot")


# @dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')


# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная 15')


async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=["start", "help"])
    dp.register_message_handler(pizza_open_command, commands=["Режим_работы"])
    dp.register_message_handler(pizza_place_command, commands=["Расположение"])
    dp.register_message_handler(pizza_menu_command, commands=["Меню"])
