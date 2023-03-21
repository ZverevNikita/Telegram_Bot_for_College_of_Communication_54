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
    bot.send_message(message.chat.id, "Приветствую Вас на странице нашего бота «Спортивная жизнь в КС54!»",
                     reply_markup=markup)


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

    if message.text == "Приказы":
        markup3 = types.InlineKeyboardMarkup(row_width=4)
        button18 = types.InlineKeyboardButton(text = "трен.финал", callback_data ='training_final')
        button19 = types.InlineKeyboardButton(text = "трен.ФУТБОЛ", callback_data='football')
        button20 = types.InlineKeyboardButton(text = "трен.юноши", callback_data = 'teenagers')
        button21 = types.InlineKeyboardButton(text = "doc1034", callback_data = 'doc1034')
        button22 = types.InlineKeyboardButton(text = "Акт передачи инвентаря", callback_data = 'act')
        button23 = types.InlineKeyboardButton(text = "Баскет", callback_data = 'basket')
        button24 = types.InlineKeyboardButton(text = "Баскетбол 5 на 5", callback_data = 'basketball')
        button25 = types.InlineKeyboardButton(text = "Баскетбол АСБ", callback_data = 'asb')
        button26 = types.InlineKeyboardButton(text = "Баскет Д", callback_data = 'basketball_girls')
        button27 = types.InlineKeyboardButton(text = "Волейбол Д", callback_data = 'volleyball_girls')
        button28 = types.InlineKeyboardButton(text = "волейбол КК", callback_data = 'KK')
        button29 = types.InlineKeyboardButton(text = "контигра волейбол", callback_data = 'contrgame')
        button30 = types.InlineKeyboardButton(text = "контр.игра", callback_data = 'game')
        button31 = types.InlineKeyboardButton(text = "отбор футбол", callback_data = 'otbor')
        button32 = types.InlineKeyboardButton(text = "Приказ Волейбол Д", callback_data = "order_volleyball_girls")
        button33 = types.InlineKeyboardButton(text = "Приказ волейбол", callback_data = "order_volleyball")
        button34 = types.InlineKeyboardButton(text = "Расп_Трен_Фут", callback_data = 'rasp_tren_foot')
        button35 = types.InlineKeyboardButton(text = "Сор_Шахматы", callback_data = 'sor_chess')
        button36 = types.InlineKeyboardButton(text = "сор-баскет", callback_data = 'sor_basket')
        button37 = types.InlineKeyboardButton(text = "ССЛ.воллейбол.Ю", callback_data = 'SSL')
        button38 = types.InlineKeyboardButton(text = "стрит бол девушки", callback_data = 'street')
        button39 = types.InlineKeyboardButton(text = "Теннис", callback_data = 'ten')
        button40 = types.InlineKeyboardButton(text = "трен волейбол", callback_data = 'tren_v')
        button41 = types.InlineKeyboardButton(text = "трен.девушки", callback_data = 'tren_girls')
        markup3.add(button18, button19, button20, button21, button22, button23, button24, button25, button26, button27, button28, button29, button30, button31, button32, button33, button34, button35, button36, button37, button38, button39, button40, button41)
        bot.send_message(message.chat.id, "Что Вам необходимо узнать?", reply_markup=markup3)


@bot.message_handler(func=lambda message: True, content_types=['text', 'location'])
def message_handler(message):
    if message.location:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, get_weather_string(message.location))


@bot.callback_query_handler(func=lambda call: True)
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
    elif call.data == 'training_final':
        document = open("трен.финал.pdf")
        send_document(chat_id, document)
    elif call.data == 'football':
        document1 = open("трен.ФУТБОЛ.pdf")
        send_document(chat_id, document1)
    elif call.data == 'teenagers':
        document2 = open("трен.юноши.pdf")
        send_document(chat_id, document2)
    elif call.data == 'doc1034':
        document3 = open("doc1034.pdf")
        send_document(chat_id, document3)
    elif call.data == 'act':
        document4 = open("Акт передачи инвентаря.pdf")
        send_document(chat_id, document4)
    elif call.data == 'act':
        document5 = open("Акт передачи инвентаря.pdf")
        send_document(chat_id, document5)
    elif call.data == 'basket':
        document6 = open("Баскет.pdf")
        send_document(chat_id, document6)
    elif call.data == 'basketball':
        document7 = open("Баскетбол 5 на 5.pdf")
        send_document(chat_id, document7)
    elif call.data == 'asb':
        document8 = open("Баскетбол АСБ.pdf")
        send_document(chat_id, document8)
    elif call.data == 'basketball_girls':
        document9 = open("Баскет Д.pdf")
        send_document(chat_id, document9)
    elif call.data == 'basketball_girls':
        document10 = open("Баскет Д.pdf")
        send_document(chat_id, document10)
    elif call.data == 'volleyball_girls':
        document11 = open("Волейбол Д.pdf")
        send_document(chat_id, document11)
    elif call.data == 'KK':
        document12 = open("волейбол КК.pdf")
        send_document(chat_id, document12)
    elif call.data == 'contrgame':
        document13 = open("контигра волейбол.pdf")
        send_document(chat_id, document13)
    elif call.data == 'game':
        document14 = open("контр.игра.pdf")
        send_document(chat_id, document14)
    elif call.data == 'otbor':
        document15 = open("отбор футбол.pdf")
        send_document(chat_id, document15)
    elif call.data == 'order_volleyball_girls':
        document16 = open("Приказ Волейбол Д.pdf")
        send_document(chat_id, document16)
    elif call.data == 'order_volleyball':
        document17 = open("Приказ волейбол.pdf")
        send_document(chat_id, document17)
    elif call.data == 'rasp_tren_foot':
        document18 = open("Расп_Трен_Фут.pdf")
        send_document(chat_id, document18)
    elif call.data == 'sor_chess':
        document19 = open("Сор_Шахматы.pdf")
        send_document(chat_id, document19)
    elif call.data == 'sor_basket':
        document20 = open("сор-баскет.pdf")
        send_document(chat_id, document20)
    elif call.data == 'SSL':
        document21 = open("ССЛ.воллейбол.Ю.pdf")
        send_document(chat_id, document21)
    elif call.data == 'SSL':
        document22 = open("ССЛ.воллейбол.Ю.pdf")
        send_document(chat_id, document22)
    elif call.data == 'street':
        document23 = open("стрит бол девушки.pdf")
        send_document(chat_id, document23)
    elif call.data == 'ten':
        document24 = open("Теннис.pdf")
        send_document(chat_id, document24)
    elif call.data == 'tren_v':
        document25 = open("трен волейбол.pdf")
        send_document(chat_id, document25)
    elif call.data == 'tren_girls':
        document26 = open("трен.девушки.pdf")
        send_document(chat_id, document26)

bot.infinity_polling()