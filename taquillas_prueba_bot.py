import telebot
import quickstart
import time

bot = telebot.TeleBot("351574458:AAGqAUJMg7Lm_ujw7YfB1MD7HbFO5gQS-1Q")

time = time.strftime("%d/%m/%y || %H:%M:%S")
print(time + ": Ejecutando bot")

#id = 152045426

@bot.message_handler(commands=['help'])
def send_welcome(message):
    print(time + ": Mostrando ayuda. '/help'")
    bot.send_message(message.chat.id, "Mostrando todos los comandos: \n" +
                     "/todos: Muestra información de todos los usuarios INFO: apellidos, nombre (número matrícula): fecha límite. \n"+
                     "/buscarMat numeroMatricula: Muestra información del usuario con dicha matrícula. Es necesario introducir el número de matrícula después del comando.")

@bot.message_handler(commands=['todos'])
def send_welcome(message):
    print(time + ": Mostrando todos los datos '/todos'")
    bot.send_message(message.chat.id, "Mostrando todos los datos. \n apellidos, nombre (nº matrícula): fecha límite.")
    bot.send_message(message.chat.id, quickstart.todos())

@bot.message_handler(commands=['buscarMat'])
def send_welcome(message):
    if(len(message.text) < 17):
        bot.send_message(message.chat.id, "Por favor, introduzca el com160065ndo de nuevo acompañado por un espacio y un número de matrícula con 6 dígitos. No hace falta escribirlo con letra. \n /buscarMat 000000")
    else:
        numero_matricula = message.text.split()
        print(time + ": Buscando para la matrícula " + numero_matricula[1] + " '/buscarMat'")
        respuesta = "Buscando para la matrícula: " + numero_matricula[1]
        bot.send_message(message.chat.id, respuesta)
        bot.send_message(message.chat.id, quickstart.buscar_matricula(numero_matricula[1]))
bot.polling()
input()

