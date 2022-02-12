# coding=utf-8


import unittest
from api.api import Cms
import requests
# from config.config import *
from ddt import ddt,data,unpack
from config.get_value import login_value,queryuser_value
import json

@ddt
class Case(Cms):
    @classmethod
    def setUpClass(cls) -> None:
        Cms().set_session()
        # cls.session=Cms().get_session()
    @data(*login_value())
    @unpack
    def test01_login(self,name,method,url,data,herders,exception):
        response=self.session.request(method=method,url=url,data=json.loads(data))
        assert response.json()==json.loads(exception)
    # @data(*queryuser_value())
    # @unpack
    # def test02_queryUserList(self,name,method,url,data,herders,exception):
    #     response=self.session.request(method=method,url=url,data=json.loads(data))
    #     assert response.json()==json.loads(exception)
        # print(data)
        # print(response.json())
    # def test03_adduser(self):
    #     response=self.session.post(url=saveuser_url,data=saveuser_data)
    #     assert response.json()["msg"]=="保存用户信息失败,登录帐号已存在！"
    # def test04_findtext(self):
    #     response=self.session.post(url=findtext_url,data=findtext_data)
    #     assert response.json()["msg"]=="查询栏目成功"
    # def test05_savetext(self):
    #     response=self.session.post(url=savetext_url,data=savetext_data)
    #     assert response.json()["msg"]=="保存栏目失败，栏目目录已存在！"



if __name__ == '__main__':
    unittest.main()
