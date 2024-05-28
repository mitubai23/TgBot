import asyncio
from aiogram import Bot, Dispatcher
from os import getenv
from dotenv import load_dotenv
from handlers.pic import pic_router
from handlers.echo import echo_router
from handlers.start import start_router
from handlers.info import info_router
from handlers.menu import menu_router
import logging

load_dotenv()
bot = Bot(token=getenv("TOKEN"))
dp = Dispatcher()

async def main():
    dp.include_router(pic_router)
    dp.include_router(start_router)
    dp.include_router(info_router)
    dp.include_router(menu_router)
    # echo всегда в конце
    dp.include_router(echo_router)
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())