import telebot
import quickstart
import time

bot = telebot.TeleBot("351574458:AAGqAUJMg7Lm_ujw7YfB1MD7HbFO5gQS-1Q")

time = time.strftime("%d.%m.%y----%H.%M.%S")
print(time + ": Ejecutando bot")

#id = 152045426

@bot.message_handler(commands=['todos'])
def send_welcome(message):
    print(time + ": Mostrando todos los datos '/todos'")
    bot.send_message(message.chat.id, "Mostrando todos los datos. \n apellidos, nombre (nº matrícula): fecha límite:")
    bot.send_message(message.chat.id, quickstart.todos())

@bot.message_handler(commands=['buscarMat'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Introduzca el número de matrícula.")
    mat = ""
    @bot.message_handler(commands=[mat])
    def send_welcome(message):
        print(time + ": Mostrando la matrícula")
        bot.send_message(message.chat.id, mat)
bot.polling()
input()