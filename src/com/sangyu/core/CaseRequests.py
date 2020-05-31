"""
执行用例，批量执行，并实现依赖关系


user: 2020 by pyp
"""
import jsonpath

from com.sangyu.core.DealWithTestCase import DealWithTestCase
from com.sangyu.utils.CaseData import GetCaseDada
from com.sangyu.utils.ExcelPublicInformation import ExcelPublicInfomation
from com.sangyu.utils.ExcelRule import ExcelRule
from com.sangyu.utils.JsonUtils import JsonUtils
from com.sangyu.utils.RequestUtils import getType, postType


class CaseRequests:
    json_utils = JsonUtils()
    excel = ExcelPublicInfomation()
    get_excel_col_num = ExcelRule()
    deal_with_test_case = DealWithTestCase()

    def getCaseDataAndRun(self, value):
        """
        执行用例
        :param value: 每一条用例的dict
        :return:
        """
        get_case_data = GetCaseDada(value)
        url = get_case_data.getUrl()
        header = get_case_data.getHeader()
        type = get_case_data.getType()
        data = get_case_data.getData()
        return self.runCase(type, url, data, header)

    def runCase(self, type, url, data, header):
        """
        执行用例并写入结果
        根据预期结果和实际结果对比最终写入到excel
        :param type: 请求类型
        :param url: 请求地址
        :param data: 请求数据
        :param header: 请求头
        :param expected_result: 请求预期结果
        :return: String
        """
        if type == 'get':
            res = getType(url, data, headers=header)
        if type == 'post':
            res = postType(url, data, headers=header)
        return res

    def processResponse(self, test_expected_result, res):
        """
        判断最终结果：pass or false
        :param col:
        :param test_expected_result: 预期结果
        :param res: 执行请求返回的结果
        :return:
        """
        result = ''
        if test_expected_result in res:
            result = 'pass'
        else:
            result = 'false'

        return result

    def writeCaseResult(self, data, row, sheet):
        """
        写入到excel
        :param row:
        :param sheet:
        :param self:
        :param data: 最终的结果 pass or false
        :return:
        """
        self.excel.writeData(row, self.get_excel_col_num.getTestResult(), data, sheet)

    def getRelyCase(self, rely_case_id, test_return_field):
        """
        执行依赖用例
        :param rely_case_id:
        :param test_return_field:
        :return:
        """
        rely_case = self.case_dict.get(rely_case_id)
        return jsonpath.jsonpath(self.getCaseDataAndRun(rely_case), test_return_field)

    def preRunCase(self, value):
        """
        执行用例前判断是否存在依赖
        :param value: 当前要执行case的value，字典
        :return:
        """
        if value.get('test_case') is None:  # 用例没有依赖的情况，直接执行
            return self.getCaseDataAndRun(value)

        else:
            """
            这里的逻辑需要梳理下，
            代码的实现使用了递归，因为考虑的一种的情况是当前依赖的case很有可能也依赖其他的case
            所以，在else的逻辑中（if是出口）
            第一步，拿到最终被依赖接口的case内容  case_result，比如，我们有一个接口A依赖B，B依赖C，C依赖D，程序最终会执行到D满足的if条件而return ，D的执行结果
            第二步，拿到依赖字段的值 next_rely_filed 就是拿D拿C依赖字段的值
            第三步，拿到使用字段的key next_use_name 就是C中实际要请求时的字段
            第四步，更新Json中字段的值 
            第五步：返回下一次要执行的case
            """
            case_result = self.preRunCase(self.deal_with_test_case.getTeseCaseDict().get(value.get('test_case')))
            next_rely_filed = jsonpath.jsonpath(case_result.json(), value.get('test_return_field'))  # 拿到c依赖d的字段的值
            next_key = value.get('test_rely_field')
            next_use_name = value.get('test_data')
            self.json_utils.updateCaseJsonFile(next_use_name, next_key, next_rely_filed[0])
            return self.getCaseDataAndRun(value)
