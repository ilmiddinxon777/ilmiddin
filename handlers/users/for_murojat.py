from aiogram import types
from aiogram.dispatcher import FSMContext
from states.holatlar_eng import Forma1
from loader import dp,bot
from keyboards.default.for_drinks import tasdiqlash_buttons_eng
from keyboards.default.for_menu import menu_button_english





@dp.message_handler(text="Appeal to the admin")
async def bot_echo(message: types.Message):

    await message.answer(text="enter name")
    await Forma1.ism_qabul_qilish_eng.set()


@dp.message_handler(state=Forma1.ism_qabul_qilish_eng)
async def bot_echo(message: types.Message,state:FSMContext):
    name1 = message.text
    await state.update_data(({"name":name1}))
    await message.answer(text="Enter surname")
    await Forma1.familiya_qabul_qilish_eng.set()

@dp.message_handler(state=Forma1.familiya_qabul_qilish_eng)
async def bot_echo(message: types.Message,state:FSMContext):
    familiya1 = message.text
    await state.update_data(({"Surname":familiya1}))
    await message.answer(text="Enter age")
    await Forma1.yosh_qabul_qilish_eng.set()


@dp.message_handler(state=Forma1.yosh_qabul_qilish_eng)
async def bot_echo(message: types.Message,state:FSMContext):
    yoshi1 = message.text
    await state.update_data(({"age":yoshi1}))
    await message.answer(text="enter number")
    await Forma1.tel_qabul_qilish_eng.set()


@dp.message_handler(state=Forma1.tel_qabul_qilish_eng)
async def bot_echo(message: types.Message,state:FSMContext):
    nomeri1 = message.text
    await state.update_data(({"number":nomeri1}))
    await message.answer(text="Do you confirm the the appeal")
    await Forma1.murojaat_qabul_eng.set()


@dp.message_handler(state=Forma1.murojaat_qabul_eng)
async def bot_echo(message: types.Message,state:FSMContext):
    murojaat1 = message.text
    await state.update_data(({"text":murojaat1}))

    malumot_olish1 = await state.get_data()
    user_ismi1 = malumot_olish1.get("name")
    user_familiya1 = malumot_olish1.get("Surname")
    user_yoshi1 = malumot_olish1.get("age")
    user_nomeringiz1 = malumot_olish1.get("number")
    user_murojaatingiz1 = malumot_olish1.get("text")
    matn = f"Name : {user_ismi1}\n" \
           f"Surname : {user_familiya1}\n" \
           f"Age : {user_yoshi1}\n" \
           f"Number : {user_nomeringiz1}\n" \
           f"Appeal :\n\n{user_murojaatingiz1}"
    usr_id = message.from_user.id
    await bot.send_message(chat_id=usr_id,text=matn,reply_markup=tasdiqlash_buttons_eng)
    await Forma1.tastq_qabul_qilish_eng.set()



@dp.message_handler(state=Forma1.tastq_qabul_qilish_eng,text='Agree')
async def bot_echo(message: types.Message,state:FSMContext):
    malumot_olish1 = await state.get_data()
    user_ismi1 = malumot_olish1.get("name")
    user_familiya1 = malumot_olish1.get("Surname")
    user_yoshi1 = malumot_olish1.get("age")
    user_nomeringiz1 = malumot_olish1.get("number")
    user_murojaatingiz = malumot_olish1.get("text")
    username = message.from_user.username
    matn = f"this user {username}" \
           f"Name : {user_ismi1}\n" \
           f"Surname : {user_familiya1}\n" \
           f"Age : {user_yoshi1}\n" \
           f"Nubmer : {user_nomeringiz1}\n" \
           f" Appeal :\n\n{user_murojaatingiz}"
    await bot.send_message(chat_id="1187539994",text=matn)
    await bot.send_message(chat_id="5928251626",text=matn)
    await message.answer(text="Appeal to the admin",reply_markup=menu_button_english)
    await state.finish()

@dp.message_handler(state=Forma1.tastq_qabul_qilish_eng, text='Cancel')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text="canceled message ",reply_markup=menu_button_english)
    await state.finish()
