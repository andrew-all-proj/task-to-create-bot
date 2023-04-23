import logging
import aiohttp
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from create_bot import bot, Keyboards
from state import State_bot
from token_ import api_key_currency_convertor


async def meny_currency_convertor(message: types.Message):
    await State_bot.st_select_currency.set()
    await message.answer("Введите сумму в рублях", reply_markup=Keyboards.exit)


async def select_currency(message: types.Message,  state: FSMContext):
    await state.update_data({"amount": message.text})
    await State_bot.st_currency_convertor.set()
    await message.answer("Выберите в какую валюту конвертировать", reply_markup=Keyboards.currency)


async def currency_convertor(message: types.Message, state: FSMContext):
    base_url = "https://api.exchangeratesapi.io/latest"
    data = await state.get_data()
    async with aiohttp.ClientSession() as session:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={message.text}&amount={data['amount']}"
        headers = {
            "apikey": api_key_currency_convertor
        }
        async with session.get(url, headers=headers) as response:
            if response.status != 200:
                return await message.answer(f"Ошибка получения курсов валют", reply_markup=Keyboards.exit)
            data = await response.json()

    await State_bot.st_select_currency.set()
    await message.answer(f"{data['result']} {message.text}", reply_markup=Keyboards.exit)


def register_handler_currency_convertor(dp: Dispatcher):
    dp.register_message_handler(meny_currency_convertor, lambda message: message.text.lower() in ['конвертер валют'],
                                content_types=types.ContentType.TEXT, state='*')
    dp.register_message_handler(select_currency, lambda message: message.text.lower() not in ['выход'],
                                content_types=types.ContentType.TEXT, state=State_bot.st_select_currency)
    dp.register_message_handler(currency_convertor, lambda message: message.text.lower() not in ['выход'],
                                content_types=types.ContentType.TEXT, state=State_bot.st_currency_convertor)