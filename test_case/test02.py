# coding=utf-8

import unittest
from api.api import Api
import requests

class Case(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.api=Api()
    # def test01_login(self):
    #     assert self.api.login().status_code==200
    # def test02_queryUserList(self):
    #     assert self.api.queryUserList().status_code==200
    # def test03_adduser(self):
    #     assert self.api.saveuser().status_code==200
    # def test04_findtext(self):
    #     assert self.api.findtext().status_code==200
    # def test05_savetext(self):
    #     assert self.api.savetext().status_code==200
    def test06_deluser(self):
        assert self.api.deluser()["msg"]=="1条数据删除成功！"
    def test07_deltext(self):
        assert self.api.deltext()["msg"]=="1条已数据删除"


if __name__ == '__main__':
    unittest.main()