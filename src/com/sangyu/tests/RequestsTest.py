'''
练习requests库的使用
1. 当前python环境安装pip3 install requests
2. 主要API使用（参考官方文档）
3. 安装 pip3 install Pillow

'''
import json
from io import BytesIO

from PIL import Image

import requests

response = requests.request('get','http://httpbin.org/get') # 返回请求结果的响应码
print(response)

'''
四种请求方式
'''
res1 = requests.get('http://httpbin.org/get')  # 发送一个get请求；get类型用来获取数据，请求数据在url中
# print('res1 ->', res1)

res2 = requests.post('http://httpbin.org/post', data={'key': 'value'})  # 发送一个post请求 ，post类型用来提交数据，请求数据在请求体中，就是data中
# print('res2 ->', res2)

res3 = requests.put('http://httpbin.org/put', data={'key': 'value'})  # 发送一个put请求，put类型用来修改数据，请求数据在请求体中
# print('res3 ->', res3)

res4 = requests.delete('http://httpbin.org/delete')  # 发送一个delete请求，delete用来删除数据，请求数据在url中
# print('res4 ->', res4)

'''
给get请求增加请求参数

1. Requests 允许你使用 params 关键字参数，

2. 以一个字符串字典来提供这些参数。

3. 注意字典里值为 None 的键都不会被添加到 URL 的查询字符串里。

4. 字典的value可以是列表
'''
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

res5 = requests.get('http://httpbin.org/get', params=payload)
print('res5 ->', res5)

print('res5.url ->', res5.url)

'''
响应内容(上面我们看到的都是响应码，但是实际用的过程中我们除了需要知道响应码也需要知道响应内容)
1. Requests 会自动解码来自服务器的内容。大多数 unicode 字符集都能被无缝地解码。
2. 请求发出后，Requests 会基于 HTTP 头部对响应的编码作出有根据的推测。
3. 当你访问 r.text 之时，Requests 会使用其推测的文本编码。
4. Requests 使用了什么编码，并且能够使用 r.encoding 属性来改变它
5. 如果你改变了编码，每当你访问 r.text ，Request 都将会使用 r.encoding 的新值
'''

res6 = requests.get('https://api.github.com/events')
res7 = requests.get('http://httpbin.org/get')

print('res6.encoding ->', res6.encoding)
print('res7.encoding ->', res7.encoding)

print('res6.text ->', res6.text)
print('res7.text ->', res7.text)

'''
二进制响应内容
1. 以字节的方式访问请求响应体
2. Requests 会自动为你解码 gzip 和 deflate 传输编码的响应数据
3. 以请求返回的二进制数据创建一张图片
'''
res8 = requests.get('https://api.github.com/events')
print('res8.content ->', res8.content)

# i = Image.open(BytesIO(res8.content))


'''
JSOIN响应内容
1. Requests 中也有一个内置的 JSON 解码器
2. 如果 JSON 解码失败， r.json() 就会抛出一个异常
3. 响应内容是 401 (Unauthorized)，尝试访问 r.json() 将会抛出 ValueError: No JSON object could be decoded 异常。
4. 成功调用 r.json() 并**不**意味着响应的成功.有的服务器会在失败的响应中包含一个 JSON 对象（比如 HTTP 500 的错误细节）
5. 要检查请求是否成功，请使用 r.raise_for_status() 或者检查 r.status_code 是否和你的期望相同
'''
res9 = requests.get('https://api.github.com/events')
print('res9.json() -> ', res9.json())
print('res9.raise_for_status() -> ', res9.raise_for_status())
print('res9.status_code -> ', res9.status_code)

'''
原始响应内容
1. 获取来自服务器的原始套接字响应
2. 确保在初始请求中设置了 stream=True
3. 访问 r.raw
4. 将r.raw读取到数据存储到文件
5. 使用 Response.iter_content 将会处理大量你直接使用 Response.raw 不得不处理的。(这种方式会有问题的要换种方式去实现)

'''

res10 = requests.get('https://api.github.com/events', stream=True)
print('res10.raw ->', res10.raw)
print('res10.raw ->', res10.raw.read(10))

# chunk_size = 10
# filename = '/Users/pengyapan/PycharmProjects/AutoInterfaceTest/src/com/sangyu/docs/test.txt'
# with open(filename, 'wb') as fd:
#     for chunk in res10.iter_content(chunk_size):
#         fd.write(chunk)

