from aiogram.filters import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import Message
from aiogram import Router
from lexicon.names_button import title_buttons


router = Router()

# Методом as_markup() передаём клавиатуру как аргумент туда, где она требуется:
@router.message(Command(commands='keyboard'))
async def keyboard_building(message: Message):
    # Инициализируем билдер
    kb_builder = ReplyKeyboardBuilder()
    # Создаём первый список с кнопками
    buttons = [KeyboardButton(text=f'{title_buttons[i]}') for i in range(5)]
    # Распаковываем список с кнопками методом add
    kb_builder.add(*buttons)
    # Явно сообщаем билдеру сколько хотим видеть кнопок в 1-м и 2-м рядах
    kb_builder.adjust(1, 2)
    await message.answer(
        text="Воттакая получается клавиатура",
        reply_markup=kb_builder.as_markup(resize_keyboard=True)
    )
