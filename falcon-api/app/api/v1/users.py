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
from app.model import User
from app.errors import (
    AppError,
    InvalidParameterError,
    UserNotExistsError,
    PasswordNotMatch,
)

LOG = log.get_logger()

FIELDS = {
    "email": {
        "type": "string",
        "regex": "[a-zA-Z0-9._-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,4}",
        "required": True,
        "maxlength": 320,
    },
    "password": {
        "type": "string",
        "regex": "[0-9a-zA-Z]\w{3,14}",
        "required": True,
        "minlength": 8,
        "maxlength": 64,
    },
}


def validate_user_create(req, res, resource, params):
    schema = {
        "email": FIELDS["email"],
        "password": FIELDS["password"],
    }

    v = Validator(schema)
    if not v.validate(req.context["data"]):
        raise InvalidParameterError(v.errors)


class Collection(BaseResource):
    """
    Handle for endpoint: /api/v1/users
    """
    @falcon.before(validate_user_create)
    def on_post(self, req, res):
        session = req.context["session"]
        user_req = req.context["data"]
        if user_req:
            user = User()
            user.email = user_req["email"]
            user.password = hash_password(user_req["password"]).decode("utf-8")
            sid = uuid()
            user.sid = sid
            user.token = encrypt_token(sid).decode("utf-8")
            session.add(user)
            self.on_post_success(res, None)
        else:
            raise InvalidParameterError(req.context["data"])

    @falcon.before(auth_required)
    def on_put(self, req, res):
        pass


class Self(BaseResource):
    """
    Handle for endpoint: /api/v1/users/self/sign_in
    """

    LOGIN = "sign_in"
    RESETPW = "resetpw"

    def on_get(self, req, res):
        cmd = re.split("\\W+", req.path)[-1:][0]
        if cmd == Self.LOGIN:
            self.process_login(req, res)
        elif cmd == Self.RESETPW:
            self.process_resetpw(req, res)

    def process_login(self, req, res):
        data = req.context["data"]
        email = data["email"]
        password = data["password"]
        session = req.context["session"]
        try:
            user_db = User.find_by_email(session, email)
            if verify_password(password, user_db.password.encode("utf-8")):
                self.on_sign_in_success(res, user_db.to_dict())
            else:
                raise PasswordNotMatch()
        except NoResultFound:
            raise UserNotExistsError("User email: %s" % email)

    @falcon.before(auth_required)
    def process_resetpw(self, req, res):
        pass
