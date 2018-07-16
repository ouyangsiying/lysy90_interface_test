# 期望和实际结果的键相比较
# 键相同，再去比较期望键中对应值的实际结果键对应的值的类型
# 首先判断是不是字典，是字典自己调用自己
# 再判断是不是是数组，是数组先判断数组的类型是否一样，一样再判断数组的长度，数组的长度一样：判断是不是字典；是不是数组；不是数组再比较值的类型
# 不是数组和字典，就比较值的类型
class CheckResult:
    def __init__(self):
        self.Flag = ""
        self.status = ""
        self.report = ''

    def comparison_result(self, expect, actual):
        expect_keys = list(expect.keys())
        actual_keys = list(actual.keys())
        code, msg = self.compre_keys(expect_keys, actual_keys)
        # print("键的比较结果:", code, msg)

        # 返回status为1，表示期望和实际结果相同
        # 返回status为-1，表示期望和实际结果不相同
        if code == -1:
            self.status = -1
            # self.report['key'] = msg
            # print("比较",self.status)
            return self.status
        else:
            for key, value in expect.items():
                # print("期望键名，期望的值，实际结果对应的值",key,value,actual[key])
                # 判断是否为字典
                if isinstance(value, dict):
                    return self.comparison_result(value, actual[key])
                # 判断是否为数组
                elif isinstance(value, list):
                    self.status= self.comparison_array(value, actual[key])
                    return self.status
                else:
                    if type(value) == type(actual[key]):
                        # 类型一样
                        if self.status == -1:
                            pass
                        else:
                            self.status = 1
                    else:
                        # 类型不一样
                        self.status = -1
            return self.status

    def compre_keys(self, expect_keys, actual_keys):
        # 比较键返回-1，表示键不相同
        # 比较键返回1，表示键相同
        # 键不相同
        if len(expect_keys) != len(actual_keys):
            # print("----建不同")
            return -1, "键不相同" + str(len(expect_keys)) + str(len(actual_keys))
            # 键相同
        else:
            for key in expect_keys:
                if key in actual_keys:
                    pass
                else:
                    return -1, "不存在的键" + key
                    # print("----建不同")
                # print("----建同")
                return 1, "键相同"

    # 比较数组
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

