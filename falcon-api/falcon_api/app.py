import falcon

from .users import Resource

api = application = falcon.API()

users = Resource()
api.add_route('/v1/users', users)