import requests
import traceback

from bot import bot
from database import BotUser
from utils import logger

r = requests.get('https://ps5status.ru/api/data')
payload = [{'name': r.json()['data']['shops'][shop]['name'], 'link': r.json()['data']['shops'][shop]['normal_link']}
           for shop in r.json()['data']['shops'].keys()
           if r.json()['data']['shops'][shop]['normal_info']['available'] is True]

if payload:
    try:
        users = BotUser.query.all()
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
        exit()

    for user in users:
        bot.send_notification(user.chat_id, payload)
