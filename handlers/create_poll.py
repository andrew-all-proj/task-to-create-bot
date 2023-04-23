import logging
import aiohttp
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from create_bot import bot, Keyboards, dp
from state import State_bot


async def meny_poll(message: types.Message):
    await State_bot.st_create_poll.set()
    await message.answer("Какой вопрос вы хотите задать в опросе?", reply_markup=Keyboards.exit)


async def create_question(message: types.Message, state: FSMContext):
    await state.update_data({"question": message.text})
    await State_bot.st_create_answer.set()
    await message.answer("Какие варианты ответов вы хотите предложить (разделяйте их запятыми)?",
                         reply_markup=Keyboards.exit)

async def create_answer(message: types.Message, state: FSMContext):
    data = await state.get_data()
    poll = types.Poll(
        question=data["question"],
        options=message.text.split(","),
        is_anonymous=False
    )
    await bot.send_poll(message.from_user.id, question=poll.question, options=poll.options, is_anonymous=poll.is_anonymous)


def register_handler_create_poll(dp: Dispatcher):
    dp.register_message_handler(meny_poll, lambda message: message.text.lower() in ["опрос"],
                                content_types=types.ContentType.TEXT, state='*')
    dp.register_message_handler(create_question, lambda message: message.text.lower() not in ['выход'],
                                content_types=types.ContentType.TEXT, state=State_bot.st_create_poll)
    dp.register_message_handler(create_answer, lambda message: message.text.lower() not in ['выход'],
                                content_types=types.ContentType.TEXT, state=State_bot.st_create_answer)