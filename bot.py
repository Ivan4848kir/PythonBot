import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from datetime import datetime

logging.basicConfig(level=logging.INFO)
bot=Bot(token="7784426296:AAH_X3gsidh41U_S3NdfvAk8BhFFnK4hW6A")
dp=Dispatcher()
dp["started_at"]=datetime.now().strftime("%Y-%m-%d %H:%M")

@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.answer("Test 1")
@dp.message(Command("test2"))
async def cmd_test2(message: types.Message):
    await message.answer("Test 2")
@dp.message(Command("add_to_list"))
async def cmd_add_to_list(message: types.Message, mylist: list[int]):
    mylist.append(7)
    await message.answer("Добавлено число 7")
@dp.message(Command("show_list"))
async def cmd_show_list(message: types.Message, mylist: list[int]):
    await message.answer(f"Ваш список: {mylist}")
@dp.message(Command("info"))
async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"Бот запущен {started_at}")

async def main():
    await dp.start_polling(bot, mylist=[1, 2, 3])

if __name__ == "__main__":
    asyncio.run(main())