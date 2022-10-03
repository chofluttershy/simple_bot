import telebot
from telebot import types

token = "5245262878:AAFOY1aj7MEKEtqg_9TBWZU0VpWu0pEGbYE"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("хочу мультик", "/help")
    bot.send_message(message.chat.id, 'Привет, По.', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Кунг-фу панда /panda, \n'
                                        'Спанч-Боб /patrick, \n'
                                        'Кик Бутовски /kick.')


@bot.message_handler(commands=['panda'])
def start_message(message):
    bot.send_photo(message.chat.id, photo=open('panda.jpg', 'rb'))


@bot.message_handler(commands=['patrick'])
def start_message(message):
    bot.send_photo(message.chat.id, photo=open('patrick.jpg', 'rb'))


@bot.message_handler(commands=['kick'])
def start_message(message):
    bot.send_photo(message.chat.id, photo=open('kick.jpg', 'rb'))


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "карлсон":
        bot.send_message(message.chat.id, 'Давай пошалим!!!')
    elif message.text.lower() == 'суперсемейка':
        bot.send_message(message.chat.id, 'НЕТ!')
    elif message.text.lower() == 'хочу мультик':
        bot.send_message(message.chat.id, 'Хоти!')
    elif message.text.lower() == 'скуби-ду':
        bot.send_message(message.chat.id, 'Сам ты пёс! ')
    else:
        bot.send_message(message.chat.id, 'Я не знаю такiй мультик')


if __name__ == "__main__":
    bot.polling(none_stop=True, timeout=123)