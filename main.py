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
    button5 = types.KeyboardButton(text="Погода", request_location=True)
    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, "Приветствую Вас на странице нашего бота «Спортивная жизнь в КС54!»", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def function(message):
    if message.text == "Команды":
        markup1 = types.InlineKeyboardMarkup(row_width=1)
        button6 = types.InlineKeyboardButton(text="Волейбол 🏐", callback_data='commands_volleyball')
        button7 = types.InlineKeyboardButton(text="Баскетбол 🏀", callback_data='commands_basketball')
        button8 = types.InlineKeyboardButton(text="Теннис 🏓", callback_data='commands_tennis')
        button9 = types.InlineKeyboardButton(text="Шахматы ♟️", callback_data='commands_chess')
        button10 = types.InlineKeyboardButton(text="Футбол ⚽", callback_data='commands_football')
        button11 = types.InlineKeyboardButton(text="Лёгкая атлетика 🏃🏻‍♂️", callback_data='commands_athletics')
        markup1.add(button6, button7, button8, button9, button10, button11)
        bot.send_message(message.chat.id, "Что Вам необходимо узнать?", reply_markup=markup1)

    if message.text == "Тренировки":
        markup2 = types.InlineKeyboardMarkup(row_width=1)
        button12 = types.InlineKeyboardButton(text="Волейбол 🏐", callback_data='training_volleyball')
        button13 = types.InlineKeyboardButton(text="Баскетбол 🏀", callback_data='training_basketball')
        button14 = types.InlineKeyboardButton(text="Теннис 🏓", callback_data='training_tennis')
        button15 = types.InlineKeyboardButton(text="Шахматы ♟️", callback_data='training_chess')
        button16 = types.InlineKeyboardButton(text="Футбол ⚽", callback_data='training_football')
        button17 = types.InlineKeyboardButton(text="Лёгкая атлетика 🏃🏻‍♂️", callback_data='training_athletics')
        markup2.add(button12, button13, button14, button15, button16, button17)
        bot.send_message(message.chat.id, "Что Вам необходимо узнать?", reply_markup=markup2)

@bot.message_handler(func=lambda message: True, content_types=['text', 'location'])
def message_handler(message):
    if message.location:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, get_weather_string(message.location))

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.data == 'commands_volleyball':
        bot.send_message(chat_id=call.message.chat.id, text='')
    elif call.data == 'commands_basketball':
        bot.send_message(chat_id=call.message.chat.id, text='')
    elif call.data == 'commands_tennis':
        bot.send_message(chat_id=call.message.chat.id, text='')
    elif call.data == 'commands_chess':
        bot.send_message(chat_id=call.message.chat.id, text='')
    elif call.data == 'commands_football':
        bot.send_message(chat_id=call.message.chat.id, text='')
    elif call.data == 'commands_athletics':
        bot.send_message(chat_id=call.message.chat.id, text='')
    elif call.data == 'training_volleyball':
        bot.send_message(chat_id=call.message.chat.id, text='')
    elif call.data == 'training_basketball':
        bot.send_message(chat_id=call.message.chat.id, text='')
    elif call.data == 'training_tennis':
        bot.send_message(chat_id=call.message.chat.id, text='')
    elif call.data == 'training_chess':
        bot.send_message(chat_id=call.message.chat.id, text='')
    elif call.data == 'training_football':
        bot.send_message(chat_id=call.message.chat.id, text='')
    elif call.data == 'training_athletics':
        bot.send_message(chat_id=call.message.chat.id, text='')
        
bot.infinity_polling()