import logging
import aiohttp
from aiogram import types, Dispatcher
from create_bot import bot, Keyboards
from state import State_bot


async def meny_weather(message: types.Message):
    await State_bot.st_get_weather.set()
    await message.answer("Введите название города:", reply_markup=Keyboards.exit)


async def get_weather(message: types.Message):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": message.text, "appid": api_key_weather, "units": "metric"}
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url, params=params) as response:
            data = await response.json()

    if data["cod"] != 200:
        return await message.answer(f"Название города введено неверно", reply_markup=Keyboards.exit)

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    await message.answer(f"{message.text}: {weather}, {temp}°C (Ощущается {feels_like}°C)", reply_markup=Keyboards.exit)


def register_handler_weather(dp: Dispatcher):
    dp.register_message_handler(meny_weather, lambda message: message.text.lower() in ['погода'],
                                content_types=types.ContentType.TEXT, state='*')
    dp.register_message_handler(get_weather, lambda message: message.text.lower() not in ['выход'],
                                content_types=types.ContentType.TEXT, state=State_bot.st_get_weather)