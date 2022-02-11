# coding=utf-8


import unittest
from api.api import Api
import requests

class Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.api=Api()
    def test01_login(self):
        assert self.api.login()["msg"]=="登录成功！"
    def test02_queryUserList(self):
        assert self.api.queryUserList()["msg"]=="查询用户成功！"
    def test03_adduser(self):
        assert self.api.saveuser()["msg"]=="保存用户信息失败,登录帐号已存在！"
    def test04_findtext(self):
        assert self.api.findtext()["msg"]=="查询栏目成功"
    def test05_savetext(self):
        assert self.api.savetext()["msg"]=="保存栏目失败，栏目目录已存在！"
    # def test06_deluser(self):
    #     assert self.api.deluser()["msg"]=="1条数据删除成功！"
    # def test07_deltext(self):
    #     assert self.api.deltext()["msg"]=="1条已数据删除"


if __name__ == '__main__':
    unittest.main()
