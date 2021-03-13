from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import server
from utils import logger

try:
    _ = server.config['DATABASE_URL']
    server.config['SQLALCHEMY_DATABASE_URI'] = server.config['DATABASE_URL']
except KeyError:
    logger.error('Database URL NOT SET! Defaulting... ')
    server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../test.db'

try:
    _ = server.config['SQLALCHEMY_TRACK_MODIFICATIONS']
except KeyError:
    server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(server)
migrate = Migrate(server, db)

from database.models import BotUser  # noqa: e402
