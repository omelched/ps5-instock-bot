import random
import datetime
from telebot.types import Message

from app import bot, logger


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_all(message: Message):
    bot.reply_to(message, message.text)
