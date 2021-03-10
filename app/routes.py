from app import server, bot
from flask import request
import telebot


@server.route('/' + server.config['BOT_TOKEN'], methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook_index():
    bot.remove_webhook()
    bot.set_webhook(url="https://ps5-instock-bot.herokuapp.com//{}".format(server.config['BOT_TOKEN']))
    return "!", 200