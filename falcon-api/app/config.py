# -*- coding: utf-8 -*-

import os
import configparser
from itertools import chain

from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy import create_engine

load_dotenv(verbose=True)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

BRAND_NAME = "Falcon REST API Template"

SECRET_KEY = "xs4G5ZD9SwNME6nWRWrK_aq6Yb9H8VJpdwCzkTErFPw="
UUID_LEN = 10
UUID_ALPHABET = "".join(map(chr, range(48, 58)))
TOKEN_EXPIRES = 3600

APP_ENV = os.getenv("APP_ENV") or "local"  # or 'live' to load live

user = os.getenv("user")
password = os.getenv("password")
POSTGRES_HOST = os.getenv("host")
database = os.getenv("database")
port = os.getenv("port")

DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{POSTGRES_HOST}:{port}/{database}"

DB_ECHO = True if os.getenv("echo") == "yes" else False
DB_AUTOCOMMIT = True

LOG_LEVEL = os.getenv("level")


def get_engine(uri):
    options = {
        "pool_recycle": 3600,
        "pool_size": 10,
        "pool_timeout": 30,
        "max_overflow": 30,
        "echo": DB_ECHO,
        "execution_options": {
            "autocommit": DB_AUTOCOMMIT
        },
    }
    return create_engine(uri, **options)
