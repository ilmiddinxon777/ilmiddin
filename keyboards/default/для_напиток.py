from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

ichimliklar_button1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="  COCA-COLA 1л"),
            KeyboardButton(text="  PEPSI 1л")
        ],
        [
            KeyboardButton(text="  ARK TEA 1л"),
            KeyboardButton(text="  DENA 1л")
        ],
        [
            KeyboardButton(text='НАЗАД')
        ]
    ],
    resize_keyboard=True
)