import json
import falcon

from .errors import InvalidParameterError


class PostRequestMiddleware(object):
    def process_request(self, req, resp):
        if req.content_type == 'application/json':
            try:
                raw_json = req.stream.read()
            except Exception:
                message = 'Read Error'
                raise falcon('Bad request', message)
            try:
                # req.context['data'] = json.loads(raw_json.decode('utf-8'))
                json_body = json.loads(raw_json.decode('utf-8'))

            except ValueError:
                raise InvalidParameterError(
                    'No JSON object could be decoded or Malformed JSON')
            except UnicodeDecodeError:
                raise InvalidParameterError('Cannot be decoded by utf-8')
            try:
                metric_value, model_id = json_body['metric_value'], json_body[
                    'model_id']
            except KeyError:
                req.context['data'] = None
            else:
                req.context['data'] = json_body

        else:
            req.context['data'] = None
