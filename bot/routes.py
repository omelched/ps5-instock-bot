from flask import request
import telebot  # noqa
import traceback

from app import server
from bot import bot, _TOKEN
from database import BotUser
from utils import logger


@server.route('/' + _TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook_index():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}.herokuapp.com//{}".format(server.config['HEROKU_APP_NAME'],
                                                              server.config['BOT_TOKEN']))
    return "!", 200


@server.route("/notify/")
def notify_all_users():
    try:
        users = BotUser.query.all()
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
        return traceback.format_exc(), 500

    for user in users:
        if not bot.send_notification(user.chat_id, 'Test notification'):
            return 'no', 500

    return "Test notification", 200
