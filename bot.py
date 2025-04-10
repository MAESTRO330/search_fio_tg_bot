"""
Точка входа в бота
"""

import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from config_reader import config
from handlers import questions, different_types


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    )

    bot = Bot(
        token=config.bot_token.get_secret_value(),
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(questions.router, different_types.router)
    await bot.delete_webhook(drop_pending_updates=True)  # Пропускаем все накопленные запросы (пока бот был выключен)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
