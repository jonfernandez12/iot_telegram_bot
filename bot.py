#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import requests
import json

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hola!Por favor, escribe /instrucciones en el chat para comenzar')

def comprobarLuz(update, context):
    """Send a message when the command /start is issued."""
    status=requests.get("https://alleta.ii.uam.es/api/states/light.lampara_derecha",
                  json={"entity_id": "light.lampara_derecha"},
                  headers={
                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0NDZmMWY1OTVjNjM0MTczYmRlODFiZTczMzVlMDA"
                                       "2NiIsImlhdCI6MTYwNjgzMzU1MSwiZXhwIjoxOTIyMTkzNTUxfQ.7mjoelXEMmRpAgJpeurDkjZA9-Gxj6DzhFlyDzhi61A",
                      "Content-Type": "application/json"})
    
    data = json.loads(status.content)
    print(data['state'])
    update.message.reply_text(data['state'])

def comprobarHorno(update, context):
    """Send a message when the command /start is issued."""
    status=requests.get("https://alleta.ii.uam.es/api/states/light.lampara_izquierda",
                  json={"entity_id": "light.lampara_izquierda"},
                  headers={
                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0NDZmMWY1OTVjNjM0MTczYmRlODFiZTczMzVlMDA"
                                       "2NiIsImlhdCI6MTYwNjgzMzU1MSwiZXhwIjoxOTIyMTkzNTUxfQ.7mjoelXEMmRpAgJpeurDkjZA9-Gxj6DzhFlyDzhi61A",
                      "Content-Type": "application/json"})
    
    data = json.loads(status.content)
    print(data['state'])
    update.message.reply_text(data['state'])

def comprobarVitro(update, context):
    """Send a message when the command /start is issued."""
    status=requests.get("https://alleta.ii.uam.es/api/states/light.luz_lectura",
                  json={"entity_id": "light.luz_lectura"},
                  headers={
                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0NDZmMWY1OTVjNjM0MTczYmRlODFiZTczMzVlMDA"
                                       "2NiIsImlhdCI6MTYwNjgzMzU1MSwiZXhwIjoxOTIyMTkzNTUxfQ.7mjoelXEMmRpAgJpeurDkjZA9-Gxj6DzhFlyDzhi61A",
                      "Content-Type": "application/json"})
    
    data = json.loads(status.content)
    print(data['state'])
    update.message.reply_text(data['state'])


def comprobarPuerta(update, context):
    """Send a message when the command /start is issued."""
    status=requests.get("https://alleta.ii.uam.es/api/states/binary_sensor.puerta_1_ias_zone",
                  json={"entity_id": "binary_sensor.puerta_1_ias_zone"},
                  headers={
                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0NDZmMWY1OTVjNjM0MTczYmRlODFiZTczMzVlMDA"
                                       "2NiIsImlhdCI6MTYwNjgzMzU1MSwiZXhwIjoxOTIyMTkzNTUxfQ.7mjoelXEMmRpAgJpeurDkjZA9-Gxj6DzhFlyDzhi61A",
                      "Content-Type": "application/json"})
    
    data = json.loads(status.content)
    print(data['state'])
    update.message.reply_text(data['state'])


