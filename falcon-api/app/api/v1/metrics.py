# -*- coding: utf-8 -*-

import re
import falcon

from sqlalchemy.orm.exc import NoResultFound
from cerberus import Validator
from cerberus.errors import ValidationError

from app import log
from app.api.common import BaseResource
from app.utils.hooks import auth_required
from app.utils.auth import encrypt_token, hash_password, verify_password, uuid
from app.model import Metric, User
from app.errors import (
    AppError,
    InvalidParameterError,
    UserNotExistsError,
    PasswordNotMatch,
)

LOG = log.get_logger()


class Collection(BaseResource):
    """
    Handle for endpoint: /api/v1/metric/
    """
    @falcon.before(auth_required)
    def on_post(self, req, res):
        session = req.context["session"]
        print("req.context[`auth_user`]", req.context["auth_user"])
        metric_req = req.context["data"]
        print("data", metric_req)
        if metric_req:
            metric = Metric()
            metric.value = metric_req["value"]
            metric.model_ref = metric_req["model_ref"]
            try:
                user_db = User.find_one_by_sid(session,
                                               req.context["auth_user"])
            except NoResultFound:
                raise UserNotExistsError("user id: %s" %
                                         req.context["auth_user"])
            metric.user_id = user_db.user_id
            session.add(metric)
            self.on_post_success(res, None)
        else:
            raise InvalidParameterError(req.context["data"])
