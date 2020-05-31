"""
返回excel的存储地址

user: 2020 by pyp
"""

import configparser


def getFilePath(section, option):
    """
    返回excel的地址
    :param section: 对应配置文件中的section
    :param option: 对应配置文件中的option
    :return: 返回option对应的value
    """
    conf = configparser.ConfigParser()
    conf.read("../conf/sangyu.cfg")
    return conf.get(section, option)



