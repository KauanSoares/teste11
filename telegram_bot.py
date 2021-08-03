import telebot

bot = telebot.TeleBot("1894419896:AAHnLdn62xs3txrjRO32LxELEwSHsfyZ5OM")

@bot.message_handler(commands=['teste1', 'teste2', 'start'])

def send_welcome(message):
	bot.reply_to(message, ("recebi teste1"))


bot.polling()