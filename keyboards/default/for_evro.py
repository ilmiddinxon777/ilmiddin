from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

evropa_button2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=" Grecks salat"),
            KeyboardButton(text="  XALIMU")
        ],
        [
            KeyboardButton(text=" PAELYA"),
            KeyboardButton(text=" PASTA karbonara")
        ],
        [
            KeyboardButton(text='Backward')
        ]
    ],
    resize_keyboard=True
)