import telebot
from telebot import types

token = "5093812074:AAFcex6kCYylSEu7UqsbYhSv1YrSNTlfKU4"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу погонять", "/help")
    bot.send_message(message.chat.id, 'Привет, давно тебя не было в уличных гонках.', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею поднимать настроение командой /cat, \n'
                                      'могу рассказать кто ты есть командой /iam, \n'
                                      'а так же передавать привет командой /hi.')


@bot.message_handler(commands=['iam'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вы самый красивый человек во Вселенной!')


@bot.message_handler(commands=['hi'])
def start_message(message):
    bot.send_message(message.chat.id, 'Приветствую, Ваше Превосходительство!')


@bot.message_handler(commands=['cat'])
def start_message(message):
    bot.send_photo(message.chat.id, photo=open('cat.jpg', 'rb'))


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу погонять":
        bot.send_message(message.chat.id, 'Погнали, мистер')
    elif message.text.lower() == 'хочу пиццу':
        bot.send_message(message.chat.id, 'НЕТ!')
    elif message.text.lower() == 'кто':
        bot.send_message(message.chat.id, 'Кто я? А может быть ты? кто?')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю, сынок!')




if __name__ == "__main__":
    bot.polling(none_stop=True, timeout=123)
