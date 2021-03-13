from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import traceback

from app import server
from bot import bot
from database import BotUser
from utils import logger


sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def timed_job():
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
            return traceback.format_exc(), 500

        for user in users:
            bot.send_notification(user.chat_id, 'Test notification')


sched.start()
