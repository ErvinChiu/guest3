# -*-coding:utf-8-*-
# @Time    :2023/10/2416:08
# @Author  :Ervin Chiu
# @Email   :ErvinChiu@outlook.com
# @File    :http_request.py
# @Software:PyCharm

import requests


class HttpRequest:

    # 创建初始化函数，每次请求都需要提供URL和param两个必备参数
    def __init__(self, url, param):
        self.url = url
        self.param = param

    def http_request(self, method, cookies=None):  # 定义默认值

        if method.upper() == "GET":
            try:
                res = requests.get(self.url, self.param, cookies=cookies)
            except Exception as e:
                print("执行get 请求报错，错误是：{0}".format(e))

                res = "Error:get 请求报错{0}".format(e)
        elif method.upper == "POST":
            try:
                res = requests.post(self.url, self.param, cookies=cookies)
            except Exception as e:
                print("执行post 请求报错，错误是{0}".format(e))
                res = "Error:post 请求报错{0}".format(e)
        else:
            print("你的请求方式不对")
            res = "Error :请求方式不对报错{0}".format(method)
        return res
