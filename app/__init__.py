from flask import Flask

from utils import config

server = Flask(__name__)
server.config.from_object(config)

try:
    _ = server.config['HEROKU_APP_NAME']
except KeyError
    server.config['HEROKU_APP_NAME'] = 'ps5-instock-bot'
