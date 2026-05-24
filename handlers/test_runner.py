import asyncio
import subprocess
import sys
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, Update

router = Router()

async def execute_command(cmd: str, message: Message, timeout: int = 300) -> str:
    """Выполняет shell-команду с таймаутом и возвращает результат"""
    try:
        proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout)
        output = f"STDOUT:\n{stdout.decode().strip()}" if stdout else ""
        output += f"\nSTDERR:\n{stderr.decode().strip()}" if stderr else ""
        return output.strip()
    except asyncio.TimeoutError:
        return f"❌ Таймаут ({timeout} сек)"
    except Exception as e:
        return f"⚠️ Ошибка: {str(e)}"


@router.message(Command(commands='runuitests'))
async def run_ui_tests(message: Message):
    await message.answer(text='Подождите, пожалуйста... идет процесс загрузки тестов!')

    try:
        result = await execute_command(
            "pytest -s -v ui_tests/tests",
            message
        )
        short_result = "\n".join([line for line in result.split("\n")])
        await message.answer(
            f"📊 Результаты тестов:\n{short_result[:3000]}"
        )
    except Exception as e:
        await message.edit_text(f"🔥 Ошибка: {str(e)}")