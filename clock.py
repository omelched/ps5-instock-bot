from apscheduler.schedulers.blocking import BlockingScheduler
import requests

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def timed_job():
    requests.get('http://0.0.0.0:5000/notify/')


sched.start()
