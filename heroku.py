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

PORT = int(os.environ.get('PORT', '8443'))
TOKEN = '849546896:AAHHyH1UvCRW85jBH9jgCGSUyBvyP9X65Sw'
APP_NAME = 'https://astrolabe-bot.herokuapp.com/'

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def get_fact(update, context):
    fact = requests.get('https://uselessfacts.jsph.pl/random.json?language=en').json()
    
    logger.info('Sending "%s" to "%s"', fact, update)
    update.message.reply_text(fact['text'])

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('fact', get_fact))

    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                      port=int(PORT),
                      url_path=TOKEN,
                      webhook_url=APP_NAME + TOKEN)
    
    updater.idle()


if __name__ == '__main__':
    main()
