from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создаем клавиатуру для выбора языка
language_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
language_keyboard.add(
    KeyboardButton("Қазақша"),
    KeyboardButton("Русский"),
    KeyboardButton("English")
)

