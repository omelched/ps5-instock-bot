import os

from flask import Flask

from utils import config, logger
from app.bot import PS5Bot

server = Flask(__name__)
server.config.from_object(config)

bot = PS5Bot(server.config['BOT_TOKEN'])

from app import routes, apihandler  # noqa: e402

if server.config['ON_HEROKU']:
    logger.info("running on HEROKU")
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
else:
    logger.info("running on local + longpolling")
    bot.remove_webhook()
    bot.polling(none_stop=True)

if __name__ == '__main__':
    server.run(debug=True)
