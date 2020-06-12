import telebot
from telebot import types

bot = telebot.TeleBot("1044670898:AAH777c-8AFvBDCA7O3g_aJxSsbwhMzccP8")


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Knop1 = types.KeyboardButton("Інформація")
    Knop2 = types.KeyboardButton("Контакти")
    Knop3 = types.KeyboardButton("ЗНО-2020")
    Knop4 = types.KeyboardButton("Спецiальностi")
    Knop5 = types.KeyboardButton("Звязок з адміністрацією")
    Knop6 = types.KeyboardButton("Перелік питань")
    markup.add(Knop1, Knop2, Knop3, Knop4, Knop5, Knop6)
    bot.send_message(message.chat.id, ' Привіт шановні колеги та студенти. Ви зайшли на Бот ХДПК, що вас цікавить?',
                     reply_markup=markup)

@bot.message_handler(commands=['questions'])
def tratata(message):
     markup = types.InlineKeyboardMarkup(row_width=1)
     Knop1 = types.InlineKeyboardButton(text='Коли день відкритих дверей?', callback_data="question1")
     Knop2 = types.InlineKeyboardButton(text='Які спеціальності є?', callback_data="question2")
     Knop3 = types.InlineKeyboardButton(text='Коли можна подавати документи?', callback_data="question5")
     Knop4 = types.InlineKeyboardButton(text='Які документи потрібні для вступу?', callback_data="question3")
     Knop5 = types.InlineKeyboardButton(text='Чи є підкурси?', callback_data="question4")
     markup.add(Knop1, Knop2, Knop3, Knop4, Knop5)
     bot.send_message(message.chat.id, "Перелік питань", reply_markup=markup)



