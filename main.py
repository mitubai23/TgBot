import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging
import random
from dotenv import load_dotenv
from os import getenv, listdir, path

load_dotenv()
bot = Bot(token=getenv("TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}")


@dp.message(Command('myinfo'))
async def myinfo(message: types.Message):
    await message.answer(f"Ваше имя: {message.from_user.first_name}\n"
                          f"Ваша username: {message.from_user.username}\n"
                          f"Ваш id: {message.from_user.id}")


@dp.message(Command("pic"))
async def pic(message: types.Message):
    image_directory = 'images'
    file_name = random.choice(listdir(image_directory))
    file_path = path.join(image_directory, file_name)
    logging.info(file_path)
    file = types.FSInputFile(file_path)
    await message.answer_photo(file)


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():

    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())