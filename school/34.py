# 5182389599:AAH-_EAQVuBvNwGxN0Qt_7NAkXiTpCL_9qM
import telebot

bot = telebot.TeleBot("5182389599:AAH-_EAQVuBvNwGxN0Qt_7NAkXiTpCL_9qM")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет меня зовут Бот давай с тобой познакомимся")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	# bot.reply_to(message, message.text)
    if message.text=="privet":
        bot.reply_to(message, "privet rad znakomstvu")
    else:
        bot.reply_to(message, "я не понимаю тебя")

bot.infinity_polling()