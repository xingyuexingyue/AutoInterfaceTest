"""
生成配置内容


user: 2020 by pyp
"""
import configparser

conf = configparser.ConfigParser()  # 生成config对象

# conf.set("sec_b", "b_key3", "new-$r")  # 更新指定section，option的值
#
# conf.set("sec_b", "b_newkey", "new-value")  # 写入指定section增加新option和值

conf.add_section('filename')  # 增加新的section

conf.set('filename', 'excel', '/Users/pengyapan/PycharmProjects/AutoInterfaceTest/src/com/sangyu/docs/case1.xls')

conf.set('filename', 'case_json', '/Users/pengyapan/PycharmProjects/AutoInterfaceTest/src/com/sangyu/docs/user.json')

conf.write(open("/Users/pengyapan/PycharmProjects/AutoInterfaceTest/src/com/sangyu/conf/sangyu.cfg", "w"))  # 写回配置文件
