# coding=utf-8

import requests
from config.config import *
import unittest
# response=requests.Session().post(url=login_url,data=login_data)
# print(response.json())


class Cms(unittest.TestCase):
    @classmethod
    def set_session(cls):
        cls.session=requests.Session()
    # @classmethod
    # def get_session(cls):
    #     return cls.session
    # def test01_login(self):
    #     response=self.session.post(url=login_url,data=login_data)
    #     assert response.json()["msg"]=="登录成功！"
    #     print(response)

if __name__ == '__main__':
    a=Cms()
    a.set_session()
    a.test01_login()




