import asyncio
import logging
from pathlib import Path

from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from create_dp import dp
from handlers import user, other, keyboard, test_runner, allure_report_process


# Функция конфигурирования и запуска бота
async def main(dp: Dispatcher):
    # Загружаем конфиг в переменную config
    config: Config = load_config('D:\\My_All_Projects\\bot_ui_api_test\\.env')
    # Задаём базовую конфигурацию логирования
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)

    logging.basicConfig(
        level=logging.getLevelName(level=config.log.level),
        format=config.log.format,
        handlers=[
            logging.FileHandler(log_dir / 'bot.log', encoding='utf-8'),  # Запись в файл
            logging.StreamHandler()  # Вывод в консоль
        ]
    )
    # Инициализируем бот и диспетчер
    bot_token = Bot(token=config.bot.token)
    # Регистриуем роутеры в диспетчере
    dp.include_router(keyboard.router)
    dp.include_router(test_runner.router)
    dp.include_router(allure_report_process.router)
    dp.include_router(user.router)
    dp.include_router(other.router)


    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot_token.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot_token)


asyncio.run(main(dp))