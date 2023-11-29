from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from keyboards.default.menu_uchun import menu_button
from keyboards.default.taomlar_uchun import taomlar_button
from keyboards.default.shirinliklar_uchun import shirinliklar_button
from keyboards.default.ichimliklar_uchun import ichimliklar_button
from keyboards.default.turk_uchun import turk_button
from keyboards.default.evropa_taomlari import evropa_button
from keyboards.inline.tillar_uchun import till_button
from keyboards.default.для_мeню import menu_button1
from keyboards.default.для_блюд import taom_button1
from keyboards.default.для_слад import shirinliklar_button1
from keyboards.default.для_евро import evropa_button1
from keyboards.default.для_напиток import ichimliklar_button1
from keyboards.default.для_тюрк import turk_button1
from keyboards.default.for_menu import menu_button_english
from keyboards.default.for_meals import taomlar_button2
from keyboards.default.for_drinks import ichimliklar_button2
from keyboards.default.for_desert import shirinliklar_button2
from keyboards.default.for_evro import evropa_button2
from keyboards.default.for_turk import turk_button2
from loader import dp
from filters.shaxsiy_uchun import Shaxsiy

@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=till_button)


@dp.callback_query_handler(text="til1")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Assalomu alaykum magig restauran botiga xush kelibsiz",reply_markup=menu_button)


@dp.message_handler(text='Ortga')
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Buyurtmangiz qabul qilindi operator telefonini kutung, {xabar.from_user.full_name}!",reply_markup=menu_button)

@dp.message_handler(text='TAOMLAR')
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum magig restauran botiga xush kelibsiz",reply_markup=taomlar_button)

@dp.message_handler(text='Ortga')
async def bot_start(message: types.Message):
    await message.answer(f"Buyurtmangiz qabul qilindi operator telefonini kutung, {message.from_user.full_name}!",reply_markup=menu_button)

@dp.message_handler(text='shrinliklar')
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum magig restauran botiga xush kelibsiz",reply_markup=shirinliklar_button)

@dp.message_handler(text='Ortga')
async def bot_start(message: types.Message):
    await message.answer(f"Buyurtmangiz qabul qilindi operator telefonini kutung, {message.from_user.full_name}!",reply_markup=menu_button)

@dp.message_handler(text='ICHIMLIKAR')
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum magig restauran botiga xush kelibsiz",reply_markup=ichimliklar_button)

@dp.message_handler(text='Ortga')
async def bot_start(message: types.Message):
    await message.answer(f"SBuyurtmangiz qabul qilindi operator telefonini kutung, {message.from_user.full_name}!", reply_markup=menu_button)


@dp.message_handler(text='TURK TAOMLARI')
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum magig restauran botiga xush kelibsiz",reply_markup=turk_button)

@dp.message_handler(text='Ortga')
async def bot_start(message: types.Message):
    await message.answer(f"Buyurtmangiz qabul qilindi operator telefonini kutung, {message.from_user.full_name}!",reply_markup=menu_button)

@dp.message_handler(text='EVROPA MILLIY TAOMLARI')
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum magig restauran botiga xush kelibsiz",reply_markup=evropa_button)

@dp.message_handler(text='Ortga')
async def bot_start(message: types.Message):
    await message.answer(f"Buyurtmangiz qabul qilindi operator telefonini kutung, {message.from_user.full_name}!", reply_markup=menu_button)

@dp.callback_query_handler(text="til3")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Здраствуйте вас приветсвуйут ресторан magig " ,reply_markup=menu_button1)

@dp.message_handler(text='НАЗАД')
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Ваш заказ принять дождитесь звонка оператора, {xabar.from_user.full_name}!",reply_markup=menu_button1)


@dp.message_handler(text='БЛЮДЫ')
async def bot_start(message: types.Message):
    await message.answer(f"Здраствуйте вас приветсвуйут ресторан magig",reply_markup=taom_button1)


@dp.message_handler(text='НАЗАД')
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Ваш заказ принять дождитесь звонка оператора, {xabar.from_user.full_name}!",reply_markup=menu_button1)


@dp.message_handler(text='СЛАДОСТИ')
async def bot_start(message: types.Message):
    await message.answer(f"Здраствуйте вас приветсвуйут ресторан magig",reply_markup=shirinliklar_button1)


@dp.message_handler(text='НАЗАД')
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Ваш заказ принять дождитесь звонка оператора, {xabar.from_user.full_name}!",reply_markup=menu_button1)

@dp.message_handler(text='ЕВРОПЕЙСКИЕ БЛЮДЫ')
async def bot_start(message: types.Message):
    await message.answer(f"Здраствуйте вас приветсвуйут ресторан magig",reply_markup=evropa_button1)


@dp.message_handler(text='НАЗАД')
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Ваш заказ принять дождитесь звонка оператора, {xabar.from_user.full_name}!",reply_markup=menu_button1)


@dp.message_handler(text='НАПИТКИ')
async def bot_start(message: types.Message):
    await message.answer(f"Здраствуйте вас приветсвуйут ресторан magig",reply_markup=ichimliklar_button1)


@dp.message_handler(text='НАЗАД')
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Ваш заказ принять дождитесь звонка оператора, {xabar.from_user.full_name}!",reply_markup=menu_button1)


@dp.message_handler(text='ТУРЕТСКИЕ БЛЮДЫ')
async def bot_start(message: types.Message):
    await message.answer(f"Здраствуйте вас приветсвуйут ресторан magig",reply_markup=turk_button1)


@dp.callback_query_handler(text="til2")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Hello and welcome to magig restauran bot",reply_markup=menu_button_english)


@dp.message_handler(text='Backward')
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Accept your order wait for the operator to call, {xabar.from_user.full_name}!",reply_markup=menu_button_english)


@dp.message_handler(text="MEALS")
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Hello and welcome to magig restauran bot",reply_markup=taomlar_button2)


@dp.message_handler(text='Backward')
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Accept your order wait for the operator to call, {xabar.from_user.full_name}!",reply_markup=menu_button_english)


@dp.message_handler(text="DRINKS")
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Hello and welcome to magig restauran bot",reply_markup=ichimliklar_button2)

@dp.message_handler(text='Backward')
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Accept your order wait for the operator to call, {xabar.from_user.full_name}!",reply_markup=menu_button_english)


@dp.message_handler(text="DESSERT")
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Hello and welcome to magig restauran bot",reply_markup=shirinliklar_button2)


@dp.message_handler(text='Backward')
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Accept your order wait for the operator to call, {xabar.from_user.full_name}!",reply_markup=menu_button_english)


@dp.message_handler(text="EVRO NATIONAL MEALS")
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Hello and welcome to magig restauran bot",reply_markup=evropa_button2)


@dp.message_handler(text='Backward')
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Accept your order wait for the operator to call, {xabar.from_user.full_name}!",reply_markup=menu_button_english)


@dp.message_handler(text="TURKISH NATIONAL MEALS")
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Hello and welcome to magig restauran bot",reply_markup=turk_button2)


@dp.message_handler(text='Backward')
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Accept your order wait for the operator to call, {xabar.from_user.full_name}!",reply_markup=menu_button_english)

@dp.message_handler(text='Boshqa tilni tanlash')
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Yangi tillni tanlash bosh menusi ",reply_markup=till_button)

@dp.message_handler(text='Вибырите другой язык')
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Главный меню выбира языка",reply_markup=till_button)


@dp.message_handler(text='Choose a new language')
async def bot_start(xabar: types.Message):
    await xabar.answer(f"Main language selection menu",reply_markup=till_button)



