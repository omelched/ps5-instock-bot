from apscheduler.schedulers.blocking import BlockingScheduler
import requests

from app import server

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def timed_job():
    requests.get('https://{}.herokuapp.com/notify/'.format(server.config['HEROKU_APP_NAME']))


sched.start()
