import logging
import aiohttp
from aiogram import types, Dispatcher
from create_bot import bot, Keyboards
from state import State_bot


async def welcome(message: types.Message):
    await State_bot.st_main.set()
    await message.answer("Привет! Что бы ты хотел сделать?", reply_markup=Keyboards.main_meny)


def register_handler_main_meny(dp: Dispatcher):
    dp.register_message_handler(welcome, state='*',
                                content_types=types.ContentType.TEXT)
