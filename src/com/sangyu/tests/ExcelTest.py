import xlrd

from com.sangyu.utils.FilePath import getFilePath

'''
打开Excel文件读取数据
'''
filename = getFilePath('filename', 'excel')
data = xlrd.open_workbook(filename)
# print(data)

'''
获取book中一个工作表，返回一个Sheet对象
'''
table = data.sheets()
# print(table)

# 通过索引顺序获取
table1 = data.sheets()[0]
# print(table)

# 返回所有sheet的名称
names = data.sheet_names()
# print(names)

# 根据索引获得对应sheet的名称
name = data.sheet_names()[0]
# print(name)

# 检查某个sheet是否导入完毕
# print(data.sheet_loaded('sheet1'))

# 根据sheet索引或者名称获取sheet内容，同时获取sheet名称、行数、列数
sheet2 = data.sheet_by_index(0)
# print(sheet2)
# print(sheet2.name)
# print(sheet2.nrows)
# print(sheet2.ncols)

# 根据sheet名称获取整行和整列的值
sheet3 = data.sheet_by_name('sheet1')
rows = sheet2.row_values(0)
cols = sheet2.col_values(0)
print(rows)
print(cols)

# 获取指定单元格的内容
# print(sheet3.cell(1, 1).value.encode('utf-8'))

# 获取单元格内容的数据类型 ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
# print(sheet2.cell(1, 0).ctype)  # 1 为string类型
# print(sheet2.cell(1, 1).ctype)  # 2 为number类型
# print(sheet2.cell(1, 2).ctype)  # 3 为date类型

# 获取单元内容为日期类型的方式
# 使用xlrd的xldate_as_tuple处理为date格式，先判断表格的ctype=3时xlrd才能执行操作

# print(sheet3.cell(1, 12).ctype)
# xlrd.xldate_as_tuple(sheet2.cell_value(1, 2), data.datemode)
# (2015, 5, 5, 0, 0, 0)
# date_value = xlrd.xldate_as_tuple(sheet2.cell_value(1,2),workbook.datemode)
# date(*date_value[:3])
# datetime.date(2015, 5, 5)
# date(*date_value[:3]).strftime('%Y/%m/%d')
# '2015/05/05'
