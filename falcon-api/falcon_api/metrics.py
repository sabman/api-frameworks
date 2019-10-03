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
    def on_post(self, req, resp):

        try:
            try:
                metric_value = req.get_header(
                    'metric_value') if req.get_header(
                        'metric_value') else raiser(Exception)
                model_id = req.get_header('model_id') if req.get_header(
                    'model_id') else raiser(Exception)

            except Exception:
                status_code = falcon.HTTP_400
                return

            try:
                sqlalchemy_engine.execute(
                    "INSERT INTO falcon_user (metric_value, model_id) VALUES(%s, %s)",
                    (metric_value, model_id))
            except:
                status_code = falcon.HTTP_500
                return
            else:
                status_code = falcon.HTTP_201
                return
        finally:
            resp.status = status_code
