import telebot
from telebot import types

from api_key import API_KEY

key = API_KEY

bot = telebot.TeleBot(key)



@bot.message_handler(commands=['start'])
def greetings(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('❓Contacts')
    btn2 = types.KeyboardButton('🔧Test functions')
    markup.add(btn1,btn2)
    bot.reply_to(message,f'Hi, {message.from_user.first_name} {message.from_user.last_name}!',
    reply_markup = markup)

@bot.message_handler(content_types=['text'])
def reply_to_text(message):
    if message.text == '❓Contacts':
        photo = open('image/di_caprio.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,'https://github.com/AlexeyProg')
    elif message.text == '🔧Test functions':
        markup_tests = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn_audio = types.KeyboardButton('send audio')
        markup_tests.add(btn_audio)
        bot.send_message(message.chat.id, '🔧Test functions', reply_markup=markup_tests)
        

        # audio = open('audio/rihanna.mp3','rb')
        # bot.send_audio(message.chat.id, audio)
bot.infinity_polling()

