import requests
import json
import config


class NetworkRequest:
    def __init__(self):
        # self.req = requests.session()
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

    # def post(self, url, data=None, headers=None, cookies=None):
    #     if not headers:
    #         post_headers = headers
    #     else:
    #         post_headers = self.headers
    #     self.response = self.req.post(self.baseUrl + url, data=data, headers=post_headers)
    #     return self.response
    #
    # def get(self, url, data=None, headers=None, cookies=None):
    #     if not headers:
    #         post_headers = headers
    #     else:
    #         post_headers = self.headers
    #     self.response = self.req.get(self.baseUrl + url, data=data, headers=post_headers)
    #     return self.response
    def post(self, url, params={}):
        if params == {}:
            try:
                request = requests.post(self.baseUrl + url, None, headers=self.headers, cookies=self.cookies)
                return request
            except Exception as e1:
                print(e1.message)
        else:
            try:
                request = requests.post(self.baseUrl + url, params, headers=self.headers, cookies=self.cookies)
                return request
            except Exception as e1:
                print(e1)

    def get(self, url, params={}):
        if params == {}:
            try:
                request = requests.get(self.baseUrl + url)
                return request
            except Exception as e2:
                print(e2.message)
        else:
            keys = params.keys()
            paramslen = keys.__len__()
            if paramslen != 0:
                url = url + "?"
            index = 1
            for key in keys:
                if index == paramslen:
                    url = url + key + "=" + params[key]
                else:
                    url = url + key + "=" + params[key] + "&"
                index = index + 1
        url = url.replace(' ', '')
        try:
            request = requests.get(self.baseUrl + url, params)
            return request
        except Exception as e2:
            print(e2)
    # ****************************************************

    def request_token(self):
        self.response = self.get('/api/token')
        self.token = json.loads(self.response.content)["result"]["_token"]
        return self.token
