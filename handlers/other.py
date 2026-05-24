from aiogram.types import Message
from create_dp import dp
from lexicon.lexicon import LEXICON_RU
from aiogram import Router


router = Router()

# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start", "/help", '/aboutmyself', '/runapitests', '/runuitests'
@router.message()
async def another_messages(message: Message):
    if message.text not in ['/help', '/start', '/aboutmyself', '/runapitests', '/runuitests', '/keyboard']:
        response = (
            f"Я не знаю такую команду {message.text}\n"
            f"Доступные команды:\n"
            f"/start - Бот подскажет что он может делать\n"
            f"/help - Бот подскажет команды которыми можно пользоватся\n"
            f"Или нажмите кнопку 'Menu'"
        )
    else:
        response = "Извините, я понимаю только текстовые команды. Попробуйте /help"
    await message.answer(response)