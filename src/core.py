from telegram.ext import Updater, CommandHandler

import logging
import os


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Дима фуРс петуч")


if os.path.isfile("..\\token"):
    with open("..\\token") as token_file:
        private_token = token_file.readline()

updater = Updater(token=private_token)
dispatcher = updater.dispatcher
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()

