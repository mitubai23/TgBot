from aiogram import Router, types
from aiogram.filters import Command

echo_router = Router()

@echo_router.message()
async def echo(message: types.Message):
    await message.answer(message.text)