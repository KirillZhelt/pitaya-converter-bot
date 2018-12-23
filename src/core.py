from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
import os

from numtools import Number, NumeralSystem

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hi, it is Pitaya Converter.")

def process_number(bot, update):
    number = Number(update.message.text)
    
    message = str()
    for numeral_system, convert_function in Number.convert_functions.items():
        if number.numeral_system != numeral_system:
            message += convert_function(number)
            message += "\n" 

    bot.send_message(chat_id=update.message.chat_id, text=message)


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

if os.path.isfile("token"):
    with open("token") as token_file:
        private_token = token_file.readline()

    updater = Updater(token=private_token)

    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", start)
    text_handler = MessageHandler(Filters.text, process_number)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(text_handler)

    updater.start_polling()
    updater.idle()
else:
    logging.error("can't find the token file")
