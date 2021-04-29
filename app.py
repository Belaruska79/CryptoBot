import telebot

TOKEN = r"1747673799:AAFZAO27LmaTQHylv01R2LJ3dqs57kttrcE"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
   text = r'''\values - список доступных валют ,
валюта1 валюта2 сумма   перевод суммы из валюты1 в валюту2'''
bot.send_message(message.chat.id, text)

bot.polling()

