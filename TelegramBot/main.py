import telebot
from telebot import types
import config

token = '5788796203:AAEORHlnQLiUWK_xC9PzmC6UXX3_4SZhhhc'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text="Про нас")
    button1 = types.KeyboardButton(text="О нас")
    button2 = types.KeyboardButton(text="Родителям")
    button3 = types.KeyboardButton(text="Учащимся")
    button4 = types.KeyboardButton(text="Педагогам")
    button5 = types.KeyboardButton(text="Дополнительное образование")
    button6 = types.KeyboardButton(text="Проекты")
    button7 = types.KeyboardButton(text="Предпрофессиональные классы")
    button8 = types.KeyboardButton(text="Сведения об образовательной организации")
    button9 = types.KeyboardButton(text="Дополнительная информация")
    button10 = types.KeyboardButton(text="Электронные сервисы")
    button11 = types.KeyboardButton(text="Как нас найти?")
    button12 = types.KeyboardButton(text="Контактная информация")
    markup.add(button, button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
               button11, button12)
    bot.send_message(message.chat.id,
                     'Приветствую Вас на странице нашего бота ГБОУ "Школа №2100! Чего бы Вы хотели бы узнать о нашей школе?',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def function(message):
    if (message.text == "Про нас"):
        bot.send_message(message.chat.id,
                         text="Школа №2100 - современная и динамично развивающаяся образовательная образовательная организация, следующая в своей работе девизу: «Каким бы сложным ни был путь, какими бы призрачными ни казались цели, несмотря ни на что, МЫ каждый день идём вперёд!». Поэтому для нас важен вклад каждого участника образовательного процесса в общий результат!")
    else:
        if (message.text == "О нас"):
            markup0 = types.InlineKeyboardMarkup(row_width=1)
            button1_1 = types.InlineKeyboardButton(text="Общая информация",
                                                   url="https://sch2100.mskobr.ru/o-nas/obshaya-informatciya")
            button1_2 = types.InlineKeyboardButton(text="Педагогический состав",
                                                   url="https://sch2100.mskobr.ru/o-nas/pedagogicheskii-sostav")
            button1_3 = types.InlineKeyboardButton(text="Контакты подразделений",
                                                   url="https://sch2100.mskobr.ru/o-nas/kontakty-podrazdelenij")
            button1_4 = types.InlineKeyboardButton(text="Новости",
                                                   url="https://sch2100.mskobr.ru/o-nas/kontakty-podrazdelenij")
            button1_5 = types.InlineKeyboardButton(text="Органы управления",
                                                   url="https://sch2100.mskobr.ru/o-nas/organy-upravleniya/upravlyayushchij-sovet")
            button1_6 = types.InlineKeyboardButton(text="Отзывы", url="https://sch2100.mskobr.ru/o-nas/reviews/")
            button1_7 = types.InlineKeyboardButton(text="Наши достидения",
                                                   url="https://sch2100.mskobr.ru/o-nas/nashi-dostizheniya")
            button1_8 = types.InlineKeyboardButton(text="Платные образовательные услуги",
                                                   url="https://sch2100.mskobr.ru/o-nas/paid_services")
            button1_9 = types.InlineKeyboardButton(text="Общественная жизнь", callback_data="cb_social_life")
            button1_10 = types.InlineKeyboardButton(text="Фото и видео",
                                                    url="https://sch2100.mskobr.ru/o-nas/photo-i-video/photo")
            button1_11 = types.InlineKeyboardButton(text="СМИ о нас", url="https://sch2100.mskobr.ru/o-nas/smi-o-nas")
            markup0.add(button1_1, button1_2, button1_3, button1_4, button1_5, button1_6, button1_7, button1_8,
                        button1_9, button1_10, button1_11)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup0)

        if (message.text == "Общественная жизнь"):
            markup0_0 = types.InlineKeyboardMarkup(row_width=1)
            button0_1 = types.InlineKeyboardButton(text="Спортивный клуб",
                                                   url="https://sch2100.mskobr.ru/o-nas/obshchestvennaya-zhizn/sport-club")
            button0_2 = types.InlineKeyboardButton(text="Волонтёрское движение",
                                                   url="https://sch2100.mskobr.ru/o-nas/obshchestvennaya-zhizn/volunteer-dvizhenie")
            button0_3 = types.InlineKeyboardButton(text="ГТО",
                                                   url="https://sch2100.mskobr.ru/o-nas/obshchestvennaya-zhizn/obschestvennaya-jizn")
            markup0_0.add(button0_1, button0_2, button0_3)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup0_0)

        if (message.text == "Родителям"):
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            button2_1 = types.InlineKeyboardButton(text="Свободые места в классах",
                                                   url="https://sch2100.mskobr.ru/roditelyam/svobodnye-mesta")
            button2_2 = types.InlineKeyboardButton(text="Вопрос - ответ",
                                                   url="https://sch2100.mskobr.ru/roditelyam/vopros-otvet/")
            button2_3 = types.InlineKeyboardButton(text="Дошкольное образование",
                                                   url="https://sch2100.mskobr.ru/roditelyam/doshkolnoe-obrazovanie")
            button2_4 = types.InlineKeyboardButton(text="Все вопросы о питании",
                                                   url="https://sch2100.mskobr.ru/roditelyam/vse-voprosi-o-pitanii")
            button2_5 = types.InlineKeyboardButton(text="Психологическая поддержка ребёнка",
                                                   url="https://sch2100.mskobr.ru/roditelyam/psiholog-podderzhka-rebenka")
            markup1.add(button2_1, button2_2, button2_3, button2_4, button2_5)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup1)

        if (message.text == "Учащимся"):
            markup2 = types.InlineKeyboardMarkup(row_width=1)
            button3_1 = types.InlineKeyboardButton(text="Расписание, учебные периоды, каникулы",
                                                   url="https://sch2100.mskobr.ru/uchashimsya/raspisanie-kanikuly")
            button3_2 = types.InlineKeyboardButton(text="Государственная итоговая аттестация",
                                                   url="https://sch2100.mskobr.ru/uchashimsya/gia/eg")
            button3_3 = types.InlineKeyboardButton(text="Библиотека",
                                                   url="https://sch2100.mskobr.ru/uchashimsya/biblioteka")
            button3_4 = types.InlineKeyboardButton(text="Совет учащихся",
                                                   url="https://sch2100.mskobr.ru/uchashimsya/sovet-obuchayushchihsya")
            markup2.add(button3_1, button3_2, button3_3, button3_4)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup2)

        if (message.text == "Педагогам"):
            markup3 = types.InlineKeyboardMarkup(row_width=1)
            button4_1 = types.InlineKeyboardButton(text="Образовательные проекты",
                                                   url="https://sch2100.mskobr.ru/pedagogam/obrazovatelnye-proekty")
            button4_2 = types.InlineKeyboardButton(text="Вакансии", url="https://sch2100.mskobr.ru/pedagogam/vakansii")
            button4_3 = types.InlineKeyboardButton(text="Возможности МЭШ для педагогов",
                                                   url="https://sch2100.mskobr.ru/pedagogam/vozmozhnosti-MESH-dlya-pedagogov")
            button4_4 = types.InlineKeyboardButton(text="Конкурсы, олимпиады, конференции",
                                                   url="https://sch2100.mskobr.ru/pedagogam/konkursy-olimpiady-konferencii")
            button4_5 = types.InlineKeyboardButton(text="Профсоюзная организация",
                                                   url="https://sch2100.mskobr.ru/pedagogam/labor_organization")
            button4_6 = types.InlineKeyboardButton(text="Совет ветеранов педагогического труда",
                                                   url="https://sch2100.mskobr.ru/pedagogam/sovet-veteranov-ped-truda")
            markup3.add(button4_1, button4_2, button4_3, button4_4, button4_5, button4_6)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup3)

        if (message.text == "Дополнительное образование"):
            markup4 = types.InlineKeyboardMarkup(row_width=1)
            button5_1 = types.InlineKeyboardButton(text="Поиск кружков и секций",
                                                   url="https://sch2100.mskobr.ru/dop-obr/poisk-kruzhkov-i-sekcij")
            markup4.add(button5_1)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup4)

        if (message.text == "Проекты"):
            markup5 = types.InlineKeyboardMarkup(row_width=1)
            button6_1 = types.InlineKeyboardButton(text="Московские проекты",
                                                   url="https://sch2100.mskobr.ru/proekty/moskovskie-proekty")
            markup5.add(button6_1)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup5)

        if (message.text == "Предпрофессиональные классы"):
            markup6 = types.InlineKeyboardMarkup(row_width=1)
            button7_1 = types.InlineKeyboardButton(text="Кадетский класс",
                                                   url="https://sch2100.mskobr.ru/predprof/cadet-class/project-metrics")
            button7_2 = types.InlineKeyboardButton(text="Лингвистическая вертикаль",
                                                   url="https://sch2100.mskobr.ru/predprof/linguistic-vertical/project-metrics")
            markup6.add(button7_1, button7_2)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup6)

        if (message.text == "Сведения об образовательной организации"):
            markup18 = types.InlineKeyboardMarkup(row_width=1)
            button19_1 = types.InlineKeyboardButton(text="Основные сведения",
                                                    url="https://sch2100.mskobr.ru/info_edu/basics/#/")
            button19_2 = types.InlineKeyboardButton(text="Структура и органы управления образовательной организацией",
                                                    url="https://sch2100.mskobr.ru/o-nas/kontakty-podrazdelenij")
            button19_3 = types.InlineKeyboardButton(text="Документы",
                                                    url="https://sch2100.mskobr.ru/info_edu/all_docs/")
            button19_4 = types.InlineKeyboardButton(text="Образование",
                                                    url="https://sch2100.mskobr.ru/info_edu/education#/")
            button19_5 = types.InlineKeyboardButton(text="Руководство. Педагогический (научно-педагогический) состав",
                                                    url="https://sch2100.mskobr.ru/o-nas/pedagogicheskii-sostav")
            button19_6 = types.InlineKeyboardButton(
                text="Материально-техническое обеспечение и оснащенность образовательного процесса",
                url="https://sch2100.mskobr.ru/info_edu/support_and_equipment")
            button19_7 = types.InlineKeyboardButton(text="Платные образовательные услуги",
                                                    url="https://sch2100.mskobr.ru/o-nas/paid_services")
            button19_8 = types.InlineKeyboardButton(text="Финансово-хозяйственная деятельность",
                                                    url="https://sch2100.mskobr.ru/info_edu/financial_activity")
            button19_9 = types.InlineKeyboardButton(text="Вакантные места для приёма (перевода) обучающихся",
                                                    url="https://sch2100.mskobr.ru/roditelyam/svobodnye-mesta")
            button19_10 = types.InlineKeyboardButton(text="Образовательные стандарты и требования",
                                                     url="https://sch2100.mskobr.ru/info_edu/standards")
            button19_11 = types.InlineKeyboardButton(text="Стипендии и меры поддержки обучающихся",
                                                     url="https://sch2100.mskobr.ru/info_edu/grants")
            button19_12 = types.InlineKeyboardButton(text="Доступная среда",
                                                     url="https://sch2100.mskobr.ru/info_edu/accessible-environment")
            button19_13 = types.InlineKeyboardButton(text="Международное сотрудничество",
                                                     url="https://sch2100.mskobr.ru/info_edu/international-cooperation")
            button19_14 = types.InlineKeyboardButton(text="Платёжные реквизиты",
                                                     url="https://sch2100.mskobr.ru/info_edu/platezhnye_rekvizity/")
            button19_15 = types.InlineKeyboardButton(text="Публичный доклад руководителя",
                                                     url="https://sch2100.mskobr.ru/info_edu/report")
            button19_16 = types.InlineKeyboardButton(text="Организация питания в образовательной организации",
                                                     url="https://sch2100.mskobr.ru/roditelyam/vse-voprosi-o-pitanii")
            markup18.add(button19_1, button19_2, button19_3, button19_4, button19_5, button19_6, button19_7, button19_8,
                         button19_9, button19_10, button19_11, button19_12, button19_13, button19_14, button19_15,
                         button19_16)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup18)

        if (message.text == "Дополнительная информация"):
            markup19 = types.InlineKeyboardMarkup(row_width=1)
            button20_1 = types.InlineKeyboardButton(text="Классы", url="https://sch2100.mskobr.ru/info_add/classes")
            button21_2 = types.InlineKeyboardButton(text="Безопасность",
                                                    url="https://sch2100.mskobr.ru/info_add/security")
            button22_3 = types.InlineKeyboardButton(text="Противодействие коррупции",
                                                    url="https://sch2100.mskobr.ru/info_add/protivodejstvie-korrupcii")
            button23_4 = types.InlineKeyboardButton(text="Антикризисная команда",
                                                    url="https://sch2100.mskobr.ru/info_add/antikrizisnaya-komanda")
            button24_5 = types.InlineKeyboardButton(text="Защита персональных данных",
                                                    url="https://sch2100.mskobr.ru/info_add/personal_data")
            button25_6 = types.InlineKeyboardButton(text="Охрана труда",
                                                    url="https://sch2100.mskobr.ru/info_add/ohrana-truda")
            button26_7 = types.InlineKeyboardButton(text="Сведения о заработной плате",
                                                    url="https://sch2100.mskobr.ru/info_add/teachers_salary/")
            button27_8 = types.InlineKeyboardButton(text="Безопасность дорожного движения",
                                                    url="https://sch2100.mskobr.ru/info_add/traffic_safety")
            button28_9 = types.InlineKeyboardButton(text="Благоустройство территорий",
                                                    url="https://sch2100.mskobr.ru/info_add/land_improvements")
            markup19.add(button20_1, button21_2, button22_3, button23_4, button24_5, button25_6, button26_7, button27_8,
                         button28_9)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup19)

        if (message.text == "Электронные сервисы"):
            markup20 = types.InlineKeyboardMarkup(row_width=1)
            button31_1 = types.InlineKeyboardButton(text="Московская электронная школа",
                                                    url="https://sch2100.mskobr.ru/elektronnye_servisy/idnevnik")
            button32_2 = types.InlineKeyboardButton(text="Государственные услуги",
                                                    url="https://sch2100.mskobr.ru/elektronnye_servisy/gov_services")
            button33_3 = types.InlineKeyboardButton(text="Электронная карта в образовании",
                                                    url="https://moskvenok.mos.ru/")
            button34_4 = types.InlineKeyboardButton(text="Полезные ссылки",
                                                    url="https://sch2100.mskobr.ru/elektronnye_servisy/useful_links")
            markup20.add(button31_1, button32_2, button33_3, button34_4)
            bot.send_message(message.chat.id, 'Что именно требуется?', reply_markup=markup20)


@bot.callback_query_handler(func=lambda call: True)
def callback_query_handler(call):
    data = call.data
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    if "social_life" in data:
        markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton(text="test", url="https://www.google.com")
        markup.add(button)
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="текст сообщения", reply_markup=markup)

bot.polling()
