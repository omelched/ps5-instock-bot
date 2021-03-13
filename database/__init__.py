from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import server

try:
    _ = server.config['DATABASE_URL']
except KeyError:
    server.config['SQLALCHEMY_DATABASE_URI'] = server.config['DATABASE_URL']

try:
    _ = server.config['SQLALCHEMY_TRACK_MODIFICATIONS']
except KeyError:
    server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(server)
migrate = Migrate(server, db)

from database.models import User  # noqa: e402
