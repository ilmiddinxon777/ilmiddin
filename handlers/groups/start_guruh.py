from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp
from filters.guruh_uchun import Guruh

@dp.message_handler(Guruh,CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu aleykum 🥰 bizning gruppamizga xush kelibsiz , {message.from_user.full_name}!")