
class Check:
    def __init__(self):
        self.Flag = ""
        self.status = ""

#比较字典的key
    def compre_keys(self,expect_keys,actual_keys):
        if len(expect_keys) != len(actual_keys):
            # print("----建不同")
            return -1, "键不相同" + str(len(expect_keys)) + str(len(actual_keys))
        else:
            for key in expect_keys:
                if key in actual_keys:
                    pass
                else:
                    return -1, "不存在的键" + key
                return 1,"键相同"

    def comparison_result(self,expect,actual):
        expect_keys = list(expect.keys())
        actual_keys = list(actual.keys())
        code, msg = self.compre_keys(expect_keys, actual_keys)

        if code == -1:
            self.status = -1
            return self.status
        else:
            for key in expect_keys:
                if expect[key] != actual[key]:
                    self.status = -1
                    return self.status
                else:
                    if isinstance(expect[key], dict):
                        return self.comparison_result(expect[key], actual[key])
                    # 判断是否为数组
                    elif isinstance(expect[key], list):
                        self.status = self.comparison_array(expect[key], actual[key])
                        return self.status
                    else:
                        if type(expect[key]) == type(actual[key]):
                            # 类型一样
                            if self.status == -1:
                                pass
                            else:
                                self.status = 1
                        else:
                            # 类型不一样
                            self.status = -1
            return self.status

    def comparison_array(self, array1, array2):
        if type(array1) != type(array2):
            status = -1
            # print("数组不相等")
            return status
        else:
            if len(array1) != len(array2):
                status = -1
                # print("数组不相等")
                return status
            else:
                for i in range(len(array1)):
                    if isinstance(array1[i], dict):
                        return self.comparison_result(array1[i], array2[i])
                    elif isinstance(array1[i], list):
                        return self.comparison_array(array1[i], array2[i])
                    else:
                        if array1[i] != array2[i]:
                            status = -1
                            # print("数组不相等")
                            return status
                        else:
                            # print("数组相等")
                            status = 1
                # print(status)
                return status
