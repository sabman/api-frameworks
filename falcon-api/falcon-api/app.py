import falcon

from .user import Resource

api = application = falcon.API()

user = Resource()
api.add_route('/', user)