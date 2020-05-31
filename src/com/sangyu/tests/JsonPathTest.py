import json

import jsonpath
import requests

payload = (('key1', 'value1'), ('key1', 'value2'))
r = requests.post('http://httpbin.org/post', data=payload)
r1 = r.json()  # 返回的是对象
print(type(r1))
print(r1)
r2 = json.dumps(r1)
print(type(r2))
r3 = json.loads(r2)  # 把json格式字符串转化为python对象，此处返回的是一个Unicode字符
print(type(r3))
city_list = jsonpath.jsonpath(r1, "$..Accept-Encoding")
print(city_list)