from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

shirinliklar_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="  TORT SNICKERS"),
            KeyboardButton(text="  MEDOVOY TORT")
        ],
        [
            KeyboardButton(text="  NAPALION TORT"),
            KeyboardButton(text="  QAYMOQLI TORT")
        ],
        [
            KeyboardButton(text='Ortga')
        ]
    ],
    resize_keyboard=True
)