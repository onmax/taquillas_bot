import telebot

import quickstart
import time
from telebot import types
import json
bot = telebot.TeleBot("351574458:AAGqAUJMg7Lm_ujw7YfB1MD7HbFO5gQS-1Q")

time = time.strftime("%d/%m/%y || %H:%M:%S: ")
print(time + "Ejecutando bot")

#id = 152045426
@bot.message_handler(commands=['help'])
def send_welcome(message):
    print(time + "Mostrando ayuda. '/help'")
    bot.send_message(message.chat.id, "Mostrando todos los comandos: \n" +
                     "<b>/todos</b>: Muestra información de todos los usuarios INFO: apellidos, nombre (número matrícula): fecha límite. \n"+
                     "<b>/buscarMat numeroMatricula</b>: Muestra información del usuario con dicha matrícula. Es necesario introducir el número de matrícula después del comando.",
                     parse_mode= "HTML")

@bot.message_handler(commands=['todos'])
def send_welcome(message):
    page = message.text.split()
    if(len(page)==1):
        print(time + "Mostrando todos los datos '/todos'. Pg: 1")
        bot.send_message(chat_id=message.chat.id,
                         text="Mostrando todos los datos. \n apellidos, nombre (nº matrícula): fecha límite. \n Buscando en pg 1" )
    else:
        print(time + "Mostrando todos los datos '/todos'. Pg: " + page[1])
        bot.send_message(chat_id= message.chat.id,
                         text = "Mostrando todos los datos. \n apellidos, nombre (nº matrícula): fecha límite. \n Buscando en pg " + page[1])
    markup = types.ReplyKeyboardMarkup(one_time_keyboard= True, resize_keyboard= True)
    if(len(page) == 1 or page[1]== '1'):
        page = 1
        markup.add('/todos 2')
    else:
        page = int(page[1])
        anterior = '/todos ' + str(page - 1)
        posterior = '/todos ' + str(page + 1)
        markup.add(anterior, posterior)
    bot.send_message(message.chat.id, quickstart.todos(page), parse_mode="HTML", reply_markup= markup)


@bot.message_handler(commands=['buscarMat'])
def send_welcome(message):
    if(len(message.text) < 17):
        bot.send_message(message.chat.id, "Por favor, introduzca el comando de nuevo acompañado por un espacio y un número de matrícula con 6 dígitos. No hace falta escribirlo con letra. \n /buscarMat 000000")
    else:
        numero_matricula = message.text.split()
        print(time + "Buscando para la matrícula " + numero_matricula[1] + " '/buscarMat'")
        respuesta = "Buscando para la matrícula: " + numero_matricula[1]
        bot.send_message(message.chat.id, respuesta)
        bot.send_message(message.chat.id, quickstart.buscar_matricula(numero_matricula[1]), parse_mode="HTML")

@bot.message_handler(commands=['buscarNom'])
def send_welcome(message):
    if(len(message.text) < 17):
        bot.send_message(message.chat.id, "Por favor, introduzca el comando de nuevo acompañado por un espacio y el nombre de la persona que se busca. \n /buscarNom Almudena")
    else:
        nombre_a_buscar = message.text.split()
        print(time + ": Buscando para la matrícula " + nombre_a_buscar[1] + " '/buscarMat'")
        respuesta = "Buscando para la matrícula: " + nombre_a_buscar[1]
        bot.send_message(message.chat.id, respuesta)
        bot.send_message(message.chat.id, quickstart.buscar_nombre(nombre_a_buscar[1]))

bot.polling()
input()

