import falcon

from .metrics import Resource

api = application = falcon.API()

metrics = Resource()
api.add_route('/v1/metrics', metrics)