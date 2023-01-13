from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton("/Режим_работы")
b2 = KeyboardButton("/Расположение")
b3 = KeyboardButton("/Меню")
# b4 = KeyboardButton("/Номер", request_contact=True)
# b5 = KeyboardButton("/Где_я", request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2, b3)
