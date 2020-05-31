import requests

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get("http://httpbin.org/cookies")
# print(r.text)


# s = requests.Session()
# s.auth = ('user', 'pass')
# s.headers.update({'x-test': 'true'})
#
# r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
# print(r.text)


# 方法级别的参数也不会被跨请求保持。下面的例子只会和第一个请求发送 cookie ，而非第二个
s = requests.Session()
r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)

r = s.get('http://httpbin.org/cookies')
print(r.text)

