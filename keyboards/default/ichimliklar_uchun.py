from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

ichimliklar_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="  COCA-COLA 1l"),
            KeyboardButton(text="  PEPSI 1l")
        ],
        [
            KeyboardButton(text="  ARK TEA 1l"),
            KeyboardButton(text="  DENA 1l")
        ],
        [
            KeyboardButton(text='Ortga')
        ]
    ],
    resize_keyboard=True
)