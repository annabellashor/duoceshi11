# coding=utf-8


import unittest
import requests
from config.config import *
from api.api import Cms

class Case(Cms):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.session=Cms().get_session()

    def test07_deltext(self):
        response=self.session.post(url=deltext_url,data=deltext_data)
        assert response.json()["msg"]=="1条已数据删除"