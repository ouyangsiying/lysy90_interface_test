from common.NetworkRequest import NetworkRequest
from tool.Tool import Tool


class Processing:
    def __init__(self):
        self.net = NetworkRequest()
    def login(self,username,password):
        token = self.net.request_token()
        parm ={}
        hash_password = Tool.hash_password(password, token)
        print("加密密码", hash_password)
        parm["user_name"] = username
        parm["_token"] = token
        parm["password"] = hash_password
        print(parm)
        r_login = self.net.post("/auth/login",parm)
        print("登录结果",r_login.text)
p = Processing()
p.login("admin001","111111")
