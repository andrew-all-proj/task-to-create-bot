import aiohttp
from aiogram import types, Dispatcher
from aiogram import types, Dispatcher

from create_bot import Keyboards, bot
from state import State_bot


async def meny_random_picture(message: types.Message):
    await State_bot.st_random_picture.set()
    await message.answer("отправить случайную картинку:", reply_markup=Keyboards.random_picture)


async def get_random_picture(message: types.Message):
    await State_bot.st_random_picture.set()
    async with aiohttp.ClientSession() as session:
        url = f"https://meow.senither.com/v1/random"
        async with session.get(url) as response:
            if response.status != 200:
                return await message.answer(f"Ошибка получения котика", reply_markup=Keyboards.exit)
            data = await response.json()
    await bot.send_photo(chat_id=message.chat.id, photo=data['data']['url'])  #


def register_handler_random_picture(dp: Dispatcher):
    dp.register_message_handler(meny_random_picture, lambda message: message.text.lower() in ['случайная картинка'],
                                content_types=types.ContentType.TEXT, state='*')
    dp.register_message_handler(get_random_picture, lambda message: message.text.lower() not in ['выход'],
                                content_types=types.ContentType.TEXT, state=State_bot.st_random_picture)
