import io
import os
import uuid
import mimetypes

import falcon
import json

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.config import sqlalchemy_engine


def raiser(ex):
    raise ex


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

        try:
            try:
                name = req.get_header('username') if req.get_header(
                    'username') else raiser(Exception)
            except Exception:
                response = {"error": "Bad Request"}
                resp.status = falcon.HTTP_400
                return

            try:
                sqlalchemy_engine.execute(
                    "INSERT INTO falcon_user (username) VALUES(%s)", (name, ))
            except:
                response = {"error": "Interanl Server Error"}
                resp.status = falcon.HTTP_500
                return
            else:
                response = {"response": "Resource Created"}
                resp.status = falcon.HTTP_201
                return
        finally:
            resp.body = json.dumps(response, ensure_ascii=False)
