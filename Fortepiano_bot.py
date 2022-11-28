import time
import telebot
from telebot import types
import sqlite3
import datetime


token = '5621078456:AAHn78D0qMlcLiwldfHHAR2g9TL7L-sF6HM'
bot = telebot.TeleBot(token)


def db(item1=None, item2=None, item3=None, item4=None):
    conn = sqlite3.connect('Fortepiano-registrations.db')
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS List_of_registrations_fortepiano (id INTEGER PRIMARY KEY AUTOINCREMENT, date TIMESTAPE, name TEXT, age TEXT, colvo TEXT, number INT)''')
    cursor.execute('''INSERT INTO List_of_registrations_fortepiano (date, name, age, colvo, number) VALUES (?, ?, ?, ?, ?)''', (datetime.date.today(), item1, item2, item3, item4))
    conn.commit()


def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=3)
    markup_1 = types.InlineKeyboardButton(text='👨🏼‍💻 Информация обо мне', callback_data='1')
    markup_2 = types.InlineKeyboardButton(text='✅ Записаться на бесплатное занятие', callback_data='2')
    markup_3 = types.InlineKeyboardButton(text='🙋‍♂ Контакты', callback_data='3')
    markup_4 = types.InlineKeyboardButton(text='💲 Стоимость', callback_data='5')
    markup.add(markup_1, markup_3, markup_4, markup_2)
    return markup


def back_main():
    markup = types.InlineKeyboardMarkup()
    markup_1 = types.InlineKeyboardButton(text='🔙 Главное меню', callback_data='main')
    markup.add(markup_1)
    return markup


@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = main_menu()
    name = str(message.from_user.first_name)
    if message.from_user.last_name != None:
        name += ' ' + str(message.from_user.last_name)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGNstjWmT1KRbfEeAvuxilNCJPpzjsvQAC9wEAAhZCawo59nBvtGN_xCoE')
    time.sleep(2.0)
    bot.send_message(message.chat.id, f'Здравствуйте, <b>{name}!</b>\n'
                                      f'\n'
                                      f'Этот бот создан для Вашего удобства.\n'
                                      f'С его помощью Вы можете познакомиться со мной, узнать мои контакты, стоимость занятий '
                                      f'а также записаться на <b>бесплатное</b> пробное занятие по фортепиано в Минске в удобное '
                                      f'для Вас время!\n'
                                      f'\n'
                                      f'Оставьте заявку на <b>бесплатное</b> пробное занятие и я Вам перезвоню!',
                     parse_mode='html', reply_markup=keyboard)


@bot.message_handler(commands=['record'])
def record(message):
    new_reg(message)


@bot.message_handler(commands=['inform'])
def inform(message):
    info(message)


@bot.message_handler(commands=['contacts'])
def contact(message):
    contacts(message)

@bot.message_handler()
def info(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup_1 = types.InlineKeyboardButton(text='Больше информации на сайте 🔝', url='https://fortepiano-minsk.by')
    markup_2 = types.InlineKeyboardButton(text='🔙 Главное меню', callback_data='main')
    markup_3 = types.InlineKeyboardButton(text='✅ Записаться на бесплатное занятие', callback_data='2')
    markup.add(markup_1, markup_3, markup_2)
    bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/4keBszBvEmxjzw')
    time.sleep(2.0)
    bot.send_message(message.chat.id, '👩🏻 <b>Давайте познакомимся!</b> 👩🏻\n'
                                      'Меня зовут Дарья и я обучаю игре на фортепиано <b>уже 8 лет.</b> За это время <b>более 150-ти человек</b> под моим началом успешно достигли поставленных целей и освоили инструмент.\n'
                                      '\n'
                                      'Я закончила <b>Санкт-Петербургский институт культуры.</b> Умею проводить интересные и нескучные занятия для <b>детей и взрослых.</b> Имею твёрдое убеждение в том, что музыка - это в первую очередь счастье от того, что из-под твоих рук рождается звук. Восторг от <b>созданного тобой волшебства. Самостоятельно.</b> Ты можешь что-то крутое, чего не могут все остальные.\n'
                                      '\n'
                                      'В процессе обучения мы с Вами познакомимся с нотной грамотой, изучим основы сольфеджио и <b>сыграем Ваши любимые мелодии.</b> На каком бы уровне в данный момент Вы не находились, <b>уже через месяц занятий</b> прогресс будет заметным и существенным!', parse_mode='html')
    time.sleep(10.0)
    bot.send_message(message.chat.id, '<b>Почему мои ученики выбирают меня?</b>\n'
                                      '\n'
                                      '🎓 <b>УРОВЕНЬ ОБРАЗОВАНИЯ</b>\n'
                                      '- Санкт-Петербургский государственный <b>институт культуры</b>\n'
                                      '- Витебский государственный <b>музыкальный колледж</b> имени И.И. Соллертинского\n'
                                      '- Гимназия №3 города Витебска, <b>отделение фортепиано</b>\n'
                                      '\n'
                                      '💼 <b>ОПЫТ РАБОТЫ</b>\n'
                                      '- Государственные и частные музыкальные школы в Витебске, Минске и <b>Санкт-Петербурге</b>\n'
                                      '- Индивидуальный репетитор по фортепиано <b>с 2014 года</b>\n'
                                      '- За время работы научила играть на фортепиано <b>более 150-ти человек</b>\n'
                                      '\n'
                                      '👶🏻 <b>ДЕТСКОЕ ОБРАЗОВАНИЕ</b>\n'
                                      '- Возраст моих учеников <b>от 3-х лет</b>\n'
                                      '- На занятиях с детьми я использую специальные тематические материалы: стикеры, наклейки и другое, что позволяет эффективно <b>вовлечь ребёнка в процесс обучения</b>\n'
                                      '- Каждый ребёнок уникален, понимание этого простого принципа позволяет мне быстро находить общий язык с детьми, <b>вызывать у них доверие и желание учиться</b>\n'
                                      '- <b>Ваш ребёнок научится</b> чувствовать ритм, читать ноты, понимать теорию музыки и играть на фортепиано\n'
                                      '\n'
                                      '❤️ <b>ОСОБЫЙ ПОДХОД</b>\n'
                                      '- Работаю <b>на любом уровне:</b> новичок, любитель, профессионал\n'
                                      '- Освоение с нуля, повышение мастерства, помощь с домашними заданиями, дополнительные занятия, подготовка к поступлению в музыкальную школу - построим программу обучения <b>индивидуально для Вас</b>\n'
                                      '- Гибкое <b>расписание занятий</b>\n'
                                      '- С моей помощью <b>Вы сможете научится играть на инструменте</b> любые композиции, а <b>Ваш ребёнок поступит в музыкальную школу</b> или успешно сдаст выпускные экзамены\n'
                                      '<b>- Со мной Вам захочется заниматься снова и снова!</b>\n'
                                      '\n'
                                      '✅ <b>Запишитесь на БЕСПЛАТНОЕ пробное занятие сейчас и убедитесь сами, что играть на фортепиано просто и интересно!</b>', parse_mode='html', reply_markup=markup)


@bot.message_handler()
def price(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup_1 = types.InlineKeyboardButton(text='🔙 Главное меню', callback_data='main')
    markup_2 = types.InlineKeyboardButton(text='✅ Записаться на занятие', callback_data='2')
    markup.add(markup_1, markup_2)

    bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/NaY3XO0AeJqk-Q')
    time.sleep(2.0)
    bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/5FTizhyqmbCICw')
    time.sleep(2.0)
    bot.send_photo(message.chat.id, 'https://static.orgpage.ru/newsphotos/ab/ab89359f94b04702a97e1621a77d35b6.jpg', reply_markup=markup)


@bot.message_handler()
def contacts(message):
    back = back_main()
    markup = types.InlineKeyboardMarkup(row_width=3)
    markup_1 = types.InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/fortepiano_minsk/')
    markup_2 = types.InlineKeyboardButton(text='Вконтакте', url='https://vk.com/id184760662')
    markup_3 = types.InlineKeyboardButton(text='Website', url='https://fortepiano-minsk.by')
    markup.add(markup_1, markup_2, markup_3)
    bot.send_message(message.chat.id, 'Связаться со мной можно любым удобным для Вас способом', reply_markup=markup)
    time.sleep(3.0)
    bot.send_contact(message.chat.id, '+375297135563', 'Дарья', reply_markup=back)


@bot.message_handler(content_types=['text'])
def new_reg(message):

    msg = bot.send_message(message.chat.id, 'Как Вас зовут?')
    bot.register_next_step_handler(msg, name)


def name(message):
    global name_
    name_ = message.text

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1)
    markup_1 = types.KeyboardButton(text='Взрослый')
    markup_2 = types.KeyboardButton(text='Ребёнок дошкольного возраста')
    markup_3 = types.KeyboardButton(text='Ребёнок 6-17 лет')
    markup.add(markup_1, markup_2, markup_3)

    msg = bot.send_message(message.chat.id, 'Кто будет заниматься?', reply_markup=markup)
    bot.register_next_step_handler(msg, age)


def age(message):
    global age_
    age_ = message.text

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=3)
    markup_1 = types.KeyboardButton(text='1')
    markup_2 = types.KeyboardButton(text='2')
    markup_3 = types.KeyboardButton(text='3 и более')
    markup.add(markup_1, markup_2, markup_3)

    msg = bot.send_message(message.chat.id, 'Сколько занятий в неделю Вас бы устроило?', reply_markup=markup)
    bot.register_next_step_handler(msg, colvo)


def colvo(message):
    global colvo_
    colvo_ = message.text

    markup = types.ReplyKeyboardRemove(selective=False)

    msg = bot.send_message(message.chat.id, 'По какому номеру телефона с Вами можно связаться?', reply_markup=markup)
    bot.register_next_step_handler(msg, number)


def number(message):
    global number_
    number_ = message.text
    back = back_main()
    ID = message.chat.id

    db(name_, age_, colvo_, number_)

    bot.send_message(message.chat.id, f'<b>Спасибо! Ваша заявка зарегистрирована!</b>\n'
                                      f'Ждите звонка для уточнения всей необходимой информации 😁👍', parse_mode='html', reply_markup=back)

    bot.send_message(chat_id=959880478, text=f'<u><b>Новая запись с id {ID}</b></u>\n'
                                              f'\n'
                                              f'{datetime.datetime.now()}\n'
                                              f'Имя: <u>{name_}</u>\n'
                                              f'Номер телефона: <u>{number_}</u>\n'
                                              f'Заниматься будет <u>{age_}</u>\n'
                                              f'Планируют <u>{colvo_}</u> раз в неделю', parse_mode='html')
    bot.send_message(chat_id=2117898685, text=f'<u><b>Новая запись с id {ID}</b></u>\n'
                                              f'\n'
                                              f'{datetime.datetime.now()}\n'
                                              f'Имя: <u>{name_}</u>\n'
                                              f'Номер телефона: <u>{number_}</u>\n'
                                              f'Заниматься будет <u>{age_}</u>\n'
                                              f'Планируют <u>{colvo_}</u> раз в неделю', parse_mode='html')



@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    x = main_menu()
    if call.message:
        if call.data == '1':
            return info(call.message)
        if call.data == '2':
            return new_reg(call.message)
        if call.data == '3':
            return contacts(call.message)
        if call.data == '5':
            return price(call.message)
        if call.data == 'main':
            bot.send_message(call.message.chat.id, 'Что Вас интересует?', parse_mode='html', reply_markup=x)


if __name__ == '__main__':
    bot.polling(none_stop=True)