'''
定制请求头
1. 如果你想为请求添加 HTTP 头部，只要简单地传递一个 dict 给 headers 参数就可以了
'''

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

'''
更加复杂的 POST 请求
1. 只需简单地传递一个字典给 data 参数。你的数据字典在发出请求时会自动编码为表单形式
2. data 参数传入一个元组列表。在表单中多个元素使用同一 key 的时候，这种方式尤其有效
3. 发送string而不是dict
4. 使用 json 参数直接传递，然后它就会被自动编码
'''

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

payload = (('key1', 'value1'), ('key1', 'value2'))
r = requests.post('http://httpbin.org/post', data=payload)

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)

'''
POST一个多部分编码(Multipart-Encoded)的文件
1. Requests 使得上传多部分编码文件变得很简单
2. 显式地设置文件名，文件类型和请求头
3. 文件设置为字符串
'''
url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=files)
r.text

url = 'http://httpbin.org/post'
files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

r = requests.post(url, files=files)
r.text

url = 'http://httpbin.org/post'
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
r = requests.post(url, files=files)
r.text

'''
1. 如果发送了一个错误请求(一个 4XX 客户端错误，
或者 5XX 服务器错误响应)，我们可以通过 Response.raise_for_status() 来抛出异常：

2. 由于我们的例子中 r 的 status_code 是 200 ，当我们调用 raise_for_status() 时，得到的是：None
'''

bad_r = requests.get('http://httpbin.org/status/404')
bad_r.status_code
bad_r.raise_for_status()

'''
1. 以一个 Python 字典形式展示的服务器响应头
2. r.headers['Content-Type']
'''

r.headers

r.headers['Content-Type']

r.headers.get('content-type')

'''
访问cookie
'''

url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)

r.cookies['example_cookie_name']

'''
发送cookies参数
'''

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)

r.text

'''
Cookie 的返回对象为 RequestsCookieJar，它的行为和字典类似，但接口更为完整，适合跨域名跨路径使用。你还可以把 Cookie Jar 传到 Requests 中
'''

jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'http://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
r.text

'''
重定向与请求历史
1. 可以使用响应对象的 history 方法来追踪重定向。
2. Response.history 是一个 Response 对象的列表，为了完成请求而创建了这些对象
3. 这个对象列表按照从最老到最近的请求进行排序
'''

r = requests.get('http://github.com')
r.url
r.status_code
r.history

'''
如果你使用的是GET、OPTIONS、POST、PUT、PATCH 或者 DELETE，那么你可以通过 allow_redirects 参数禁用重定向处理：
'''

r = requests.get('http://github.com', allow_redirects=False)
r.status_code
r.history

'''
使用了 HEAD，你也可以启用重定向
'''
r = requests.head('http://github.com', allow_redirects=True)
r.url
r.history

'''
1. 你可以告诉 requests 在经过以 timeout 参数设定的秒数时间之后停止等待响应。基本上所有的生产代码都应该使用这一参数。如果不使用，你的程序可能会永远失去响应：

2. timeout 仅对连接过程有效，与响应体的下载无关。 timeout 并不是整个下载响应的时间限制，而是如果服务器在 timeout 秒内没有应答，将会引发一个异常（更精确地说，是在 timeout 秒内没有从基础套接字上接收到任何字节的数据时）
'''
requests.get('http://github.com', timeout=0.001)

'''
错误与异常

1. 遇到网络问题（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出一个 ConnectionError 异常。

2. 如果 HTTP 请求返回了不成功的状态码， Response.raise_for_status() 会抛出一个 HTTPError 异常。

3. 若请求超时，则抛出一个 Timeout 异常。

4. 若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。

5. 所有Requests显式抛出的异常都继承自 requests.exceptions.RequestException 。
'''

############################ 高级用法 ##########################################

'''
会话对象
1. 会话对象让你能够跨请求保持某些参数。
2. 它也会在同一个 Session 实例发出的所有请求之间保持 cookie
3. 所以如果你向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升
'''


# 我们来跨请求保持一些 cookie
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'


# 会话也可用来为请求方法提供缺省数据。这是通过为会话对象的属性提供数据来实现的
s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})
# both 'x-test' and 'x-test2' are sent
s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
# 任何你传递给请求方法的字典都会与已设置会话层数据合并。方法层的参数覆盖会话的参数