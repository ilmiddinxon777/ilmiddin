from aiogram import types
from aiogram.dispatcher import FSMContext

from states.holatlar import Forma
from loader import dp,bot
from keyboards.default.taomlar_uchun import tasdiqlash_buttons
from keyboards.default.menu_uchun import menu_button


@dp.message_handler(text="Adminga murojat")
async def bot_echo(message: types.Message):

    await message.answer(text="Ismni kiriting")
    await Forma.ism_qabul_qilish.set()


@dp.message_handler(state=Forma.ism_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    ism = message.text
    await state.update_data(({"ismingiz":ism}))
    await message.answer(text="Familiyangiz kiriting")
    await Forma.familiya_qabul_qilish.set()

@dp.message_handler(state=Forma.familiya_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    familiya = message.text
    await state.update_data(({"familiyangiz":familiya}))
    await message.answer(text="Yoshni kiriting kiriting")
    await Forma.yosh_qabul_qilish.set()


@dp.message_handler(state=Forma.yosh_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    yoshi = message.text
    await state.update_data(({"yoshi":yoshi}))
    await message.answer(text="Telefon raqamni  kiriting kiriting")
    await Forma.tel_qabul_qilish.set()


@dp.message_handler(state=Forma.tel_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    nomeri = message.text
    await state.update_data(({"nomeringiz":nomeri}))
    await message.answer(text="Murojaatni kiriting kiriting kiriting")
    await Forma.murojaat_qabul.set()


@dp.message_handler(state=Forma.murojaat_qabul)
async def bot_echo(message: types.Message,state:FSMContext):
    murojaat = message.text
    await state.update_data(({"text":murojaat}))

    malumot_olish = await state.get_data()
    user_ismi = malumot_olish.get("ismingiz")
    user_familiya = malumot_olish.get("familiyangiz")
    user_yoshi = malumot_olish.get("yoshi")
    user_nomeringiz = malumot_olish.get("nomeringiz")
    user_murojaatingiz = malumot_olish.get("text")
    matn = f"Ism : {user_ismi}\n" \
           f"Familiya : {user_familiya}\n" \
           f"Yosh : {user_yoshi}\n" \
           f"Nomer : {user_nomeringiz}\n" \
           f" Murojat :\n\n{user_murojaatingiz}"
    usr_id = message.from_user.id
    await bot.send_message(chat_id=usr_id,text=matn,reply_markup=tasdiqlash_buttons)
    await Forma.tastq_qabul_qilish.set()



@dp.message_handler(state=Forma.tastq_qabul_qilish,text='Tasdiqlash')
async def bot_echo(message: types.Message,state:FSMContext):
    malumot_olish = await state.get_data()
    user_ismi = malumot_olish.get("ismingiz")
    user_familiya = malumot_olish.get("familiyangiz")
    user_yoshi = malumot_olish.get("yoshi")
    user_nomeringiz = malumot_olish.get("nomeringiz")
    user_murojaatingiz = malumot_olish.get("text")
    username = message.from_user.username
    matn = f"Ushbu foydalanuvchi {username}" \
           f"Ism : {user_ismi}\n" \
           f"Familiya : {user_familiya}\n" \
           f"Yosh : {user_yoshi}\n" \
           f"Nomer : {user_nomeringiz}\n" \
           f" Murojat :\n\n{user_murojaatingiz}"
    await bot.send_message(chat_id="1187539994",text=matn)
    await bot.send_message(chat_id="5928251626",text=matn)
    await message.answer(text="Adminga yuborildi",reply_markup=menu_button)
    await state.finish()

    @dp.message_handler(state=Forma.tastq_qabul_qilish, text='Bekor qilish',)
    async def bot_echo(message: types.Message, state: FSMContext):
        await message.answer(text="Bekor qilindi",reply_markup=menu_button)
        await state.finish()
