#importarmos librerias y el archivo quickstart
import telebot
import time
import quickstart
#Para poder usar el teclado interactivo
from telebot import types

#Guardamos en una variable nuestro bot
bot = telebot.TeleBot("351574458:AAGqAUJMg7Lm_ujw7YfB1MD7HbFO5gQS-1Q")



#Comando de help, info
@bot.message_handler(commands=['help', 'info'])
def send_welcome(message):
    #Separamos el mensaje del usuario en un array
    help = message.text.split()

    #Si el usuario no ha escrito nada después de help o info se ejecuta el if
    if(len(help) == 1):
        #Mostramos en la consola que se ejecutado /help
        print(message.from_user.first_name + "-> " + time.strftime("%d/%m/%y || %H:%M:%S: ") + "Mostrando ayuda. '/help'")
        #Mensaje para el usuario con los comandos.
        bot.send_message(message.chat.id, "Mostrando todos los comandos: \n" +
                         "<b>/todos</b>: Muestra información de todos los usuarios INFO: apellidos, nombre (número matrícula)\n"+
                         "<b>/matricula numero_matricula</b>: Muestra información del usuario con dicha matrícula. Es necesario introducir el número de matrícula después del comando. \n"
                         "<b>/nombre Nombre_a_buscar</b>: Muestra todos los usuarios en la BBDD que coinciden con ese nombre. Es necesario introducir el nombre después del comando. \n"
                         "<b>/apellido Apellido_a_buscar</b>: Muestra todos los usuarios en la BBDD que coinciden con el apellido buscado. Es necesario introducir el apellido después del comando.",
                         parse_mode= "HTML")
        #Preparamos el teclado de acción rápida
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add('/help todos', '/help matricula');markup.add('/help nombre', '/help apellido')
        #Ejecutamos el teclado
        bot.send_message(message.chat.id, "Más información de los comandos:", parse_mode="HTML", reply_markup=markup)
    else:
        #Si la segunda parte del /help es igual a todos o "all"
        if(help[1] == "todos" or help[1] == "all"):
            #Mostramos la información del comando /todos
            bot.send_message(message.chat.id, "<b>/todos, /all</b>: Muestra información de todos los usuarios.\n" +
                                              "INFO: apellidos, nombre (número matrícula): fecha límite. " +
                             "\nSe muestran los datos en grupos de 50 en 50. \nPara acceder a un grupo, escribir: <i>/todos numero_pagina</i>", parse_mode="HTML")
            #Lo imprimos por la consola
            print(message.from_user.first_name + "-> " + time.strftime("%d/%m/%y || %H:%M:%S: ") + "Mostrando /help todos")
            #Preparamos el teclado
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            markup.add('/todos 1', '/todos 2'); markup.add('/todos 3', '/todos 4')
            #Ejecutamos el teclado
            bot.send_message(message.chat.id, "Acción rápida:", parse_mode="HTML", reply_markup=markup)
        #La segunda parte la ponemos en minusuculas y quitamos la s (para evitar poner como parametro buscarMat, buscarNom, buscarApellido matriculas, nombres, apellidos)
        help[1] = help[1].lower()
        help[1] = help[1].replace("s", "")

        # Si la segunda parte del /help es igual a matricula o matr o buscar matr
        if (help[1] == "matricula" or  help[1] == "buscarmat" or help[1] == "matr"):
            #Mostramos la información del comando /matricula
            bot.send_message(message.chat.id,
                             "<b>/matricula, /matr, /buscarmat, /buscarMat</b>: Muestra información del usuario con dicha matrícula. Es necesario introducir el número de matrícula después del comando." +
                             "\nEjemplo: <i>/marticula Numero_matricula</i>",parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
            #Lo imprimos por la consola
            print(message.from_user.first_name + "-> " + time.strftime("%d/%m/%y || %H:%M:%S: ") + "Mostrando /help matricula")

        # Si la segunda parte del /help es igual a nombre o buscarnom
        if (help[1] == "nombre" or help[1] == "buscarnom"):
            #Mostramos la información del comando /matricula
            bot.send_message(message.chat.id,
                             "<b>/nombre, /buscarNom, /buscarnom</b>: Muestra todos los usuarios en la BBDD que coinciden con ese nombre. Es necesario introducir el nombre después del comando." +
                             "\nEjemplo: <i>/nombre Nombre_a_buscar</i>", parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
            #Lo imprimos por la consola
            print(message.from_user.first_name + "-> " + time.strftime("%d/%m/%y || %H:%M:%S: ") + "Mostrando /help nombre")
        # Si la segunda parte del /help es igual a apellido o buscarapellido
        if (help[1] == "apellido" or help[1] == "buscarapellido"):
            #Mostramos la información del comando /matricula
            bot.send_message(message.chat.id,
                             "<b>/apellido, /buscarape, /buscarApe, /apellidos</b>: Muestra todos los usuarios en la BBDD que coinciden con ese apellido. Es necesario introducir el apellido después del comando." +
                             "\nEjemplo: <i>/apellido Apellido_a_buscar</i>", parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
            #Lo imprimos por la consola
            print(message.from_user.first_name + "-> " + time.strftime("%d/%m/%y || %H:%M:%S: ") + "Mostrando /help apellido")

#Comando de todos, all
@bot.message_handler(commands=['todos', 'all'])
def send_welcome(message):
    #Separamos el mensaje del usuario en un array, cada palabra en una posicion Ej: ['/todos', '2']
    page = message.text.split()
    #Si el usuario solo ha puesto /todos o /all
    if(len(page)==1):
        #Lo imprimos por la consola
        print(message.from_user.first_name + "-> " + time.strftime("%d/%m/%y || %H:%M:%S: ") + "Mostrando todos los datos '/todos'. Pg: 1")
        #Mandamos al usuario una introducción de lo que va a aparecer, en este caso página 1
        bot.send_message(chat_id=message.chat.id,
                         text="Buscando datos.\n Buscando en pg 1",
                         reply_markup=types.ReplyKeyboardRemove())
    else:
        #Imprimimos por consola
        print(message.from_user.first_name + "-> " + time.strftime("%d/%m/%y || %H:%M:%S: ") + "Mostrando todos los datos '/todos'. Pg: " + page[1])
        #Mandamos al usuario lo que va a parecer y le informamos de la pagina donde está realizando la búsqueda
        bot.send_message(chat_id= message.chat.id,
                         text = "Mostrando todos los datos. \n apellidos, nombre (nº matrícula): fecha límite. \n Buscando en pg " + page[1],
                         reply_markup=types.ReplyKeyboardRemove())
    #Preparamos el teclado, si se encuentra en la pagina 1 solo muestra /todos 2
    markup = types.ReplyKeyboardMarkup(one_time_keyboard= True, resize_keyboard= True)
    if(len(page) == 1 or page[1]== '1'):
        page = 1
        markup.add('/todos 2')
    else:
        page = int(page[1])
        anterior = '/todos ' + str(page - 1)
        posterior = '/todos ' + str(page + 1)
        markup.add(anterior, posterior)
    #Ejecutamos el teclado
    bot.send_message(message.chat.id, quickstart.todos(page), parse_mode="HTML", reply_markup=markup)

#comando para buscar matrículas
@bot.message_handler(commands=['buscarMat', 'buscarmat', 'matr', 'matricula'])
def send_welcome(message):
    #Separamos el mensaje en un array
    numero_matricula = message.text.split()
    #Si el usuario no ha especificado la matricula a buscar, salta el error, o bien si el usuario ha escrito mal la matrícula
    if(len(numero_matricula) == 1 or len(numero_matricula[1]) < 6):
        bot.send_message(message.chat.id, "Por favor, introduzca el comando de nuevo acompañado por un espacio y un número de matrícula con 6 dígitos. No hace falta escribirlo con letra. \n <i>/matricula 000000</i>",
                         parse_mode="HTML",
                         reply_markup=types.ReplyKeyboardRemove())
    else:
        respuesta = "Buscando para la matrícula: " + numero_matricula[1]
        print(message.from_user.first_name + "-> " + time.strftime("%d/%m/%y || %H:%M:%S: ") + respuesta)
        bot.send_message(message.chat.id, respuesta, parse_mode="HTML",reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, quickstart.buscar_matricula(numero_matricula[1], time, message), parse_mode="HTML")

@bot.message_handler(commands=['buscarNom', 'buscarnom', 'nombre'])
def send_welcome(message):
    nombre = message.text.split()
    if 1 == len(nombre):
        bot.send_message(message.chat.id, "Por favor, introduzca un nombre para buscar como se muestra a continuacion:\n<i>/nombre Pepe</i>",
                         parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
    else:
        respuesta = "Buscando para el nombre: <b>" + nombre[1] + "</b>"
        print(message.from_user.first_name + "-> " + time.strftime("%d/%m/%y || %H:%M:%S: ") + respuesta.replace("<b>", "").replace("</b>", ""))
        bot.send_message(message.chat.id, respuesta, parse_mode="HTML",reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, quickstart.buscar_nombre(nombre[1]), parse_mode="HTML")

@bot.message_handler(commands=['buscarApe', 'buscarape', 'apellidos', 'apellido'])
def send_welcome(message):
    appellido = message.text.split()
    if 1 == len(appellido):
        bot.send_message(message.chat.id, "Por favor, introduzca un nombre para buscar como se muestra a continuacion:\n"
                                          "<i>/appellido Pepe</i>", parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
    else:
        apellido_total = appellido[1]
        if(len(appellido) == 3):
            apellido_total += " " + appellido[2]
        respuesta = "Buscando para el apellido: <b>" + apellido_total + "</b>"
        print(message.from_user.first_name + "-> " + time.strftime("%d/%m/%y || %H:%M:%S: ") + respuesta.replace("<b>", "").replace("</b>", ""))
        bot.send_message(message.chat.id, respuesta, parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, quickstart.buscar_apellido(apellido_total), parse_mode="HTML")

#Comando por si no existe un comando
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message.from_user.first_name + "-> " + time.strftime("%d/%m/%y || %H:%M:%S: ") + message.text)
    bot.send_message(message.chat.id, "Mmm, <b>no es un comando</b>. \nMira los comando posibles en /help",
                     parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())


print(time.strftime("%d/%m/%y || %H:%M:%S: ") + "Ejecutando bot")

bot.polling()
input()

