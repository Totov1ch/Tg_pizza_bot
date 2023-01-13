import json
import string
from aiogram import Bot, types, Dispatcher
from aiogram import types
from create_bot import dp


@dp.message_handler(lambda message: 'taxi' in message.text)
async def taxi(message: types.Message):
    await message.answer("Taxi")


@dp.message_handler(lambda message: message.text.startswith('ololo'))
async def taxi(message: types.Message):
    await message.answer(message.text[6:])


# @dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == "Привет":
        await message.reply("Ты лох! И шутки твои тупые")
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply("Ты на кого материшься?")
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
