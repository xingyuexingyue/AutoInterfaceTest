"""
这个类主要是将一个case封装成一个class对象


user: 2020 by pyp
"""


class CaseData:
    test_id = ''
    test_features = ''
    test_url = ''
    test_result = ''

    def __init__(self, test_id, test_features, test_url, test_result):
        self.test_id = test_id
        self.test_features = test_features
        self.test_url = test_url
        self.test_result = test_result

    def getId(self):
        return self.test_id

    def getFeatures(self):
        return self.test_features

    def getUrl(self):
        return self.test_url

    def getResult(self):
        return self.test_result
