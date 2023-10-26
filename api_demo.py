# -*-coding:utf-8-*-
# @Time    :2023/10/2415:14
# @Author  :Ervin Chiu
# @Email   :ErvinChiu@outlook.com
# @File    :api_demo.py
# @Software:PyCharm

import requests

# get 请求

#res = requests.get("https://www.baidu.com")
#print(res)
#print(res.request.headers)
# print(res.status_code)

# http://150.109.156.47:8000/api/get_event_list/?eid=3


# url = "http://150.109.156.47:8000/api/get_event_list"
# param = {"eid": "3"}
# res = requests.get(url, param)
# print(res.json())


import unittest

from http_request import HttpRequest

from ddt import ddt, data

from do_excel import DoExcel

#
# class TestHttpRequest(unittest.TestCase):
#
#     def test_case_00(self):
#         url = "http://150.109.156.47:8000/api/get_event_list"
#         param = {"eid": "1"}
#         res = HttpRequest(url, param).http_request("get")
#         print("第1条用例的执行结果是：{0}".format(res.json()))
#
#     def test_case_01(self):
#         url = "http://150.109.156.47:8000/api/get_event_list"
#         param = {"eid": "2"}
#         res = HttpRequest(url, param).http_request("get")
#         print("第2条用例的执行结果是：{0}".format(res.json()))
#
#     def test_case_02(self):
#         url = "http://150.109.156.47:8000/api/get_event_list"
#         param = {"eid": "3"}
#         res = HttpRequest(url, param).http_request("get")
#         print("第3条用例的执行结果是：{0}".format(res.json()))
#
#     def test_case_03(self):
#         url = "http://150.109.156.47:8000/api/get_event_list"
#         param = {"eid": "6"}
#         res = HttpRequest(url, param).http_request("get")
#         print("第4条用例的执行结果是：{0}".format(res.json()))
#
#
# if __name__ == '__main__':
#     unittest.main()


# test_data = [{"id":"1","url": "http://150.109.156.47:8000/api/get_event_list", "params": {"eid": "1"}, "method": "get"},
#              {"id":"2","url": "http://150.109.156.47:8000/api/get_event_list", "params": {"eid": "2"}, "method": "get"},
#              {"id":"3","url": 'http://150.109.156.47:8000/api/get_event_list', 'params': {'eid': "3"}, "method": "get"}]
# #
#
# @ddt
# class TestHttpRequest(unittest.TestCase):
#
#     @data(*test_data)
#     def test_case_01(self, data_item):
#         print("**********" * 10)
#         print("ddt 分解出来的数据是：{0}".format(data_item))
#
#         res = HttpRequest(data_item["url"], data_item["param"]).http_request(data_item["method"])
#         print("第一条用例的执行结果是{0}".format(res.json()))
#
#
# if __name__ == '__main__':
#     unittest.main()


test_data = DoExcel("data.xlsx", "Sheet1").do_excel()


@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self) -> None:
        self.t = DoExcel("data.xlsx", "Sheet1")

    @data(*test_data)
    def test_case_01(self, data_item):
        print("**********" * 20)
        print("ddt 分解出来的数据是：{0}".format(data_item))

        res = HttpRequest(data_item["url"], eval(data_item["params"])).http_request(data_item["method"])
        print("第{1}条用例执行结果是{0}".format(res.json(),data_item["id"]))
        try:
            self.assertEqual(res.json()["status"], 10200)


            test_result = "Pass"
        except AssertionError as e:
            print("执行接口测试出错，错误是{0}".format(e))

            test_result = "Fail"
            #raise e

        finally:
                self.t.write_back(data_item["id"] + 1, 7, str(res.json()))
                self.t.write_back(data_item["id"] + 1, 8,test_result)
    def tearDown(self) -> None:
        print("测试结束！")


if __name__ == '__main__':
    unittest.main()
