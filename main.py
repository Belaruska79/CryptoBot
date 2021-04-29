import telebot
from config import TOKEN, exchanger
from extensions import Convertor, ConverterException



bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = r'''/values - список доступных валют  ,
валюта1 валюта2 сумма   перевод суммы из валюты1 в валюту2'''
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:\n'
    text += "\n".join(exchanger.keys())
    bot.reply_to(message, text)
    try:
        if len(value) != 3:
            raise valueError ('Неверное количество знаков')
        val1, val2, amount=values

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split('')
    values = list(map(str.lower, values))
    try
        result = Convertor.get_price(values)
    except ConverterException as e:
        bot.reply_to(message, 'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, 'Не удалось обработать команду \n{e}')
   else:
        text = f'Цена{values[0]} {values[1]} в {values[2} -- {result} {exchanger[values[1]]}'
        bot.reply_to(message, text)


bot.polling(none_stop=True, interval=0)

