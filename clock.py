from apscheduler.schedulers.blocking import BlockingScheduler
import requests

from app import server
from bot import bot

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def timed_job():
    r = requests.get('https://ps5status.ru/api/data')
    payload = [{'name': r.json()['data']['shops'][shop]['name'], 'link': r.json()['data']['shops'][shop]['normal_link']}
               for shop in r.json()['data']['shops'].keys()
               if r.json()['data']['shops'][shop]['normal_info']['available'] is True]

    if payload:
        requests.get('https://{}.herokuapp.com/notify/'.format(server.config['HEROKU_APP_NAME']))


sched.start()
