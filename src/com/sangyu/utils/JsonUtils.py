"""
处理Json数据

比如Json的读取、获取每个case的请求数据


user: 2020 by pyp
"""

import json

from com.sangyu.utils.FilePath import getFilePath


class JsonUtils:
    json_path = getFilePath('filename', 'case_json')

    def getAllJsonData(self):
        """
        读取json文件里面的数据
        :param path: 文件路径
        :return:
        """
        with open(self.json_path, 'r') as fp:
            data = json.load(fp)
        return data

    def getCaseJsonData(self, json_name):
        """
        从读取到json文件中获取case对应的json数据，当做请求中的data
        :param json_name:
        :return:
        """
        json_data = self.getAllJsonData().get(json_name)
        return json_data

    def updateCaseJsonFile(self, json_name, key, value):
        """
        将依赖的字段重新更新到json文件
        :param json_name:
        :param key:
        :param value:
        :return:
        """
        all_data = self.getAllJsonData()
        json_file_data = all_data.get(json_name)
        json_file_data[key] = value
        with open(self.json_path, 'w') as fp:
            fp.write(json.dumps(all_data))
