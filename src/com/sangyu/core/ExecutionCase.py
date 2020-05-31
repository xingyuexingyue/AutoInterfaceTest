"""
执行case

user: 2020 by pyp
"""
import json

from com.sangyu.core.CaseRequests import CaseRequests
from com.sangyu.utils.ExcelPublicInformation import ExcelPublicInfomation


class ExecutionCase:
    case_requests = CaseRequests()

    def runWithCase(self):
        """
        实现思路：
        1. 获得Excel对象
        2. 遍历每个sheet以及sheet下的每行数据（相当于是每个sql）
        3. 依次执行每条用例并记录结果
        :return:
        """
        excel_public_information = ExcelPublicInfomation()
        excel_data = excel_public_information.getExcel('filename', 'excel')  # 获得了excel的对象
        sheet_names = excel_public_information.getExcelSheetNames(excel_data)  # 获得Excel的所有sheet
        sheet_len = excel_public_information.getExcelSheetslen(sheet_names)  # 获得Excel的总数，依此遍历

        for i in range(0, sheet_len):
            cond = excel_public_information.getIsLooadedByIndex(excel_data, i)
            if cond:
                sheet_rol_len = excel_public_information.getSheetRowsNum(excel_data, i)
                for j in range(1, sheet_rol_len):
                    case = excel_public_information.excelCase(excel_data, i, j)
                    is_run = case.get('test_run')
                    if is_run == 'yes':
                        res = self.case_requests.preRunCase(case)
                        expected_result = case.get('test_expected_result')

                        if res.status_code is not 200:
                            self.case_requests.writeCaseResult('请求返回的状态码非200', j, i)
                        elif expected_result == '':
                            self.case_requests.writeCaseResult('pass', j, i)
                        else:
                            result = self.case_requests.processResponse(expected_result, json.dumps(res.json()))
                            self.case_requests.writeCaseResult(result, j, i)
                    else:
                        self.case_requests.writeCaseResult('Not performed', j, i)

