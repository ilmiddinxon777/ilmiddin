from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

ichimliklar_button2 = ReplyKeyboardMarkup(
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
            KeyboardButton(text='Backward')
        ]
    ],
    resize_keyboard=True
)



tasdiqlash_buttons_eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Agree"),
            KeyboardButton(text="Cancel")
        ]
    ],
    resize_keyboard=True
)