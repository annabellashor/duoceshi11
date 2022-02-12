# coding=utf-8
import unittest
import requests
from config.config import *
from api.api import Cms

class Case(Cms):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.session=Cms().get_session()
    def test05_savetext(self):
        response=self.session.post(url=savetext_url,data=savetext_data)
        assert response.json()["msg"]=="保存栏目失败，栏目目录已存在！"
