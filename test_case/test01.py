# coding=utf-8


import unittest
from api.api import Api
import requests

class Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.api=Api()
    def test01_login(self):
        assert self.api.login().status_code==200
    def test02_queryUserList(self):
        assert self.api.queryUserList().status_code==200
    def test03_adduser(self):
        assert self.api.saveuser().status_code==200
if __name__ == '__main__':
    unittest.main()
