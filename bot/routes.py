from flask import request
import telebot  # noqa

from app import server
from bot import bot, _TOKEN


@server.route('/' + _TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook_index():
    bot.remove_webhook()
    bot.set_webhook(url="https://ps5-instock-bot.herokuapp.com//{}".format(server.config['BOT_TOKEN']))
    return "!", 200
