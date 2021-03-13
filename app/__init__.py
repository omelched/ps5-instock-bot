from flask import Flask

from utils import config

server = Flask(__name__)
server.config.from_object(config)

