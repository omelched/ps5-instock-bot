from datetime import datetime
from sqlalchemy.orm.exc import FlushError
from sqlalchemy.exc import IntegrityError

from database import db


class BotUser(db.Model):
    __tablename__ = 'bot_user'

    _id = db.Column(db.Integer, primary_key=True)  # noqa
    first_name = db.Column(db.String(100), nullable=False)  # noqa
    username = db.Column(db.String(100))  # noqa
    registration_date = db.Column(db.DateTime, nullable=False, default=datetime.now())  # noqa
    chat_id = db.Column(db.String(100), nullable=False)  # noqa

    def __repr__(self):
        return f"User:{self._id}, {self.first_name}"

    @classmethod
    def create_new(cls, _id, fn, ci, un=None, rd=None):
        new_user = BotUser(_id=_id, first_name=fn, username=un, registration_date=rd, chat_id=ci)
        try:
            db.session.add(new_user)
            db.session.commit()
            return True, new_user
        except (FlushError, IntegrityError) as e:
            return False, e
        except Exception as e:
            raise e



