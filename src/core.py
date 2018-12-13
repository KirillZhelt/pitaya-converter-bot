from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
import os


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hi, it is Pitaya Converter.")

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def numbers(bot, update):
    # TODO: should decide what to do with negative numbers
    bot.send_message(chat_id=update.message.chat_id, text=str(bin(int(update.message.text))))


if os.path.isfile("token"):
    with open("token") as token_file:
        private_token = token_file.readline()

# TODO: handle invalid token
updater = Updater(token=private_token)
dispatcher = updater.dispatcher
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

start_handler = CommandHandler("start", start)
numbers_handler = MessageHandler(Filters.regex("^(-?[1-9]+\d*)$|^0$"), numbers)
echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(numbers_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
