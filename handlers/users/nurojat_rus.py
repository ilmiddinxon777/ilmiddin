from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.для_мeню import menu_button1
from states.holatlar_rus import Forma2
from loader import dp,bot
from keyboards.default.для_блюд import tasdiqlash_buttons_rus






@dp.message_handler(text="Обрашение к админу")
async def bot_echo(message: types.Message):

    await message.answer(text="введите  имя")
    await Forma2.ism_qabul_qilish_rus.set()


@dp.message_handler(state=Forma2.ism_qabul_qilish_rus)
async def bot_echo(message: types.Message,state:FSMContext):
    name2 = message.text
    await state.update_data(({"имя":name2}))
    await message.answer(text="введите фамилию")
    await Forma2.familiya_qabul_qilish_rus.set()

@dp.message_handler(state=Forma2.familiya_qabul_qilish_rus)
async def bot_echo(message: types.Message,state:FSMContext):
    familiya2 = message.text
    await state.update_data(({"фамилия":familiya2}))
    await message.answer(text="введите свой возраст")
    await Forma2.yosh_qabul_qilish_rus.set()


@dp.message_handler(state=Forma2.yosh_qabul_qilish_rus)
async def bot_echo(message: types.Message,state:FSMContext):
    yoshi2 = message.text
    await state.update_data(({"возраст":yoshi2}))
    await message.answer(text="введите номер")
    await Forma2.tel_qabul_qilish_rus.set()


@dp.message_handler(state=Forma2.tel_qabul_qilish_rus)
async def bot_echo(message: types.Message,state:FSMContext):
    nomeri2 = message.text
    await state.update_data(({"номер":nomeri2}))
    await message.answer(text="Вы подтверждаете обращению")
    await Forma2.murojaat_qabul_rus.set()


@dp.message_handler(state=Forma2.murojaat_qabul_rus)
async def bot_echo(message: types.Message,state:FSMContext):
    murojaat2 = message.text
    await state.update_data(({"обращение":murojaat2}))

    malumot_olish1 = await state.get_data()
    user_ismi1 = malumot_olish1.get("имя")
    user_familiya1 = malumot_olish1.get("фамилия")
    user_yoshi1 = malumot_olish1.get("лет")
    user_nomeringiz1 = malumot_olish1.get("номер")
    user_murojaatingiz1 = malumot_olish1.get("обращение")
    matn = f"имя : {user_ismi1}\n" \
           f"фамилия : {user_familiya1}\n" \
           f"возраст: {user_yoshi1}\n" \
           f"номер: {user_nomeringiz1}\n" \
           f"обращение :\n\n{user_murojaatingiz1}"
    usr_id = message.from_user.id
    await bot.send_message(chat_id=usr_id,text=matn,reply_markup=tasdiqlash_buttons_rus)
    await Forma2.tastq_qabul_qilish_rus.set()

@dp.message_handler(state=Forma2.tastq_qabul_qilish_rus, text="отправить")
async def bot_echo(message: types.Message,state:FSMContext):
    malumot_olish1 = await state.get_data()
    user_ismi1 = malumot_olish1.get("имя")
    user_familiya1 = malumot_olish1.get("фамилия")
    user_yoshi1 = malumot_olish1.get("возраст")
    user_nomeringiz1 = malumot_olish1.get("номер")
    user_murojaatingiz = malumot_olish1.get("обращение")
    username = message.from_user.username
    matn = f"этот пользователь {username}" \
           f"имя: {user_ismi1}\n" \
           f"фамилия : {user_familiya1}\n" \
           f"возраст: {user_yoshi1}\n" \
           f"номер: {user_nomeringiz1}\n" \
           f" обращение :\n\n{user_murojaatingiz}"
    await bot.send_message(chat_id="1187539994",text=matn)
    await bot.send_message(chat_id="5928251626",text=matn)
    await message.answer(text="отправленно к админстратору",reply_markup=menu_button1)
    await state.finish()

@dp.message_handler(state=Forma2.murojaat_qabul_rus, text="отменить")
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text="отменить",reply_markup=menu_button1)
    await state.finish()