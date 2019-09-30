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

        try:
            try:
                username = req.get_param('username') if req.get_param(
                    'username') else raiser(Exception)
            except Exception:
                response = {"error": "Bad Request"}
                resp.status = falcon.HTTP_400
                return
            try:
                result = sqlalchemy_engine.execute(
                    "SELECT * FROM falcon_user WHERE username=%s",
                    (username, ))
            except:
                response = {"error": "Interanl Server Error"}
                resp.status = falcon.HTTP_500
                return
            else:
                for row in result:
                    response = {"id": row["id"], "username": row["username"]}

                resp.status = falcon.HTTP_200
                return
            try:
                result = sqlalchemy_engine.execute("SELECT * FROM falcon_user")
            except:
                response = {"error": "Interanl Server Error"}
                resp.status = falcon.HTTP_500
                return
            else:
                response = []
                for row in result:
                    response.append({
                        'id': row['id'],
                        'username': row['username']
                    })
                resp.status = falcon.HTTP_200
                return
        finally:
            resp.body = json.dumps(response, ensure_ascii=False)

    def on_post(self, req, resp):

        try:
            try:
                username = req.get_header('username') if req.get_header(
                    'username') else raiser(Exception)
            except Exception:
                response = {"error": "Bad Request"}
                resp.status = falcon.HTTP_400
                return

            try:
                sqlalchemy_engine.execute(
                    "INSERT INTO falcon_user (username) VALUES(%s)",
                    (username, ))
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
