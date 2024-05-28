from aiogram import Router, types
from aiogram.filters import Command
import random
from os import listdir, path
import logging

pic_router = Router()

@pic_router.message(Command("pic"))
async def pic(message: types.Message):
    image_directory = '../images'
    file_name = random.choice(listdir(image_directory))
    file_path = path.join(image_directory, file_name)
    logging.info(file_path)
    file = types.FSInputFile(file_path)
    await message.answer_photo(file)