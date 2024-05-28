import asyncio
from aiogram import Bot
from config import bot, dp, database
from handlers.pic import pic_router
from handlers.echo import echo_router
from handlers.start import start_router
from handlers.info import info_router
from handlers.menu import menu_router
from handlers.survey import survey_router
import logging

async def on_startup(bot: Bot) -> None:
    await database.create_tables()

async def main():
    dp.include_router(pic_router)
    dp.include_router(start_router)
    dp.include_router(info_router)
    dp.include_router(menu_router)
    dp.include_router(survey_router)
    # echo всегда в конце
    dp.include_router(echo_router)
    dp.startup.register(on_startup)
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())