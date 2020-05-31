# -*- coding: utf-8 -*-

"""
请求方法支持：get和post

user: 2020 by pyp
"""

import requests


def getType(url, params=None, **kwargs):
    """
    发送一个get请求
    :param url: 请求的地址
    :param params: 请求的参数，get类型的请求参数在url中，默认为空
    :param kwargs: 接受可变参数列表
    :return: 返回一个Response 对象，可以从这个对象中获取想要的信息
    """
    return requests.get(url, params=params, **kwargs)


def postType(url, data=None, json=None, **kwargs):
    """
    发送一个post请求
    :param url: 请求的地址
    :param data: 请求的参数，post类型的请求参数在请求体中，默认为空
    :param json: 使用data的时候传递的参数是dict，如果想传递一个string可以在data=json.dumps(payload)，也可以直接传递json参数
    :param kwargs: 接受可变参数列表
    :return: 返回一个Response 对象，可以从这个对象中获取想要的信息
    """
    return requests.post(url, data=data, json=json, **kwargs)
