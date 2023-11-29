from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

evropa_button1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=" Греческий салат"),
            KeyboardButton(text="  Xaлиму")
        ],
        [
            KeyboardButton(text=" Пaэлья"),
            KeyboardButton(text=" Паста Карбонара")
        ],
        [
            KeyboardButton(text='НАЗАД')
        ]
    ],
    resize_keyboard=True
)