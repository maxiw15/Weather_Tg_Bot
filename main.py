import telebot
from yandex import weather_want_know


token = "5572813010:AAF18_DlYPryC6-GXcIswRG2q5QTZfWlavA"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['чепопогоде'])
def send_welcome(message):
    answer = weather_want_know()
    bot.reply_to(message, answer)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "доступная команда - /чепопогоде")


bot.infinity_polling()
