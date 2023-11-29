import telebot

bot = telebot.TeleBot('6344534257:AAFri7Nwl0YGGF_uT3NzCjJ6gDoeLry9QIo')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '*Попытка выучить английский*', parse_mode='Markdown')


@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, '*кошка на английском*', parse_mode='Markdown')


@bot.message_handler(commands=['go'])
def main(message):
    bot.send_message(message.chat.id, '*язык на английском*', parse_mode='Markdown')


bot.infinity_polling()