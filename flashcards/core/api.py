import json

import flask as fl


class JSONResponse(fl.Response):

    def __init__(self, response=None, status=None, headers=None, mimetype='application/json', content_type=None,
                 direct_passthrough=False):
        super().__init__(json.dumps(response), status, headers, mimetype, content_type, direct_passthrough)


class APIResponse(JSONResponse):
    def __init__(self, data=None, status=200, message=''):
        response = {
            'meta': {
                'status': status,
                'message': message
            }
        }
        if data:
            response['data'] = data
        super().__init__(response=response, status=status)
