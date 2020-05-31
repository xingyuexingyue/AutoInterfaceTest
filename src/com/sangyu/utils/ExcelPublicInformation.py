"""
返回excel中公共信息

比如行数、列数、读取、写入

user: 2020 by pyp
"""
from xlutils.copy import copy

import xlrd

from com.sangyu.utils.ExcelRule import ExcelRule
from com.sangyu.utils.FilePath import getFilePath


class ExcelPublicInfomation:
    def getExcel(self, section, option):
        """
        打开并去读excel
        :return: 一个对象，通过这个对象可以获取到excel里的信息
        """
        filename = getFilePath(section, option)
        return xlrd.open_workbook(filename)

    def getExcelSheetNames(self, excel_data):
        """
        返回所有sheet的名称
        :return:
        """
        return excel_data.sheet_names()

    def getExcelSheetslen(self, sheets):
        """
        返回所有sheet的个数
        :return: int
        """
        return len(sheets)

    def getSheetName(self, excel_data, inx):
        """
        根据索引返回sheet的名称
        :param excel_data:
        :param inx: sheet的索引
        :return: String
        """
        return excel_data.sheet_names()[inx]

    def getIsLooadedByName(self, excel_data, excel_name):
        """
        检查某个sheet是否导入完毕
        :param excel_data:
        :param excel_name: sheet的名称
        :return: boolean
        """
        return excel_data.sheet_loaded(excel_name)

    def getIsLooadedByIndex(self, excel_data, inx):
        """
        检查某个sheet是否导入完毕
        :param excel_data:
        :param inx: sheet的名称
        :return: boolean
        """
        return excel_data.sheet_loaded(inx)

    def getExcelData(self, excel_data, inx):
        """
        根据索引获取sheet整行和整列的值
        :param excel_data:
        :param inx:
        :return:
        """
        return excel_data.sheet_by_index(inx)

    def getSpecifyExcelData(self, excel_data, inx, row, col):
        """
        获取指定单元格的内容
        :param excel_data:
        :param inx: sheet的索引
        :param row: 行数
        :param col: 列数
        :return:  不同结果返回的类型不同
        """
        return self.getExcelData(excel_data, inx).cell(row, col).value

    def excelCase(self, excel_data, inx, row):
        """
        返回某个sheet中一条用例的信息
        :param excel_data: excel内容
        :param inx: sheet的index
        :param row: 行数
        :return: dict
        """
        case_dict = {}

        excel_rule = ExcelRule()

        t_id = self.getSpecifyExcelData(excel_data, inx, row, excel_rule.getTestId())
        t_features = self.getSpecifyExcelData(excel_data, inx, row, excel_rule.getTestFeatures())
        t_url = self.getSpecifyExcelData(excel_data, inx, row, excel_rule.getTestUrl())
        t_run = self.getSpecifyExcelData(excel_data, inx, row, excel_rule.getTestRun())
        t_type = self.getSpecifyExcelData(excel_data, inx, row, excel_rule.getTestType())
        t_is_header = self.getSpecifyExcelData(excel_data, inx, row, excel_rule.getTestIsHeader())
        t_case = self.getSpecifyExcelData(excel_data, inx, row, excel_rule.getTestCase()) if self.getSpecifyExcelData(
            excel_data, inx, row, excel_rule.getTestCase()) != '' else None
        t_return_field = self.getSpecifyExcelData(excel_data, inx, row,
                                                  excel_rule.getTestReturnField()) if self.getSpecifyExcelData(
            excel_data, inx, row, excel_rule.getTestReturnField()) is not '' else None
        t_rely_field = self.getSpecifyExcelData(excel_data, inx, row,
                                                excel_rule.getTestRelyField()) if self.getSpecifyExcelData(excel_data,
                                                                                                           inx, row,
                                                                                                           excel_rule.getTestRelyField()) is not '' else None
        t_data = self.getSpecifyExcelData(excel_data, inx, row, excel_rule.getTestData())
        t_expected_result = self.getSpecifyExcelData(excel_data, inx, row, excel_rule.getTestExpectedResult())
        t_result = self.getSpecifyExcelData(excel_data, inx, row, excel_rule.getTestResult())

        case_dict['test_id'] = t_id
        case_dict['test_features'] = t_features
        case_dict['test_url'] = t_url
        case_dict['test_run'] = t_run
        case_dict['test_type'] = t_type
        case_dict['test_is_header'] = t_is_header
        case_dict['test_case'] = t_case
        case_dict['test_return_field'] = t_return_field
        case_dict['test_rely_field'] = t_rely_field
        case_dict['test_data'] = t_data
        case_dict['test_expected_result'] = t_expected_result
        case_dict['test_result'] = t_result

        return case_dict

    def getSheetRowsNum(self, excel_data, inx):
        """
        获取某个sheet的总行数
        :param excel_data:
        :param inx:
        :return:
        """
        sheet2 = excel_data.sheet_by_index(inx)
        return sheet2.nrows

    def writeData(self, row, col, data, sheet):
        """
        写入excel数据
        :param excel_data:
        :param row:
        :param col:
        :param data:
        :return:
        """
        excel_data = self.getExcel('filename', 'excel')  # 获得了excel的对象
        write_data = copy(excel_data)
        sheet_data = write_data.get_sheet(sheet)
        sheet_data. write(row, col, data)
        filename = getFilePath('filename', 'excel')
        write_data.save(filename)

    def getAllCaseNums(self):
        """
        获得所有用例数量
        :return:
        """
        excel_public_information = ExcelPublicInfomation()
        excel_data = excel_public_information.getExcel('filename', 'excel')  # 获得了excel的对象
        sheet_names = excel_public_information.getExcelSheetNames(excel_data)  # 获得Excel的所有sheet
        sheet_len = excel_public_information.getExcelSheetslen(sheet_names)  # 获得Excel的总数，依此遍历
        all_case = 0
        all_run = 0
        for i in range(0, sheet_len):
            cond = excel_public_information.getIsLooadedByIndex(excel_data, i)
            if cond:
                sheet_rol_len = excel_public_information.getSheetRowsNum(excel_data, i)
                for j in range(1, sheet_rol_len):
                    all_case += 1
        return all_case

    def getAllRunCaseNums(self):
        """
        获得所有执行用例的数量
        :return:
        """
        excel_public_information = ExcelPublicInfomation()
        excel_data = excel_public_information.getExcel('filename', 'excel')  # 获得了excel的对象
        sheet_names = excel_public_information.getExcelSheetNames(excel_data)  # 获得Excel的所有sheet
        sheet_len = excel_public_information.getExcelSheetslen(sheet_names)  # 获得Excel的总数，依此遍历
        all_run = 0
        for i in range(0, sheet_len):
            cond = excel_public_information.getIsLooadedByIndex(excel_data, i)
            if cond:
                sheet_rol_len = excel_public_information.getSheetRowsNum(excel_data, i)
                for j in range(1, sheet_rol_len):
                    case = excel_public_information.excelCase(excel_data, i, j)
                    is_run = case.get('test_run')
                    if is_run == 'yes':
                        all_run += 1
        return all_run


if __name__ == '__main__':
    e = ExcelPublicInfomation()
    a = e.getAllCaseNums()
    print(a)
    b = e.getAllRunCaseNums()
    print(b)