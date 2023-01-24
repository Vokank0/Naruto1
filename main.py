import telebot
from telebot import types
bot = telebot.TeleBot("5649328540:AAH_9WbhiyRThSUR2Lm4_bAWocZuKdRGpNA", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/2x2ru")
    item2 = types.KeyboardButton("/QTV # DVOA 'ua'")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Щоб скачати серію  для початку вибери озвучку.')
    bot.send_message(message.chat.id, 'Після цього вибири сезон.')
    bot.send_message(message.chat.id, 'Та напиши номер серії.', reply_markup=markup)
@bot.message_handler(commands=["2x2ru"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item3 = types.KeyboardButton("/1 сезон")
    item4 = types.KeyboardButton("/2 сезон")
    markup.add(item3, item4)


    bot.send_message(message.chat.id, 'Обери потрібний сезон', reply_markup=markup)
@bot.message_handler(commands=["2"])
def one(message):
    bot.send_message(message.chat.id, 'Напиши серію')
    @bot.message_handler()
    def o(message):
        if message.text == '460':
            bot.send_message(message.chat.id, 'Серія завантажується')












bot.polling(none_stop=True)