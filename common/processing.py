from common.NetworkRequest import NetworkRequest
from tool.Tool import Tool


class Processing:
    def __init__(self):
        self.net = NetworkRequest()

    def login(self,username,password):
        token = self.net.request_token()
        parms ={}
        hash_password = Tool.hash_password(password, token)
        parms["user_name"] = username
        parms["_token"] = token
        parms["password"] = hash_password
        print(parms)
        r_login = self.net.post("/auth/login",parms)
        print("登录结果:",r_login.text)

    def logout(self):
        self.post("/auth/logout", {})
p = Processing()
p.login("admin001","111111")
