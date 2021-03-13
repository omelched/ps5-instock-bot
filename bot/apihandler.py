from telebot.types import Message  # noqa
import traceback

from bot import bot
from database import User
from utils import logger


@bot.message_handler(commands=['addme'])
def add_me(message):
    try:
        result = User.create_new(message.from_user.id,
                                 message.from_user.first_name,
                                 message.chat.id,
                                 message.from_user.username)
    except Exception as e:
        bot.reply_to(message, f"Oops, there was an error")
        logger.error(e)
        logger.error(traceback.format_exc())
        return

    if result[0]:
        bot.reply_to(message, f"{result[1]} was created")
    else:
        bot.reply_to(message, f"You are already registered!")


@bot.message_handler(commands=['deleteme'])
def delete_me(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo(message: Message):
    bot.reply_to(message, message.text)
