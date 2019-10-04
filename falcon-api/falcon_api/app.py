import falcon

from .metrics import Resource
from .middleware import PostRequestMiddleware

middleware = [PostRequestMiddleware()]
api = application = falcon.API(middleware=middleware)
metrics = Resource()
api.add_route('/api/v1/metrics', metrics)