"""
Excel规则

比如每一列的含义
user: 2020 by pyp
"""


class ExcelRule:
    """
    记录每一列的信息
    :return:
    """
    test_id = 0  # id
    test_features = 1  # 模块
    test_url = 2  # url
    test_run = 3  # 是否运行
    test_type = 4  # 请求类型
    test_is_header = 5  # 是否携带header
    test_case = 6  # case依赖，记录的是当前列表的id
    test_return_field = 7  # 依赖返回的数据格式
    test_rely_field = 8  # 依赖字段
    test_data = 9  # 请求数据
    test_expected_result = 10  # 预期结果
    test_result = 11  # 实际结果

    def getTestId(self):
        """
        返回id所在列数
        :return: int
        """
        return self.test_id

    def getTestFeatures(self):
        """
        返回模块名称所在列数
        :return: int
        """
        return self.test_features

    def getTestUrl(self):
        """
        返回url所在列数
        :return: int
        """
        return self.test_url

    def getTestRun(self):
        """
        返回是否运行所在列数
        :return: int
        """
        return self.test_run

    def getTestType(self):
        """
        返回请求类型所在列数
        :return: int
        """
        return self.test_type

    def getTestIsHeader(self):
        """
        返回是否携带header所在列数
        :return: int
        """
        return self.test_is_header

    def getTestCase(self):
        """
        返回case依赖所在列数
        :return: int
        """
        return self.test_case

    def getTestReturnField(self):
        """
        返回依赖返回的数据格式所在列数
        :return: int
        """
        return self.test_return_field

    def getTestRelyField(self):
        """
        返回数据依赖字段所在列数
        :return: int
        """
        return self.test_rely_field

    def getTestData(self):
        """
        返回请求数据所在列数
        :return: int
        """
        return self.test_data

    def getTestExpectedResult(self):
        """
        返回预期结果的所在列数
        :return:
        """
        return self.test_expected_result

    def getTestResult(self):
        """
        返回实际结果的所在列数
        :return: int
        """
        return self.test_result


