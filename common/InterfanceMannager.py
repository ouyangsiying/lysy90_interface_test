#读接口的文件夹
from tool.Tool import Tool

class InterfaceMannager:
    def __init__(self):
        self.url = None
        self.method = None
        self.need_login = None
        self.test_datas = None
        self.expect_datas = None
        self.login_username = None
        self.login_password = None


    # def get_url(self,url):
    #     return url
    #
    # def method(self, method):
    #     return method
    #
    # def need_login(self, need_login):
    #     return need_login
    #
    # def test_data(self, test_data):
    #     return test_data
    #
    # def expect_data(self, expect_data):
    #     return expect_data

    def get_api_lists(self,interface_file):
        api_file = Tool.read_json(interface_file)
        api_list = api_file["api_list"]
        print("测试接口",api_list)
        return api_list

    def get_one_api(self,api_lists):
        for api in api_lists:
            self.url = api["url"]
            self.method = api["method"]
            self.need_login = api["login"]["type"]
            self.login_username = api["login"]["username"]
            self.login_password = api["login"]["password"]
            self.test_datas = api["test_data"]
            expect_data_addr = api["expect_data"]
            self.expect_datas = expect_data_file[expect_data_addr]
            for expect_data in self.expect_datas:
                print("期望结果", expect_data)
            params = test_data_file[test_datas]




api = InterfaceMannager()
api.get_api_lists("interface")