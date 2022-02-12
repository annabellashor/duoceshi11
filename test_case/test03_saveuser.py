# coding=utf-8
import unittest
import requests
from config.config import *
from api.api import Cms

class Case(Cms):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.session=Cms().get_session()
    def test03_adduser(self):
        response=self.session.post(url=saveuser_url,data=saveuser_data)
        assert response.json()["msg"]=="保存用户信息失败,登录帐号已存在！"
