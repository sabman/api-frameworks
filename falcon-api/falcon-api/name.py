import io
import os
import uuid
import mimetypes

import falcon
import json

from sqlalchemy import create_engine
import psycopg2

from dotenv import load_dotenv
from pathlib import Path  # python3 only
env_path = Path(__file__).parents[1] / '.env'
print(env_path)
load_dotenv(dotenv_path=env_path)


class Resource(object):
    def on_get(self, req, resp):
        doc = {'name': 'Usman Haider'}

        # Create a JSON representation of the resource
        resp.body = json.dumps(doc, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        name = req.get_param("name", required=True)

        conn = psycopg2.connect(host=os.getenv("HOST"),
                                port=os.getenv("PORT"),
                                user=os.getenv("PG_USER"),
                                password=os.getenv("PASSWORD"),
                                database="api_frameworks")  # To remove slash

        cursor = conn.cursor()
        cursor.execute("INSERT INTO test_frameworks (test_data) VALUES(%s)",
                       (name, ))
        conn.commit()
        cursor.close()
        conn.close()

        resp.body = json.dumps({"response": "resource created"},
                               ensure_ascii=False)
        resp.status = falcon.HTTP_201
