# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, LargeBinary
from sqlalchemy.dialects.postgresql import JSONB

from app.model import Base
from app.config import UUID_LEN
from app.utils import alchemy
from sqlalchemy.orm import relationship


class User(Base):
    user_id = Column(Integer, primary_key=True)
    email = Column(String(320), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    token = Column(String(255), nullable=False)
    children = relationship("Metric")

    # intentionally assigned for user related service such as resetting password: kind of internal user secret key
    sid = Column(String(UUID_LEN), nullable=False)

    def __repr__(self):
        return "<User(user_id='%s', email='%s', token='%s')>" % (
            self.user_id, self.email, self.token)

    @classmethod
    def get_id(cls):
        return User.user_id

    @classmethod
    def find_one_by_sid(cls, session, sid):
        return session.query(User).filter(User.sid == sid).one()

    @classmethod
    def find_by_email(cls, session, email):
        return session.query(User).filter(User.email == email).one()

    FIELDS = {"email": str, "token": str}

    FIELDS.update(Base.FIELDS)
