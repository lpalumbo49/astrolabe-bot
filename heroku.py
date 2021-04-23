from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import json
import logging
import os


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = os.environ['TELEGRAM_TOKEN']

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def get_fact(update, context):
    fact = requests.get('https://uselessfacts.jsph.pl/random.json?language=en').json()
    
    logger.info('Sending "%s" to "%s"', fact, update)
    update.message.reply_text(fact['text'])

def main():
    logger.info('Hola!')

    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('fact', get_fact))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
