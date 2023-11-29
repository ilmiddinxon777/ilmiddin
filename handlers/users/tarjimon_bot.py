from aiogram import types
from googletrans import Translator
from loader import dp

tarlimon = Translator()

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    till = tarlimon.detect(text=message.text).lang
    if till =='uz':
        tarjimo_qilish = tarlimon.translate(text=message.text,dest='en',src='uz').text
        await message.answer(text=tarjimo_qilish)
    if till =='en':
        tarjimo_qilish = tarlimon.translate(text=message.text,dest='uz',src='en').text
        await message.answer(text=tarjimo_qilish)
    if till =='ru':
        tarjimo_qilish = tarlimon.translate(text=message.text,dest='en',src='ru').text
        await message.answer(text=tarjimo_qilish)
    if till =='en':
        tarjimo_qilish = tarlimon.translate(text=message.text,dest='ru',src='en').text
        await message.answer(text=tarjimo_qilish)
    if till =='ru':
        tarjimo_qilish = tarlimon.translate(text=message.text,dest='uz',src='ru').text
        await message.answer(text=tarjimo_qilish)
    if till =='uz':
        tarjimo_qilish = tarlimon.translate(text=message.text,dest='ru',src='uz').text
        await message.answer(text=tarjimo_qilish)