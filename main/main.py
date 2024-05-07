from aiogram import Bot, Dispatcher, types, executor 
from aiogram.types.web_app_info import WebAppInfo
bot = Bot('')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start (message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open WebApp', web_app=WebAppInfo(url="https://ru.wikipedia.org/wiki/%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81")))
    await message.answer('hello my friend', reply_markup=markup)
        
executor.start_polling(dp)
