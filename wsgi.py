import os
from app import server
from bot import bot
from utils import logger

if __name__ == '__main__':

    if server.config['ON_HEROKU']:
        logger.info("running on HEROKU")
        server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
    else:
        logger.info("running on local + longpolling")
        bot.remove_webhook()
        bot.polling(none_stop=True)

