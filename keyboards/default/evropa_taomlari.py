import traceback

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

evropa_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=" Grecheskiy salat"),
            KeyboardButton(text="  Xalimu")
        ],
        [
            KeyboardButton(text=" Paelya"),
            KeyboardButton(text=" Pasta karbonara")
        ],
        [
            KeyboardButton(text='Ortga')
        ]
    ],
    resize_keyboard=True
)