from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU


router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])

# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])