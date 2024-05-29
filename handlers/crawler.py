from aiogram import Router, types, F
from aiogram.filters import Command
from crawler.house import HouseCrawler

crawler_router = Router()

@crawler_router.message(Command("crawler"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Да", callback_data="scrap"),
            ]
        ]
    )
    await message.answer(f"Начать парсинг?", reply_markup=kb)

@crawler_router.callback_query(F.data == 'scrap')
async def scrap(callback: types.CallbackQuery):
    crawler = HouseCrawler()
    page = crawler.get_page()
    houses = crawler.get_links(page)
    for house in houses:
        await callback.message.answer(house)