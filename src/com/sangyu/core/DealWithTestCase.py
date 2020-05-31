"""
excel中读取到数据存储到map

user: 2020 by pyp
"""
from com.sangyu.core.CaseData import CaseData
from com.sangyu.utils.ExcelPublicInformation import ExcelPublicInfomation


class DealWithTestCase:
    case_dict = {}

    def getTeseCaseDict(self):
        """
        从excel中获得case数据

        这么做的目的是：在依赖case中可以从map中获得到依赖case执行所需要的信息
        :return: dict
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

                    test_id = case.get('test_id')
                    self.case_dict[test_id] = case
        return self.case_dict

    def afterTest(self):
        """
        将执行后有问题的数据，每条映射到一个对象中，并将对象存储到一个list中（这样做的目的是记录顺序），显示的时候可以按照从小到大的顺序去执行
        :return: list
        """
        excel_public_information = ExcelPublicInfomation()
        excel_data = excel_public_information.getExcel('filename', 'excel')  # 获得了excel的对象
        sheet_names = excel_public_information.getExcelSheetNames(excel_data)  # 获得Excel的所有sheet
        sheet_len = excel_public_information.getExcelSheetslen(sheet_names)  # 获得Excel的总数，依此遍历
        after_test_case_list = []
        for i in range(0, sheet_len):
            cond = excel_public_information.getIsLooadedByIndex(excel_data, i)
            if cond:
                sheet_rol_len = excel_public_information.getSheetRowsNum(excel_data, i)
                for j in range(1, sheet_rol_len):
                    case = excel_public_information.excelCase(excel_data, i, j)

                    test_id = case.get('test_id')
                    test_result = case.get('test_result')
                    if test_result != 'pass':
                        test_features = case.get('test_features')
                        test_url = case.get('test_url')
                        case_data = CaseData(test_id,test_features, test_url,test_result)
                        after_test_case_list.append(case_data)
        return after_test_case_list

