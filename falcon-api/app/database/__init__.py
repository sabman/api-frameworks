# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker, scoped_session

from app import log
from app import config

LOG = log.get_logger()

db_session = scoped_session(sessionmaker())

LOG.info("Connecting to database..")
engine = config.get_engine(config.DATABASE_URL)


def init_session():
    db_session.configure(bind=engine)

    from app.model import Base

    Base.metadata.create_all(engine)
