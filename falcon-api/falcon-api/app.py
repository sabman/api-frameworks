import falcon

from .name import Resource

api = application = falcon.API()

name = Resource()
api.add_route('/', name)