def alterarLuz(update, context):
    message = update['message']['text']
    status=requests.get("https://alleta.ii.uam.es/api/states/light.lampara_derecha",
                  json={"entity_id": "light.lampara_derecha"},
                  headers={
                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0NDZmMWY1OTVjNjM0MTczYmRlODFiZTczMzVlMDA"
                                       "2NiIsImlhdCI6MTYwNjgzMzU1MSwiZXhwIjoxOTIyMTkzNTUxfQ.7mjoelXEMmRpAgJpeurDkjZA9-Gxj6DzhFlyDzhi61A",
                      "Content-Type": "application/json"})
    
    data = json.loads(status.content)
    estado = data['state']
    if estado == 'on' and message =='/encenderLuz' :
        update.message.reply_text("Ya esta encendido")
    elif estado == 'off' and message == '/apagarLuz':
        update.message.reply_text("Ya esta apagado")
    elif estado == 'on' and message == '/apagarLuz':
        requests.post("https://alleta.ii.uam.es/api/services/light/turn_off",
                  json={"entity_id": "light.lampara_derecha"},
                  headers={
                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0NDZmMWY1OTVjNjM0MTczYmRlODFiZTczMzVlMDA"
                                       "2NiIsImlhdCI6MTYwNjgzMzU1MSwiZXhwIjoxOTIyMTkzNTUxfQ.7mjoelXEMmRpAgJpeurDkjZA9-Gxj6DzhFlyDzhi61A",
                      "Content-Type": "application/json"})

        update.message.reply_text("Apagado")
    elif estado == 'off' and message == '/encenderLuz':
        requests.post("https://alleta.ii.uam.es/api/services/light/turn_on",
                  json={"entity_id": "light.lampara_derecha", "brightness_pct": "100",
                        "rgb_color": [255, 182, 109]},
                  headers={
                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0NDZmMWY1OTVjNjM0MTczYmRlODFiZTczMzVlMDA"
                                       "2NiIsImlhdCI6MTYwNjgzMzU1MSwiZXhwIjoxOTIyMTkzNTUxfQ.7mjoelXEMmRpAgJpeurDkjZA9-Gxj6DzhFlyDzhi61A",
                      "Content-Type": "application/json"})

        update.message.reply_text("Encendido")

def alterarHorno(update, context):
    message = update['message']['text']
    status=requests.get("https://alleta.ii.uam.es/api/states/light.lampara_izquierda",
                  json={"entity_id": "light.lampara_izquierda"},
                  headers={
                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0NDZmMWY1OTVjNjM0MTczYmRlODFiZTczMzVlMDA"
                                       "2NiIsImlhdCI6MTYwNjgzMzU1MSwiZXhwIjoxOTIyMTkzNTUxfQ.7mjoelXEMmRpAgJpeurDkjZA9-Gxj6DzhFlyDzhi61A",
                      "Content-Type": "application/json"})
    
    data = json.loads(status.content)
    estado = data['state']
    if estado == 'on' and message =='/encenderHorno' :
        update.message.reply_text("Ya esta encendido")
    elif estado == 'off' and message == '/apagarHorno':
        update.message.reply_text("Ya esta apagado")
    elif estado == 'on' and message == '/apagarHorno':
        requests.post("https://alleta.ii.uam.es/api/services/light/turn_off",
                  json={"entity_id": "light.lampara_izquierda"},
                  headers={
                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0NDZmMWY1OTVjNjM0MTczYmRlODFiZTczMzVlMDA"
                                       "2NiIsImlhdCI6MTYwNjgzMzU1MSwiZXhwIjoxOTIyMTkzNTUxfQ.7mjoelXEMmRpAgJpeurDkjZA9-Gxj6DzhFlyDzhi61A",
                      "Content-Type": "application/json"})
        update.message.reply_text("Apagado")
    elif estado == 'off' and message == '/encenderHorno':
        requests.post("https://alleta.ii.uam.es/api/services/light/turn_on",
                  json={"entity_id": "light.lampara_izquierda", "brightness_pct": "100"},
                  headers={
                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0NDZmMWY1OTVjNjM0MTczYmRlODFiZTczMzVlMDA"
                                       "2NiIsImlhdCI6MTYwNjgzMzU1MSwiZXhwIjoxOTIyMTkzNTUxfQ.7mjoelXEMmRpAgJpeurDkjZA9-Gxj6DzhFlyDzhi61A",
                      "Content-Type": "application/json"})
        update.message.reply_text("Encendido")

