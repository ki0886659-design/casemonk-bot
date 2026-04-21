import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

TOKEN = "8743352517:AAEBpzfldu-uWcQt4uy1u1AarLPwVu1L-Ng"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    photo_url = "https://raw.githubusercontent.com/ki0886659-design/casemonk-bot/main/1000001802.jpg"
    caption = "🎁 CaseMonk – Играй и выигрывай подарки!\n\nНажми «Играть», чтобы открыть Web-App и начать!"
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(text="Играть", web_app=WebAppInfo(url="https://google.com")))
    markup.add(KeyboardButton(text="Поддержка"), KeyboardButton(text="Канал"))

    try:
        await message.answer_photo(photo=photo_url, caption=caption, reply_markup=markup)
    except:
        await message.answer(caption, reply_markup=markup)

@dp.message_handler(lambda m: m.text == "Поддержка")
async def sup(m: types.Message):
    await m.answer("@casemonk_sup_robot")

@dp.message_handler(lambda m: m.text == "Канал")
async def chan(m: types.Message):
    await m.answer("@CaseMonk")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
