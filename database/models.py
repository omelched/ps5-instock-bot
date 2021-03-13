from datetime import datetime
from sqlalchemy.orm.exc import FlushError

from database import db


class User(db.Model):
    __tablename__ = 'user'

    _id = db.Column(db.Integer, primary_key=True)  # noqa
    first_name = db.Column(db.String(100), nullable=False)  # noqa
    username = db.Column(db.String(100))  # noqa
    registration_date = db.Column(db.DateTime, nullable=False, default=datetime.now())  # noqa

    def __repr__(self):
        return f"User:{self._id}, {self.first_name}"

    @classmethod
    def create_new(cls, _id, fn, un=None, rd=None):
        new_user = User(_id=_id, first_name=fn, username=un, registration_date=rd)
        try:
            db.session.add(new_user)
            db.session.commit()
            return True, new_user
        except FlushError as e:
            return False, e
        except Exception as e:
            raise e



