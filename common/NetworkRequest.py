import requests
import json
import hashlib
import urllib
import http.cookiejar


class NetworkRequest:
    def __init__(self,baseUrl='http://vip.lysy90store.xyz'):
        self.baseUrl = baseUrl
        self.laravel_session = ''
        self.cookies = {}
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

    def post(self,url,params={}):
        if params =={ }:
            try:
                request = requests.post(self.baseUrl+url,None,headers=self.headers,cookies=self.cookies)
                return request
            except Exception as e1:
                print(e1.message)
        else:
            try:
                request = requests.post(self.baseUrl + url, params, headers=self.headers,cookies=self.cookies)
                return request
            except Exception as e1:
                print(e1)

    def get(self,url,params={}):
        if params =={}:
            try:
                request = requests.get(self.baseUrl+url)
                return request
            except Exception as e2:
                print(e2.message)
        else:
            keys =params.keys()
            paramslen = keys.__len__()
            if paramslen !=0:
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
            request = requests.get(self.baseUrl+url,params)
            return request
        except Exception as e2:
            print(e2)

    def delete(self,url,params={}):
        try:
            request = requests.delete(self.baseUrl+url,params)
            return request
        except Exception as e3:
            print(e3)

    def put(self,url,params={}):
        try:
            request = requests.put(self.baseUrl + url, params)
            return request
        except Exception as e4:
            print(e4)

    def gettoken(self):
        request = requests.get(self.baseUrl + '/api/token')
        token = json.loads(request.content)["result"]["_token"]
        self.laravel_session = request.cookies['laravel_session']
        self.cookies = {'laravel_session': self.laravel_session}
        return token

    def login(self,username,password):
        token = self.gettoken()
        params = {}
        params["user_name"] = username
        params["_token"] = token
        encrypted_password = hashlib.sha1((password).encode('utf_8')).hexdigest()
        encrypted_password = hashlib.sha1((encrypted_password + token).encode('utf_8')).hexdigest()
        params["password"] = encrypted_password
        request=self.post("/auth/login",params)
        print(request.content)

    def logout(self):
        self.post("/auth/logout", {})

