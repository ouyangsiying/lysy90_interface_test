import requests
import json
import config


class NetworkRequest:
    def __init__(self):
        self.req = requests.session()
        self.baseUrl = config.baseUrl
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
        self.cookies = None
        self.response = None
        self.token = None
        self.laravel_session = ''

    # ****************************************************

    def get_headers(self):
        return self.headers

    def del_headers(self, key):
        self.headers.pop(key)

    def set_headers(self, key, val):
        self.headers[key] = val

    # ****************************************************

    def post(self, url, data=None, headers=None, cookies=None):
        if headers is None:
            post_headers = self.headers
        else:
            post_headers = headers
        self.response = self.req.post(self.baseUrl + url, data=data, headers=post_headers)
        return self.response

    def get(self, url, data=None, headers=None, cookies=None):
        if headers is None:
            post_headers = self.headers
        else:
            post_headers = headers
        self.response = self.req.get(self.baseUrl + url, data=data, headers=post_headers)
        return self.response
    # ****************************************************

    def request_token(self):
        self.response = self.get('/api/token')
        self.token = json.loads(self.response.content)["result"]["_token"]
        return self.token