def alterarVitro(update, context):
    message = update['message']['text']
    status=requests.get("https://alleta.ii.uam.es/api/states/light.luz_lectura",
                  json={"entity_id": "light.luz_lectura"},
                  headers={
                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0NDZmMWY1OTVjNjM0MTczYmRlODFiZTczMzVlMDA"
                                       "2NiIsImlhdCI6MTYwNjgzMzU1MSwiZXhwIjoxOTIyMTkzNTUxfQ.7mjoelXEMmRpAgJpeurDkjZA9-Gxj6DzhFlyDzhi61A",
                      "Content-Type": "application/json"})
    
    data = json.loads(status.content)
    estado = data['state']
    if estado == 'on' and message =='/encenderVitro' :
        update.message.reply_text("Ya esta encendido")
    elif estado == 'off' and message == '/apagarVitro':
        update.message.reply_text("Ya esta apagado")
    elif estado == 'on' and message == '/apagarVitro':
        requests.post("https://alleta.ii.uam.es/api/services/light/turn_off",
                  json={"entity_id": "light.luz_lectura"},
                  headers={
                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0NDZmMWY1OTVjNjM0MTczYmRlODFiZTczMzVlMDA"
                                       "2NiIsImlhdCI6MTYwNjgzMzU1MSwiZXhwIjoxOTIyMTkzNTUxfQ.7mjoelXEMmRpAgJpeurDkjZA9-Gxj6DzhFlyDzhi61A",
                      "Content-Type": "application/json"})
        update.message.reply_text("Apagado")
    elif estado == 'off' and message == '/encenderVitro':
        requests.post("https://alleta.ii.uam.es/api/services/light/turn_on",
                  json={"entity_id": "light.luz_lectura","brightness_pct": "10", "kelvin":"1800"},
                  headers={
                      "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0NDZmMWY1OTVjNjM0MTczYmRlODFiZTczMzVlMDA"
                                       "2NiIsImlhdCI6MTYwNjgzMzU1MSwiZXhwIjoxOTIyMTkzNTUxfQ.7mjoelXEMmRpAgJpeurDkjZA9-Gxj6DzhFlyDzhi61A",
                      "Content-Type": "application/json"})
        update.message.reply_text("Encendido")


def instrucciones(update, context):
    #la lampara de la izquierda hará de horno
    #la lampara de lectura hará de vitro
    """Send a message when the command /start is issued."""
    instrucionBot= """Buenas querido usuario
    Este bot ofrece la posibilidad de comprobar el estado de distintos electrodomesticos o luces de su casa.
    A su vez, puede alterar el estado de los mismos facilmente desde el bot.
    
    Instrucciones para comprobar:
    /comprobarLuz :  comprueba el estado de la luz
    /comprobarHorno : comprueba el estado del horno 
    /comprobarVitro : comprueba el estado de la vitro
    /comprobarPuerta:  comprueba el estado de la puerta
    
    Instrucciones para encender
    /encenderLuz :  enciende la luz
    /encenderHorno : enciende el horno
    /encenderVitro : enciende la vitro
    
    Instrucciones para apagar:
    /apagarLuz :  apagar la lu
    /apagarHorno : apagar el horno
    /apagarVitro : apagar la vitro"""

    update.message.reply_text(instrucionBot)

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("333710124:AAGy7BjH965pRiXh4Hz3FAEnRLME-oxURxc", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("comprobarLuz", comprobarLuz))
    dp.add_handler(CommandHandler("comprobarHorno", comprobarHorno))
    dp.add_handler(CommandHandler("comprobarVitro", comprobarVitro))
    dp.add_handler(CommandHandler("comprobarPuerta", comprobarPuerta))


    dp.add_handler(CommandHandler("encenderLuz", alterarLuz))
    dp.add_handler(CommandHandler("encenderHorno", alterarHorno))
    dp.add_handler(CommandHandler("encenderVitro", alterarVitro))

    dp.add_handler(CommandHandler("apagarLuz", alterarLuz))
    dp.add_handler(CommandHandler("apagarHorno", alterarHorno))
    dp.add_handler(CommandHandler("apagarVitro", alterarVitro))

    dp.add_handler(CommandHandler("instrucciones", instrucciones))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
