import requests
from aiogram import types, Bot, Dispatcher, executor
import logging

API_TOKEN = '5042999290:AAHi6RXhJiOt2JIfO7Dho0V1RWCz38m6pbY'
API_KEY = 'c02d799f4255a22d10eeafec5f9054c3'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def let_start(message: types.Message):
    await message.answer('Введите название города: ')


@dp.message_handler(commands=['help'])
async def need_help(message: types.Message):
    await message.answer('Чем помочь')


@dp.message_handler()
async def weather(message: types.Message):
    city_name = message.text
    url = 'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'.format(
            city_name=city_name, API_KEY=API_KEY)
    r = requests.get(url)
    res = r.json()

    if res['cod'] == '404':
        await message.reply('Введите правильной название вашего города')
    else:
        city = res['name']
        temp = res['main']['temp']
        humidity = res['main']['humidity']
        wind = res['wind']['speed']
        text = 'Погода в городе: {city}\nТемпература:  {temp}\nВлажность:  {humidity} %\nВетер:  {wind} m/s\n'.format(
                city=city, temp=temp, humidity=humidity, wind=wind)
        await message.reply(text)

executor.start_polling(dp, skip_updates=True)
