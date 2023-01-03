import telebot
from telebot import types
import config

token = '5788796203:AAEORHlnQLiUWK_xC9PzmC6UXX3_4SZhhhc'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text = "Про нас")
    button1 = types.KeyboardButton(text = "О нас")
    button2 = types.KeyboardButton(text = "Родителям")
    button3 = types.KeyboardButton(text = "Учащимся")
    button4 = types.KeyboardButton(text = "Педагогам")
    button5 = types.KeyboardButton(text = "Дополнительное образование")
    button6 = types.KeyboardButton(text = "Проекты")
    button7 = types.KeyboardButton(text = "Предпрофессиональные классы")
    button8 = types.KeyboardButton(text = "Сведения об образовательной организации")
    button9 = types.KeyboardButton(text="Дополнительная информация")
    button10 = types.KeyboardButton(text="Электронные сервисы")
    button11 = types.KeyboardButton(text = "Как нас найти?")
    button12 = types.KeyboardButton(text = "Контактная информация")
    markup.add(button, button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12)
    bot.send_message(message.chat.id, 'Приветствую Вас на странице нашего бота ГБОУ "Школа №2100! Чего бы Вы хотели бы узнать о нашей школе?', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def function(message):
    if (message.text == "Про нас"):
        bot.send_message(message.chat.id, text="Школа №2100 - современная и динамично развивающаяся образовательная образовательная организация, следующая в своей работе девизу: «Каким бы сложным ни был путь, какими бы призрачными ни казались цели, несмотря ни на что, МЫ каждый день идём вперёд!». Поэтому для нас важен вклад каждого участника образовательного процесса в общий результат!")
    else:
        if (message.text == "О нас"):
            markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1_1 = types.KeyboardButton(text = "Общая информация")
            button1_2 = types.KeyboardButton(text = "Педагогический состав")
            button1_3 = types.KeyboardButton(text = "Контакты подразделений")
            button1_4 = types.KeyboardButton(text = "Новости")
            button1_5 = types.KeyboardButton(text = "Органы управления")
            button1_6 = types.KeyboardButton(text = "Отзывы")
            button1_7 = types.KeyboardButton(text = "Наши достидения")
            button1_8 = types.KeyboardButton(text = "Платные образовательные услуги")
            button1_9 = types.KeyboardButton(text = "Общественная жизнь")
            button1_10 = types.KeyboardButton(text = "Фото и видео")
            button1_11 = types.KeyboardButton(text = "СМИ о нас")
            markup0.add(button1_1, button1_2, button1_3, button1_4, button1_5, button1_6, button1_7, button1_8, button1_9, button1_10, button1_11)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup0)

        if (message.text == "Родителям"):
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button2_1 = types.KeyboardButton(text = "Алгоритм поступления")
            button2_2 = types.KeyboardButton(text = "Свободые места в классах")
            button2_3 = types.KeyboardButton(text = "Вопрос - ответ")
            button2_4 = types.KeyboardButton(text = "Дошкольное образование")
            button2_5 = types.KeyboardButton(text = "Все вопросы о питании")
            button2_6 = types.KeyboardButton(text = "Психологическая поддержка ребёнка")
            button2_7 = types.KeyboardButton(text = "Медицинское обслуживание")
            button2_8 = types.KeyboardButton(text = "Городской экспертно-консультативный совет родительской общественности")
            markup1.add(button2_1, button2_2, button2_3, button2_4, button2_5, button2_6, button2_7, button2_8)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup1)

        if (message.text == "Учащимся"):
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button3_1 = types.KeyboardButton(text = "Расписание, учебные периоды, каникулы")
            button3_2 = types.KeyboardButton(text = "Государственная итоговая аттестация")
            button3_3 = types.KeyboardButton(text = "Олимпиады, конкурсы и конференции")
            button3_4 = types.KeyboardButton(text = "Библиотека")
            button3_5 = types.KeyboardButton(text = "Совет учащихся")
            markup2.add(button3_1, button3_2, button3_3, button3_4, button3_5)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup2)

        if (message.text == "Педагогам"):
            markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button4_1 = types.KeyboardButton(text = "Образовательные проекты")
            button4_2 = types.KeyboardButton(text = "Вакансии")
            button4_3 = types.KeyboardButton(text = "Возможности МЭШ для педагогов")
            button4_4 = types.KeyboardButton(text = "Конкурсы, олимпиады, конференции")
            button4_5 = types.KeyboardButton(text = "Профсоюзная организация")
            button4_6 = types.KeyboardButton(text = "Совет ветеранов педагогического труда")
            markup3.add(button4_1, button4_2, button4_3, button4_4, button4_5, button4_6)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup3)

        if (message.text == "Дополнительное образование"):
            markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button5_1 = types.KeyboardButton(text = "Поиск кружков и секций")
            markup4.add(button5_1)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup4)

        if (message.text == "Проекты"):
            markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button6_1 = types.KeyboardButton(text = "Московские проекты")
            markup5.add(button6_1)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup5)

        if (message.text == "Предпрофессиональные классы"):
            markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button7_1 = types.KeyboardButton(text = "Кадетский класс")
            button7_2 = types.KeyboardButton(text = "Новый педагогический класс")
            button7_3 = types.KeyboardButton(text = "Лингвистическая вертикаль")
            button7_4 = types.KeyboardButton(text = "Математическая вертикаль")
            markup6.add(button7_1, button7_2, button7_3, button7_4)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup6)

        if (message.text == "Общественная жизнь"):
            markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button8_1 = types.KeyboardButton(text = "Спортивный клуб")
            button8_2 = types.KeyboardButton(text = "Волонтёрское движение")
            button8_3 = types.KeyboardButton(text = "ГТО")
            markup7.add(button8_1, button8_2, button8_3)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup7)

        if (message.text == "Фото и видео"):
            markup8 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button9_1 = types.KeyboardButton(text = "Фотогалерея")
            markup8.add(button9_1)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup8)

        if (message.text == "Алгоритм поступления"):
            markup9 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button10_1 = types.KeyboardButton(text = "Дошкольные группы")
            button10_2 = types.KeyboardButton(text = "Основная школа (5-9 классы)")
            button10_3 = types.KeyboardButton(text = "Поступление в 1 класс")
            markup9.add(button10_1, button10_2, button10_3)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup9)

        if (message.text == "Медицинское обслуживание"):
            markup10 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button11_1 = types.KeyboardButton(text = "Документы")
            button11_2 = types.KeyboardButton(text = "Организация медицинского обслуживания")
            button11_3 = types.KeyboardButton(text = "График проведения медицинских осмотров")
            button11_4 = types.KeyboardButton(text = "Это важно знать")
            markup10.add(button11_1, button11_2, button11_3, button11_4)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup10)

        if (message.text == "Городской экспертно-консультативный совет родительской общественности"):
            markup11 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button12_1 = types.KeyboardButton(text = "Информация для родителей")
            button12_2 = types.KeyboardButton(text = "Информация общегородских родительских онлайн-совещаний")
            button12_3 = types.KeyboardButton(text = "Конкурсы")
            button12_4 = types.KeyboardButton(text = "Образовательные программы")
            button12_5 = types.KeyboardButton(text = "Информационные встречи для родителей «Вузы-родителям»")
            button12_6 = types.KeyboardButton(text = "Совет отцов")
            button12_7 = types.KeyboardButton(text = "Профориентационные встречи для родителей «Колледжи Москвы: перспективы и возможности»")
            button12_8 = types.KeyboardButton(text = "Организация питания обучающихся в образовательных организациях города Москвы")
            button12_9 = types.KeyboardButton(text = "Создание условий получения образования детьми с ОВЗ в вопросах и ответах")
            button12_10 = types.KeyboardButton(text = "Социальная поддержка многодетных семей города Москвы")
            markup11.add(button12_1, button12_2, button12_3, button12_4, button12_5, button12_6, button12_7, button12_8, button12_9, button12_10)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup11)

        if (message.text == "Государственная итоговая аттестация"):
            markup12 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button13_1 = types.KeyboardButton(text = "ОГЭ, ЕГЭ")
            markup12.add(button13_1)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup12)

        if (message.text == "Олимпиады, конкурсы и конференции"):
            markup13 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button14_1 = types.KeyboardButton(text = "Анонсы мероприятий")
            button14_2 = types.KeyboardButton(text = "Всеросстйская олимпиада школьников")
            button14_3 = types.KeyboardButton(text = "Московская олимпиада школьников")
            button14_4 = types.KeyboardButton(text = "Олимпиада «Курчатов»")
            button14_5 = types.KeyboardButton(text = "Музеи. Парки. Усадьбы")
            button14_6 = types.KeyboardButton(text = "История и культура храмов столицы")
            button14_7 = types.KeyboardButton(text = "Не прервётся связь поколений")
            button14_8 = types.KeyboardButton(text = "Готов к жизни в умном городе")
            button14_9 = types.KeyboardButton(text = "Чемпионат профессионального мастерства города Москвы «МОСКОВСКИЕ МАСТЕРА»")
            button14_10 = types.KeyboardButton(text = "Московский детский чемпионат «Мастерята»")
            markup13.add(button14_1, button14_2, button14_3, button14_4, button14_5, button14_6, button14_7, button14_8, button14_9, button14_10)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup13)

        if (message.text == "Кадетский класс"):
            markup14 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button15_1 = types.KeyboardButton(text = "Показатели проекта")
            markup14.add(button15_1)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup14)

        if (message.text == "Новый педагогический класс"):
            markup15 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button16_1 = types.KeyboardButton(text = "Показатели проекта")
            button16_2 = types.KeyboardButton(text = "Общая информация")
            markup15.add(button16_1, button16_2)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup15)

        if (message.text == "Лингвистическая вертикаль"):
            markup16 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button17_1 = types.KeyboardButton(text = "Показатели проекта")
            markup16.add(button17_1)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup16)

        if (message.text == "Математическая вертикаль"):
            markup17 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button18_1 = types.KeyboardButton(text = "Показатели проекта")
            button18_2 = types.KeyboardButton(text = "Общая информация")
            button18_3 = types.KeyboardButton(text = "Новости")
            markup17.add(button18_1, button18_2, button18_3)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup17)

        if (message.text == "Сведения об образовательной организации"):
            markup18 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button19_1 = types.KeyboardButton(text = "Основные сведения")
            button19_2 = types.KeyboardButton(text = "Структура и органы управления образовательной организацией")
            button19_3 = types.KeyboardButton(text = "Документы")
            button19_4 = types.KeyboardButton(text = "Образование")
            button19_5 = types.KeyboardButton(text = "Руководство. Педагогический (научно-педагогический) состав")
            button19_6 = types.KeyboardButton(text = "Материально-техническое обеспечение и оснащенность образовательного процесса")
            button19_7 = types.KeyboardButton(text = "Платные образовательные услуги")
            button19_8 = types.KeyboardButton(text = "Финансово-хозяйственная деятельность")
            button19_9 = types.KeyboardButton(text = "Вакантные места для приёма (перевода) обучающихся")
            button19_10 = types.KeyboardButton(text = "Образовательные стандарты и требования")
            button19_11 = types.KeyboardButton(text="Стипендии и меры поддержки обучающихся")
            button19_12 = types.KeyboardButton(text="Доступная среда")
            button19_13 = types.KeyboardButton(text="Международное сотрудничество")
            button19_14 = types.KeyboardButton(text="Платёжные реквизиты")
            button19_15 = types.KeyboardButton(text="Публичный доклад руководителя")
            button19_16 = types.KeyboardButton(text="Организация питания в образовательной организации")
            markup18.add(button19_1, button19_2, button19_3, button19_4, button19_5, button19_6, button19_7, button19_8, button19_9, button19_10, button19_11, button19_12, button19_13, button19_14, button19_15, button19_16)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup18)

        if (message.text == "Дополнительная информация"):
            markup19 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button20_1 = types.KeyboardButton(text = "Информация для родителей")
            button21_2 = types.KeyboardButton(text = "Информация общегородских родительских онлайн-совещаний")
            button22_3 = types.KeyboardButton(text = "Конкурсы")
            button23_4 = types.KeyboardButton(text = "Образовательные программы")
            button24_5 = types.KeyboardButton(text = "Информационные встречи для родителей «Вузы-родителям»")
            button25_6 = types.KeyboardButton(text = "Совет отцов")
            button26_7 = types.KeyboardButton(text = "Профориентационные встречи для родителей «Колледжи Москвы: перспективы и возможности»")
            button27_8 = types.KeyboardButton(text = "Организация питания обучающихся в образовательных организациях города Москвы")
            button28_9 = types.KeyboardButton(text = "Создание условий получения образования детьми с ОВЗ в вопросах и ответах")
            markup19.add(button20_1, button21_2, button22_3, button23_4, button24_5, button25_6, button26_7, button27_8, button28_9)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup19)

        if (message.text == "Электронные сервисы"):
            markup20 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button31_1 = types.KeyboardButton(text = "Московская электронная школа")
            button32_2 = types.KeyboardButton(text = "Государственные услуги")
            button33_3 = types.KeyboardButton(text = "Электронная карта в образовании")
            button34_4 = types.KeyboardButton(text = "Полезные ссылки")
            markup20.add(button31_1, button32_2, button33_3, button34_4)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup20)

bot.polling(none_stop=True)
