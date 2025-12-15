#7663753264:AAHC9aUSaXCCkKO3038zyv555hsJXA5X248

import telebot
from random import randint

TOKEN = "ТВІЙ_ТОКЕН_СЮДИ"

bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Як ся маєш?")

# Обробка будь-якого іншого тексту
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    match randint(1, 4):
        case 1:
            bot.send_message(message.chat.id, f"Хороше повідомлення: ''{message.text}''")
        case 2:
            bot.send_message(message.chat.id, f"Да, да, і мені цікаво тебе слухати.")

# Запускаємо бота
bot.polling(none_stop=True)