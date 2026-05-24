from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str

@dataclass
class LogSettings:
    level: str
    format: str

@dataclass
class Config:
    bot: TgBot
    log: LogSettings

def load_config(path: str | None) -> Config:
    # Создаем экземпляр класса Env
    env: Env = Env()
    # Добавляем в переменные окружения данные, прочитанные из файла .env
    env.read_env(path)

    # Создаем экземпляр класса Config и наполняем его данными из переменных окружения
    return Config(
        bot=TgBot(token=env.str("BOT_TOKEN")),
        log = LogSettings(level=env.str("LOG_LEVEL"), format=env.str("LOG_FORMAT"))
    )
