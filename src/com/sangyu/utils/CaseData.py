"""
根据传递的用例返回每一列的值

用例传递的格式是字典


user: 2020 by pyp
"""
from com.sangyu.utils.JsonUtils import JsonUtils


class GetCaseDada:
    case_value = {}
    json_utils = JsonUtils()

    def __init__(self, case_value):
        self.case_value = case_value

    def getRun(self):
        """
        返回是否run
        :return:
        """
        return self.case_value.get('test_run')

    def getUrl(self):
        """
        返回url
        :return:
        """
        return self.case_value.get('test_url')

    def getHeader(self):
        """
        返回header
        :return:
        """
        return self.case_value.get('test_header')

    def getType(self):
        """
        返回请求类型
        :return:
        """
        return self.case_value.get('test_type')

    def getIsHeader(self):
        """
        返回是否有header
        :return:
        """
        return self.case_value.get('test_is_header')

    def getCase(self):
        """
        返回依赖的case
        :return:
        """
        return self.case_value.get('test_case')

    def getReturnFiled(self):
        """
        返回依赖case的返回的字段
        :return:
        """
        return self.case_value.get('test_return_field')

    def getRelyField(self):
        """
        返回当前case的依赖字段
        :return:
        """
        return self.case_value.get('test_rely_field')

    def getData(self):
        """
        返回请求数据
        :return:
        """
        test_data = self.case_value.get('test_data')
        if test_data is None:
            test_data = None
        else:
            test_data = self.json_utils.getCaseJsonData(test_data)
        return test_data

    def getExpectedResult(self):
        """
        返回预期结果
        :return:
        """
        return self.case_value.get('test_expected_result')

    def getResult(self):
        """
        返回实际结果
        :return:
        """
        return self.case_value.get('test_result')
