import telebot
from telebot import types

from weather import get_weather_string

token = '6201705760:AAE_kjoIWWkC9VWnOoqnDHeS1QqNQiu7Rb8'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button1 = types.KeyboardButton(text="Команды")
    button2 = types.KeyboardButton(text="Приказы")
    button3 = types.KeyboardButton(text="Тренировки")
    button4 = types.KeyboardButton(text="Спортивные залы")
    button5 = types.KeyboardButton(text="Погода")
    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, "Приветствую Вас на странице нашего бота «Спортивная жизнь в КС54!»",
                     reply_markup=markup)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def message_handler(m):
    if m.text == 'Погода':
        bot.send_message(m.chat.id, get_weather_string())


bot.infinity_polling()
