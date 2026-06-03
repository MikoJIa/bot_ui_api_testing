from pathlib import Path

from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from execute_command_process import execute_command

router = Router()

@router.message(Command('runuitests', 'runapitests', 'runalltests'))
async def run_tests(message: Message, command: CommandObject):
    await message.answer(text='Подождите, пожалуйста... идет процесс загрузки тестов!')
    failed = 0
    passed = 0
    result = ''

    # Подготовка директории для результатов
    results_dir = Path('./allure_results')
    results_dir.mkdir(parents=True, exist_ok=True)
    # чистка предыдущих результатов
    for file in results_dir.glob("*"):
        file.unlink()

    try:
        if command.command == 'runuitests':
            result = await execute_command(
                "pytest -s -v ui_tests/tests --alluredir=./allure_results",
                message
            )
        elif command.command == 'runapitests':
            result = await execute_command(
                "pytest -v -s ./api_tests/test_api_artmas.py --alluredir=./allure_results",
                message
            )
        elif command.command == 'runalltests':
            result = await execute_command(
                "pytest -v -s -n 4 ./ui_tests/tests/ ./api_tests/ --alluredir=./allure_results",
                message
            )
        short_result = "\n".join([line for line in result.split("\n") if "PASSED" in line or "FAILED" in line])
        for test in short_result.split(" "):
            if "FAILED" in test:
                failed += 1
            if "PASSED" in test:
                passed += 1
        await message.answer(
            f"📊 Результаты тестов:\n{short_result[:3000]}\nFailed: {failed}\nPassed: {passed}"
        )
    except Exception as e:
        await message.edit_text(f"🔥 Ошибка: {str(e)}")