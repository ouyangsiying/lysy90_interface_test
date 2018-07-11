import json
from common.CheckResult import CheckResult
from common.NetworkRequest import NetworkRequest
from common.WriteReport import WriteReport
from tool.Tool import Tool


class Main:
    def __init__(self):
        self.net = NetworkRequest()
        self.check = CheckResult()
        self.write = WriteReport()
        self.token = self.net.request_token()

    def run(self):
        # 读json文件,取测试数据
        api_file = Tool.read_json("interface")
        test_data_file = Tool.read_json("test_data")
        expect_data_file = Tool.read_json("expect_data")

        # 获取接口的具体信息,循环读取某一接口
        api_list = api_file["api_list"]

        for api in api_list:
            url = api["url"]
            method = api["method"]
            need_login = api["need_login"]["type"]
            login_username = api["need_login"]["username"]
            login_password = api["need_login"]["password"]
            test_datas = api["test_data"]
            expect_data_addr = api["expect_data"]
            expect_datas = expect_data_file[expect_data_addr]
            params = test_data_file[test_datas]

            for index in range(len(params)):
                # print("测试和期望",params[index],expect_datas[index])
                param = params[index]
                expect_data = expect_datas[index]
                if '_token' in param.keys():
                    param["_token"] =self.token
                if need_login == 0:
                    print("执行不需要登录的")
                    if method == "get":
                        result = self.net.get(url, param)
                        result_dict = json.loads(result.content)
                        print("实际结果", result_dict)
                        # print("开始比较实际结果和期望值")
                        flag = self.check.comparison_result( expect_data, result_dict)
                        self.write.write_report(url, param, expect_data, result_dict, flag)
                    elif method =="post":
                        result = self.net.post(url, param)
                        result_dict = json.loads(result.content)
                        print("实际结果", result_dict)
                        # print("开始比较实际结果和期望值")
                        flag = self.check.comparison_result(expect_data, result_dict)
                        self.write.write_report(url, param, expect_data, result_dict, flag)

                else:
                    # print("执行登录")
                    parms = {}
                    hash_password = Tool.hash_password(login_password, self.token)
                    parms["user_name"] = login_username
                    parms["_token"] = self.token
                    parms["password"] = hash_password
                    r_login = self.net.post("/auth/login", parms)
                    print("登录结果:", r_login.text)

                    if method == "get":
                        result = self.net.get(url, param)
                        result_dict = json.loads(result.content)
                        print("实际结果", result_dict)
                        # print("开始比较实际结果和期望值")
                        flag = self.check.comparison_result(expect_data, result_dict)
                        self.write.write_report(url, param, expect_data, result_dict, flag)

                    elif method == "post":
                        # print("请求的params", param)
                        # print("执行需要登录的post")
                        result = self.net.post(url, param)
                        result_dict = json.loads(result.content)
                        print("实际结果", result_dict)
                        # print("开始比较实际结果和期望值")
                        flag = self.check.comparison_result(expect_data, result_dict)
                        self.write.write_report(url, param, expect_data, result_dict, flag)
                result = self.net.post("/auth/logout", {})
                print('------')
if __name__ == "__main__":
    main = Main()
    main.run()
