from flask import Response, jsonify

class Success(Response):
    def __init__(self, data=None, msg=None, status=200, headers=None, mimetype='application/json', content_type=None, **kwargs):
        super().__init__(response=None, status=status, headers=headers, mimetype=mimetype, content_type=content_type)
        self.res = {
            "code": 1,
            "data": data,
            "msg": msg
        }

    def toJson(self):
        return jsonify(self.res)


class Error(Response):
    def __init__(self, data=None, msg=None, status=200, headers=None, mimetype='application/json', content_type=None, **kwargs):
        super().__init__(response=None, status=status, headers=headers, mimetype=mimetype, content_type=content_type)
        self.res = {
            "code": 0,
            "data": data,
            "msg": msg
        }

    def toJson(self):
        return jsonify(self.res)