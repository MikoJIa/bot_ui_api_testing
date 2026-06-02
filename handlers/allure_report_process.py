import os
import time
import zipfile
from pathlib import Path
from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message, FSInputFile
from execute_command_process import execute_command

router = Router()

@router.message(Command(commands='lastreport'))
async def generate_allure_report(message: Message):

    try:
        # Проверка результатов теста
        results_dir = Path('./allure_results')
        if not results_dir.exists() or not any(results_dir.iterdir()):
            await message.answer('Нет данных отчета о тестах!')
        # генерация отчетов
        await message.answer("Генерация Allure-отчетов ...")
        report_dir = Path('./allure_report')
        report_dir.mkdir(parents=True, exist_ok=True)

        generate_result = await execute_command(
            "allure generate ./allure_results --clean -o ./allure_report",
            message
        )
        print(generate_result)

        # Проверка наличия сгенерированного отчета
        report_checkup = report_dir / 'index.html'
        if not report_checkup.exists():
            await message.answer(" Ошибка генерации: index.html не найден в allure-report")

        # Создание архива
        time_step_report = int(time.time())
        zip_name = f"allure_report_{time_step_report}.zip"

        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zip:
            # Добавляем allure-report
            for root, _, files in os.walk(report_dir):
                for file in files:
                    file_path = Path(root) / file
                    archive_path = os.path.join("allure-report", os.path.relpath(file_path, report_dir))
                    zip.write(file_path, archive_path)
            # Добавляем allure-results
            for root, _, files in os.walk(results_dir):
                for file in files:
                    file_path = Path(root) / file
                    arcname = os.path.join("./allure_results", os.path.relpath(file_path, results_dir))
                    zip.write(file_path, arcname=arcname)

        # Отправка архива
        await message.answer("Отправка архива")
        document = FSInputFile(zip_name, filename=zip_name)
        await message.bot.send_document(
            chat_id=message.chat.id,
            document=document,
            caption="📊 Allure Report (включая исходные данные)"
        )

        # Очистка временных файлов
        os.remove(zip_name)
    except Exception as e:
        await message.answer(f"Критическая ошибка: {str(e)}")