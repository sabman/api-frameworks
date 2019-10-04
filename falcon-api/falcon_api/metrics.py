import io
import os
import uuid
import mimetypes

import falcon
import json

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.config import sqlalchemy_engine


class Resource(object):
    def on_post(self, req, resp):
        print("req.context['data']", req.context['data'])
        if req.context['data']:

            metric_value = req.context['data']['metric_value']
            model_id = req.context['data']['model_id']

            try:
                sqlalchemy_engine.execute(
                    "INSERT INTO falcon_user (metric_value, model_id) VALUES(%s, %s)",
                    (metric_value, model_id))
            except:
                resp.status = falcon.HTTP_500
            else:
                resp.status = falcon.HTTP_201

        else:
            resp.status = falcon.HTTP_400
