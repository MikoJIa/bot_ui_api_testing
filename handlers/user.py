import os

from aiogram.types import Message, FSInputFile
from aiogram import Router
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from lexicon.about import about_my_self
import logging
from pathlib import Path


log_dir = Path('logs')
log_dir.mkdir(exist_ok=True)

# Создаём логгер
logger = logging.getLogger('bot')
logger.setLevel(logging.DEBUG)

# Хендлер для файла
file_handler = logging.FileHandler(log_dir / 'bot.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Хендлер для консоли
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def start_command(message: Message):
    logger.info(f"User {message.from_user.id} started command")
    await message.answer(text=LEXICON_RU['/start'])

# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def help_command(message: Message):
    logger.info(f"User {message.from_user.id} pressed the help command")
    await message.answer(text=LEXICON_RU['/help'])


# Этот хэндлер генерирует логи событий и отвечает на команду /getlogs
@router.message(Command(commands='getlogs'))
async def get_logs(message: Message):
    logger.info(f"User {message.from_user.id} pressed the get logs command")
    try:
        log_file = Path('logs') / 'bot.log'
        # Проверяем существование файла логов
        if not log_file.exists():
            await message.answer("Файл логов не найден")
            return


        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            last_lines = lines[-30:] if len(lines) > 30 else lines

        log_text = ''.join(last_lines)

        if not log_text.strip():
            await message.answer("📭 Логи пусты")
            return

        # Отправляем
        if len(log_text) > 0:
            await message.answer(
                f"📋 **Последние логи:**\n```\n{log_text[-4000:]}\n```",
                parse_mode="Markdown"
            )
        else:
            parts = [log_text[i:i + 4000] for i in range(0, len(log_text), 4000)]
            for i, part in enumerate(parts, 1):
                await message.answer(
                    f"📋 **Логи (часть {i}/{len(parts)}):**\n```\n{part}\n```",
                    parse_mode="Markdown"
                )
    except Exception as e:
        logger.error(f"Error in get_logs: {e}")
        await message.answer(f"❌ Ошибка: {str(e)}")


@router.message(Command(commands='aboutmyself'))
async def about_myself(message: Message):
    logger.info(f"User {message.from_user.id} pressed the about my self")
    await message.answer(about_my_self)