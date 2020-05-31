## 目录结构

```
- src/com/sangyu
    - bin  启动入口存放可执行的文件
    - utils 封装依赖的类
    - libs  第三方库
    - tests 测试代码
    - core 核心代码
    - docs 文档
    - result HTMLTestRunner的执行结果
```

## 实现的功能

1. 处理excel的接口用例转成可执行的接口请求
2. 响应的数据的断言逻辑
3. 执行结果回填到excel
4. 执行结果的邮件发送
5. Jenkins的定时执行
