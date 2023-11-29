from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


till_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek tili",callback_data="til1"),
            InlineKeyboardButton(text="Inglis tili",callback_data="til2"),
        ],
        [
            InlineKeyboardButton(text="Russ tili",callback_data="til3")
        ],
        [
            InlineKeyboardButton(text="HAMKORLARIMIZ",url='https://t.me/ehrasg'),
            InlineKeyboardButton(text="Ulashish",switch_inline_query='Bu judayam foydali bot')
        ]
    ]
)