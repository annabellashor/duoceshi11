# coding=utf-8
import unittest
import requests
from config.config import *
from api.api import Cms

class Case(Cms):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.session=Cms().get_session()
    def test04_findtext(self):
        response=self.session.post(url=findtext_url,data=findtext_data)
        assert response.json()["msg"]=="查询栏目成功"