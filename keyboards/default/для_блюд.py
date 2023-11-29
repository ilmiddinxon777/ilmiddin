from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

taom_button1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=" Плов "),
            KeyboardButton(text=" Шашлык")
        ],
        [
            KeyboardButton(text=" Суп"),
            KeyboardButton(text="  Самсы")
        ],
        [
            KeyboardButton(text='НАЗАД')
        ]
    ],
    resize_keyboard=True
)

tasdiqlash_buttons_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="отправить"),
            KeyboardButton(text="отменить")
        ]
    ],
    resize_keyboard=True
)