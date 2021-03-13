import telebot  # noqa

from app import server

try:
    _TOKEN = server.config['BOT_TOKEN']
except KeyError:
    _TOKEN = ''


class PS5Bot(telebot.TeleBot):

    def send_notification(self, chat_id, payload):

        if not payload:
            return False

        if not chat_id:
            return False

        text = ''
        for shop in payload:
            text = text + f'PS5 is available in shop [{shop["name"]}]({shop["link"]})\n\r'

        self.send_message(chat_id, text)
        return True


bot = PS5Bot(_TOKEN)

from bot import apihandler, routes  # noqa
