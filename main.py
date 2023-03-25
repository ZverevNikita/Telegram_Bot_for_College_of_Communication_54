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

    if message.text == "Приказы":
        markup3 = types.InlineKeyboardMarkup(row_width=2)
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
        button40 = types.InlineKeyboardButton(text = "трен.волейбол", callback_data = 'tren_v')
        button41 = types.InlineKeyboardButton(text = "трен.девушки", callback_data = 'tren_girls')
        markup3.add(button18, button19, button20, button21, button22, button23, button24, button25, button26, button27, button28, button29, button30, button31, button32, button33, button34, button35, button36, button37, button38, button39, button40, button41)
        bot.send_message(message.chat.id, "Что Вам необходимо узнать?", reply_markup=markup3)

    if message.text == "Спортивные залы":
        markup4 = types.InlineKeyboardMarkup(row_width=1)
        button42 = types.InlineKeyboardButton(text = "Таганское-1", callback_data='tag')
        button43 = types.InlineKeyboardButton(text = "Рязанское-6", callback_data='rya')
        button44 = types.InlineKeyboardButton(text = "Римское-7", callback_data='rim')
        button45 = types.InlineKeyboardButton(text = "Авиамоторное-8", callback_data='bas')
        markup4.add(button42, button43, button44, button45)
        bot.send_message(message.chat.id, "Что Вам необходимо узнать?", reply_markup=markup4)

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
    elif call.data == 'tag':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('tag_2-scaled.jpg', 'rb'), caption='Адрес спортивой площадки: город Москва, улица Большие Каменщики, дом 7'), telebot.types.InputMediaPhoto(open('tag_3-scaled.jpg', 'rb')), telebot.types.InputMediaPhoto(open('tag_5-scaled.jpg', 'rb')), telebot.types.InputMediaPhoto(open('tag_6-scaled.jpg', 'rb')), telebot.types.InputMediaPhoto(open('tag_7-scaled.jpg', 'rb'))])
    elif call.data == 'rya':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('rya_1-1-scaled.jpg', 'rb'), caption='Адрес спортивой площадки: город Москва, Рязанский проспект, дом 8, строение 1'), telebot.types.InputMediaPhoto(open('rya_2-1-scaled.jpg', 'rb')), telebot.types.InputMediaPhoto(open('rya_3-1-scaled.jpg', 'rb')), telebot.types.InputMediaPhoto(open('rya_4-1-scaled.jpg', 'rb')), telebot.types.InputMediaPhoto(open('rya_5-1-scaled.jpg', 'rb')), telebot.types.InputMediaPhoto(open('rya_6-1-scaled.jpg', 'rb'))])
    elif call.data == 'rim':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('rim_3-1-scaled.jpg', 'rb'), caption='Адрес спортивной площадки: город Москва, улица Рабочая, дом 12, строение 1'), telebot.types.InputMediaPhoto(open('rim_4-1-scaled.jpg', 'rb')), telebot.types.InputMediaPhoto(open('rim_5-1-scaled.jpg', 'rb')), telebot.types.InputMediaPhoto(open('rim_6-1-scaled.jpg', 'rb'))])
    elif call.data == 'bas':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('bas-1-scaled.jpg', 'rb'), caption='Адрес спортивной площадки: город Москва, улица Басовская, дом 12'), telebot.types.InputMediaPhoto(open('bas-2-scaled.jpg', 'rb')), telebot.types.InputMediaPhoto(open('bas-4-scaled.jpg', 'rb')), telebot.types.InputMediaPhoto(open('bas-5-scaled.jpg', 'rb')), telebot.types.InputMediaPhoto(open('bas-6-scaled.jpg', 'rb')), telebot.types.InputMediaPhoto(open('bas-7-scaled.jpg', 'rb'))])
    elif call.data == 'training_final':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('1.jpg', 'rb'), caption='трен.финал'), telebot.types.InputMediaPhoto(open('2.jpg', 'rb'))])
    elif call.data == 'football':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('3.jpg', 'rb'), caption='трен.ФУТБОЛ'), telebot.types.InputMediaPhoto(open('4.jpg', 'rb'))])
    elif call.data == 'teenagers':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('5.jpg', 'rb'), caption='трен.юноши'), telebot.types.InputMediaPhoto(open('6.jpg', 'rb'))])
    elif call.data == 'doc1034':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('7.jpg', 'rb'), caption='doc1034'), telebot.types.InputMediaPhoto(open('8.jpg', 'rb'))])
    elif call.data == 'act':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('9.jpg', 'rb'), caption='Акт передачи инвентаря'), telebot.types.InputMediaPhoto(open('10.jpg', 'rb')), telebot.types.InputMediaPhoto(open('11.jpg', 'rb')), telebot.types.InputMediaPhoto(open('12.jpg', 'rb')), telebot.types.InputMediaPhoto(open('13.jpg', 'rb'))])
    elif call.data == 'basket':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('54.jpg', 'rb'), caption='Баскет'), telebot.types.InputMediaPhoto(open('55.jpg', 'rb')), telebot.types.InputMediaPhoto(open('56.jpg', 'rb')), telebot.types.InputMediaPhoto(open('57.jpg', 'rb'))])
    elif call.data == 'basketball':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('52.jpg', 'rb'), caption='Баскетбол 5 на 5'), telebot.types.InputMediaPhoto(open('53.jpg', 'rb'))])
    elif call.data == 'asb':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('48.jpg', 'rb'), caption='Баскетбол АСБ'), telebot.types.InputMediaPhoto(open('49.jpg', 'rb')), telebot.types.InputMediaPhoto(open('50.jpg', 'rb')), telebot.types.InputMediaPhoto(open('51.jpg', 'rb'))])
    elif call.data == 'basketball_girls':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('46.jpg', 'rb'), caption='Баскет Д'), telebot.types.InputMediaPhoto(open('47.jpg', 'rb'))])
    elif call.data == 'volleyball_girls':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('44.jpg', 'rb'), caption='Волейбол Д'), telebot.types.InputMediaPhoto(open('45.jpg', 'rb'))])
    elif call.data == 'KK':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('41.jpg', 'rb'), caption='волейбол КК'), telebot.types.InputMediaPhoto(open('42.jpg', 'rb')), telebot.types.InputMediaPhoto(open('43.jpg', 'rb'))])
    elif call.data == 'contrgame':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('39.jpg', 'rb'), caption='контригра волейбол'), telebot.types.InputMediaPhoto(open('40.jpg', 'rb'))])
    elif call.data == 'game':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('37.jpg', 'rb'), caption='контр.игра'), telebot.types.InputMediaPhoto(open('38.jpg', 'rb'))])
    elif call.data == 'otbor':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('36.jpg', 'rb'), caption='отбор футбол')])
    elif call.data == 'order_volleyball_girls':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('34.jpg', 'rb'), caption='Приказ Волейбол Д'), telebot.types.InputMediaPhoto(open('35.jpg', 'rb'))])
    elif call.data == 'order_volleyball':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('32.jpg', 'rb'), caption='Приказ волейбол'), telebot.types.InputMediaPhoto(open('33.jpg', 'rb'))])
    elif call.data == 'rasp_tren_foot':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('30.jpg', 'rb'), caption='Расп_Трен_Фут'), telebot.types.InputMediaPhoto(open('31.jpg', 'rb'))])
    elif call.data == 'sor_chess':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('28.jpg', 'rb'), caption='Сор_Шахматы'), telebot.types.InputMediaPhoto(open('29.jpg', 'rb'))])
    elif call.data == 'sor_basket':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('26.jpg', 'rb'), caption='сор-баскет'), telebot.types.InputMediaPhoto(open('27.jpg', 'rb'))])
    elif call.data == 'SSL':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('24.jpg', 'rb'), caption='ССЛ.волейбол.Ю'), telebot.types.InputMediaPhoto(open('25.jpg', 'rb'))])
    elif call.data == 'street':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('22.jpg', 'rb'), caption='стрит бол девушки'), telebot.types.InputMediaPhoto(open('23.jpg', 'rb'))])
    elif call.data == 'ten':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('18.jpg', 'rb'), caption='Теннис'), telebot.types.InputMediaPhoto(open('19.jpg', 'rb')), telebot.types.InputMediaPhoto(open('20.jpg', 'rb')), telebot.types.InputMediaPhoto(open('21.jpg', 'rb'))])
    elif call.data == 'tren_v':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('16.jpg', 'rb'), caption='трен.волейбол'), telebot.types.InputMediaPhoto(open('17.jpg', 'rb'))])
    elif call.data == 'tren_girls':
        bot.send_media_group(call.message.chat.id, [telebot.types.InputMediaPhoto(open('14.jpg', 'rb'), caption='трен.девушки'), telebot.types.InputMediaPhoto(open('15.jpg', 'rb'))])

bot.infinity_polling()