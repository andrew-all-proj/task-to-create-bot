from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from token_ import token_

API_TOKEN = token_
bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Keyboards():
    main_meny = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Погода", "Конвертер валют", "Случайная картинка", "Опрос"]
    main_meny.add(*buttons)

    currency = types.ReplyKeyboardMarkup(resize_keyboard=True)
    currency.add("USD", "EUR", "CNY", "Выход")

    random_picture = types.ReplyKeyboardMarkup(resize_keyboard=True)
    random_picture.row("картинка")
    random_picture.row("выход")

    exit = types.ReplyKeyboardMarkup(resize_keyboard=True)
    exit.row('Выход')

