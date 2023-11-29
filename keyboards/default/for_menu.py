from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


menu_button_english = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=" MEALS"),
            KeyboardButton(text="  DRINKS "),
        ],
        [
            KeyboardButton(text=" EVRO NATIONAL MEALS")
        ],
        [
            KeyboardButton(text=" DESSERT"),
            KeyboardButton(text="  TURKISH NATIONAL MEALS"),
        ],
        [
            KeyboardButton(text="Location",request_location=True),
            KeyboardButton(text="Contact",request_contact=True)
        ],
        [
            KeyboardButton(text="Choose a new language"),
            KeyboardButton(text="Appeal to the admin")
        ]
    ],
    resize_keyboard=True
)