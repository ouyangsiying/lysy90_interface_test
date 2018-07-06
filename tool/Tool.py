import json
import xlrd
import hashlib


class Tool:
    # 读json文件
    @staticmethod
    def read_json(filename):
        try:
            with open("../resource/" + filename + ".json", 'r', encoding='utf-8') as load_file:
                load_json_dict = json.load(load_file)
                return load_json_dict
        except Exception as e:
            print("读文件异常", e)
            exit()

    # 读excel
    @staticmethod
    def read_excel(filename):
        try:
            excel_file = xlrd.open_workbook("../test_report/" + filename + ".xls", formatting_info=True)
            return excel_file
        except Exception as e:
            print("读文件异常", e)
            exit()

    # 将json字符串格式化
    @staticmethod
    def json_converted_str(str1):
        str2 = str(str1)
        str2 = str2.replace("{", "{\n")
        str2 = str2.replace(",", ",\n")
        str2 = str2.replace("}", "}\n")
        return str2

    # 加密密码
    @staticmethod
    def hash_password(password):
        hash_password = hashlib.sha1((password).encode('utf_8')).hexdigest()
        return hash_password