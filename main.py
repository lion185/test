from aiogram import executor, Dispatcher, Bot
from aiogram.types import Message

bot = Bot("6215407782:AAHWi8lfYhUNEo2WdKfz62WkQV0Or3XsePs")
dp = Dispatcher(bot)

async def on(_):
    print("Работаю")

@dp.message_handler(content_types=['text'])
async def start(message: Message):
    await message.answer(f"Сообщение: {message.text}")

if __name__=="__main__":
    executor.start_polling(dp, on_startup=on)