@bot.message_handler(content_types=['text'])
def HOHOHo(message):
        if message.text == 'Інформація':
            markup = types.InlineKeyboardMarkup(row_width=2)
            Knon = types.InlineKeyboardButton(text='Розклад занять',
                                              url='https://drive.google.com/file/d/1pdmZ-0eO1i_r0QRVkm7Jq-AhpWfHiP2Q/view?usp=sharing')
            knop1 = types.InlineKeyboardButton(text='CISCO', callback_data="Info")
            markup.add(Knon, knop1)
            knop2 = types.InlineKeyboardButton(text='АБІТУРІЄНТУ', callback_data="Info1")
            markup.add(knop2)
            knop3 = types.InlineKeyboardButton(text='ІСТОРІЯ КОЛЕДЖУ', callback_data="Info2")
            markup.add(knop3)
            bot.send_message(message.chat.id, "ІНФОРМАЦІЯ ХДПК", reply_markup=markup)
        elif message.text == 'Звязок з адміністрацією':
            markup = types.InlineKeyboardMarkup(row_width=2)
            Knon = types.InlineKeyboardButton(text='Адмiн', url='https://t.me/UncleGrek')
            markup.add(Knon)
            bot.send_message(message.chat.id, "Натисніть на кнопку Адмін і задайте своє питання", reply_markup=markup)
        elif message.text == "Контакти":
            markup = types.InlineKeyboardMarkup(row_width=2)
            Knop1 = types.InlineKeyboardButton(text='Офіційний сайт', url='http://xemttc.at.ua/')
            Knop2 = types.InlineKeyboardButton(text='Ми в Facebook', url='https://m.facebook.com/hdpk.xemttc/')
            Knop3 = types.InlineKeyboardButton(text='На мапі', url='https://www.google.com.ua/maps/place'
                                                                   '/Дмитриевская+ул.,+26,+Харьков,'
                                                                   '+Харьковская+область,+61000/@49.985748,36.215953,'
                                                                   '17z/data=!3m1!1e3!4m2!3m1!1s0x4127a057bca8e20d:0xace6b6fe741cb7d6?hl=ru')
            Knop4 = types.InlineKeyboardButton(text='YouTube канал',
                                               url='https://www.youtube.com/channel/UC5RRje9zxKyq2cPXmvPsBMw')
            markup.add(Knop1, Knop2, Knop3, Knop4)
            bot.send_message(message.chat.id,
                             "🏘Адрес коледжу: \nм. Харків, вул. Дмитрівська 26 \n ☎️Телефони: \n (057)712-07-41 \n ("
                             "057)734-98-13 \n (057)712-47-85",
                             reply_markup=markup)
        elif message.text == "ЗНО-2020":
            bot.send_message(message.chat.id, "Учні, слухачі, слухачі, студенти закладів загальної середньої, "
                                              "професійної, професійно-технічної, вищої освіти, які в 2020 році "
                                              "завершують здобуття повної загальної середньої освіти складають "
                                              "державну підсумкову атестацію у формі ЗНО з трьох предметів: "
                                              "українська мова і література (українська мова), математика або історія "
                                              "України (період ХХ – початок ХХІ століття), один з навчальних "
                                              "предметів (за вибором здобувача освіти):  біологія, географія, фізика, "
                                              "хімія, іноземні мови.     Результати ЗНО з української мови і "
                                              "літератури (українська мова), математики або історії України (період "
                                              "ХХ – початок ХХІ століття) можуть зараховуватися як результат ДПА для "
                                              "студентів ЗВО, які скористалися правом повторного складання атестації  "
                                              "у формі ДПА.Особи, які вже здобули повну загальну середню освіту у "
                                              "минулі роки також можуть стати учасниками ЗНО-2020. Кожен "
                                              "зареєстрований учасник ЗНО має право скласти тести не більш як із "
                                              "чотирьох предметів")
        elif message.text == "Спецiальностi":
            markup = types.InlineKeyboardMarkup(row_width=2)
            Knop1 = types.InlineKeyboardButton(text='123', callback_data="test1")
            Knop2 = types.InlineKeyboardButton(text='141', callback_data="test2")
            Knop3 = types.InlineKeyboardButton(text='151', callback_data="test3")
            Knop4 = types.InlineKeyboardButton(text='192', callback_data="test4")
            Knop5 = types.InlineKeyboardButton(text='273', callback_data="test5")
            markup.add(Knop1, Knop2, Knop3, Knop4, Knop5)
            bot.send_message(message.chat.id, "Спецiальностi🧐", reply_markup=markup)
        elif message.text == "Перелік питань":
            markup = types.InlineKeyboardMarkup(row_width=1)
            Knop1 = types.InlineKeyboardButton(text='Коли день відкритих дверей?', callback_data="question1")
            Knop2 = types.InlineKeyboardButton(text='Які спеціальності є?', callback_data="question2")
            Knop3 = types.InlineKeyboardButton(text='Коли можна подавати документи?', callback_data="question5")
            Knop4 = types.InlineKeyboardButton(text='Які документи потрібні для вступу?', callback_data="question3")
            Knop5 = types.InlineKeyboardButton(text='Чи є підкурси?', callback_data="question4")
            markup.add(Knop1, Knop2, Knop3, Knop4, Knop5)
            bot.send_message(message.chat.id, "Перелік питань🤓", reply_markup=markup)
       
        else:
            bot.send_message(message.chat.id, "Невідома комманда. Напишіть /questions, щоб задати питання")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "test1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="📝123.Комп’ютерна  інженерія \n 📌Спеціалізація: \n 📌Обслуговування комп'ютерних систем і мереж (9 кл.)\n 💡Більш детальна інформація про спеціальності на http://xemttc.at.ua")
        elif call.data == "test2":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="📝Електроенергетика, електротехніка та електромеханіка \n 📌Спеціалізації \n 📌Електропостачання (9 кл.) \n 📌Монтаж і експлуатація електроустаткування підприємств і цивільних споруд (9 кл.) \n 📌Обслуговування та ремонт електроустаткування автомобілів і тракторів (9 кл.)\n 💡Більш детальна інформація про спеціальності на http://xemttc.at.ua")
        elif call.data == "test3":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="📝151.Автоматизація та комп’ютерно-інтегровані технології (9 кл.). \n 📌Спеціалізації: \n 📌Обслуговування інтелектуальних інтегрованих систем (9 кл.). \n 📌Монтаж, обслуговування та ремонт автоматизованих систем керування рухом на залізничному транспорті (9 кл.). \n 📌Обслуговування та ремонт пристроїв електрозв'язку на транспорті (9 кл., 11 кл.)\n 💡Більш детальна інформація про спеціальності на http://xemttc.at.ua")
        elif call.data == "test4":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="📝192.Будівництво та цивільна інженерія \n 📌Спеціалізації: \n 📌Монтаж, обслуговування устаткування і систем газопостачання (9 кл.) \n 📌Монтаж і обслуговування внутрішніх санітарно-технічних систем і вентиляції (9 кл.)\n 💡Більш детальна інформація про спеціальності на http://xemttc.at.ua")
        elif call.data == "test5":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="📝273. Залізничний транспорт \n 📌Спеціалізація: \n 📌Монтаж, обслуговування та ремонт автоматизованих систем керування рухом на залізничному транспорті\n 💡Більш детальна інформація про спеціальності на http://xemttc.at.ua")
        elif call.data == "question1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="📝273. Залізничний транспорт \n 📌Спеціалізація: \n 📌Монтаж, обслуговування та ремонт автоматизованих систем керування рухом на залізничному транспорті")
        elif call.data == "question2":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="📝273. Залізничний транспорт \n 📌Спеціалізація: \n 📌Монтаж, обслуговування та ремонт автоматизованих систем керування рухом на залізничному транспорті")
        elif call.data == "question3":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="📝273. Залізничний транспорт \n 📌Спеціалізація: \n 📌Монтаж, обслуговування та ремонт автоматизованих систем керування рухом на залізничному транспорті")
        elif call.data == "question4":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="📝273. Залізничний транспорт \n 📌Спеціалізація: \n 📌Монтаж, обслуговування та ремонт автоматизованих систем керування рухом на залізничному транспорті")
        elif call.data == "question5":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="📝273. Залізничний транспорт \n 📌Спеціалізація: \n 📌Монтаж, обслуговування та ремонт автоматизованих систем керування рухом на залізничному транспорті")
        elif call.data == "Info":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="АКАДЕМІЯ CISCO У ХДПК \n З 25  лютого 2019  року при Харківському державному політехнічному коледжі розпочала роботу Академія CISCO \nБажаючим пройти навчання та отримати сертифікат міжнародного зразка CISCO \n Звертатися до викладачів-інструкорів Академії CISCO:  \nВеличко Марина Валеріївна \nДегтяр Артем Андрійович \n Задара Оксана Анатоліївна \n Ярмола Оксана Сергіївна \nВи отримаєте практичні знання в усіх основоположних аспектах глобальних інформаційних мереж;\nВи зможете самостійно займатися створенням і побудовою локальних і глобальних мереж;\nВи придбаєте навички роботи з реальним обладнанням.\nПриєднуйтесь до курсу на будь-якому етапі своєї кар’єри.\nКУРСИ АКАДЕМІЇ CISCO ПРИ ХДПК:\nIT Essentials:PC Hardware and  Software - Апаратне та програмне забезпечення для ПК\nIntroduction to the Internet of Everything - Введення до всеосяжного Інтернету\nCybersecurity Essentials - Основи кібербезпеки\nIntroduction to Packet Tracer - Введення до Packet Tracer\nIntroduction to loT - Введення до Інтернету речей\nIntroduction to Cybersecurity - Введення до кібербезпеки\nNetwork Essentials - Основи комп'ютерних мереж")
        elif call.data == "Info1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Вступники подають документи: \n❗️ УВАГА! Прийом на навчання здійснюється лише за наявності паспорту(id картки). \n📎 Заяву в паперовій формі; \n📎 Документ, що посвідчує особу (дозволяється в 2017 році прийом на навчання до коледжу на основі свідоцтва про народження вступника); \n📎 Документ про освіту та додаток до нього; \n📎 Медичну довідку ф. 086-О та довідку про щеплення; \n📎 6 фотокарток 3x4 см; \n📎 Довідку про ідентифікаційний код. \n📌 Для випускників 9 класів проводяться екзамени з української мови та математики.")
        elif call.data == "Info2":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=" Теперішній час\n У 1989 році в технікумі, вперше з 1952 року, коли остаточно склався набір профілюючих спеціальностей, було відкрито нову спеціальність «Монтаж і експлуатація електроустаткування підприємств і цивільних будівель». Вперше за всю історію ХЕМТТС знову відкрита спеціальність не мала залізничної спрямованості. З цього моменту починається розширення напрямків, за якими технікум веде підготовку, що визначило його вигляд в останні десятиліття і сприяло його збереженню і розвитку як самостійного навчального закладу.\n У 1991 році технікум був перепідпорядкований Міністерству освіти України\n З очолюванням технікуму в 1997 році Віталієм Миколайовичем Немченко обсяг спеціальностей, за якими ведеться підготовка, різко розширюється. У 1998 році на базі ХЕМТТС був створений комплекс «Трансбуделектро» ( «Трансстройелектро»), до складу якого входять, з одного боку, школи і ПТУ, які допомагають формувати контингент вступників, а з іншого боку, вищі навчальні заклади різного рівня акредитації та промислові підприємства міста і області, які надають студентам місця для проходження виробничої практики. З цього ж року технікум входить на правах юридичної особи в сім навчальних науково-виробничих комплексів вищих навчальних закладів ІІІ-ІV рівня акредитації.\n У 2001 році відкривається восьма спеціальність «Обслуговування комп'ютерних та інтелектуальних систем і мереж», що стала логічним продовженням докорінної модернізації комп'ютерного парку технікуму, послідовно ведеться з 1997 року. Тоді ж на додаток до денною та заочною формами навчання був відкритий екстернат і відділення курсової підготовки за робітничими спеціальностям\n З 2005 року заняття першого курсу в групах, сформованих на базі загальної середньої освіти, проводяться в п'ятому навчальному корпусі на проспекті Любові Малої, 4-а (суміщеному з будівлею гуртожитку).\n Наказом Міністерства освіти і науки України № 440 від 20 квітня 2016 року технікум був перейменований в Харківський державний політехнічний коледж.")
bot.polling(none_stop=True)
