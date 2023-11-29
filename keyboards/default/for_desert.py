from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

shirinliklar_button2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="  CAKES SNICKERS"),
            KeyboardButton(text="  MEDOVOY CAKES")
        ],
        [
            KeyboardButton(text="  NAPALION CAKES"),
            KeyboardButton(text="  CREAMY CAKES")
        ],
        [
            KeyboardButton(text='Backward')
        ]
    ],
    resize_keyboard=True
)