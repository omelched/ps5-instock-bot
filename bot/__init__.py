import telebot  # noqa

from app import server

try:
    _TOKEN = server.config['BOT_TOKEN']
except KeyError:
    _TOKEN = ''

bot = telebot.TeleBot(_TOKEN)


from bot import apihandler, routes  # noqa

