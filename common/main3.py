import json

from common.Tool import Tool
from common.NetworkRequest import NetworkRequest
from common.CheckResult import CheckResult
from common.WriteReport import WriteReport


class Main:
    def __init__(self):
        self.net = NetworkRequest()
        self.check = CheckResult()
        self.write = WriteReport()
        # self.msg = ''
        # self.code = 0

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
            need_login = api["need_login"]
            test_data = api["test_data"]
            expect_data_addr = api["expect_data"]
            expect_data = expect_data_file[expect_data_addr]
            print("期望结果", expect_data)
            params = test_data_file[test_data]

            if method == "get":
                result = self.net.get(url, params)
                result_dict = json.loads(result.content)
                print("实际结果", result_dict)
                print("开始比较实际结果和期望值")
                flag = self.check.comparison_result( expect_data, result_dict)
                self.write.write_report(url, params, expect_data, result_dict, flag)

            # elif method == "post":
            #     result = self.net.post(url, params)
            #     print(result.content)
            #
            # if method == "delete":
            #     result = self.net.get(url, params)
            #     result_dict = json.loads(result.content)
            #     print("实际结果", result_dict)
            #     flag = self.check.comparison_result(expect_data, result_dict)
            #     self.write.write_report(url, params, expect_data, result_dict, flag)
            #
            # elif method == "put":
            #     result = self.net.post(url, params)
            #     print(result.content)

if __name__ == "__main__":
    main = Main()
    main.run()
