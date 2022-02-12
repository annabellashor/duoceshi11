# coding=utf-8
import unittest
import requests
from config.config import *
from api.api import Cms

class Case(Cms):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.session=Cms().get_session()
    def test06_deluser(self):
        response=self.session.post(url=deluser_url,data=deluser_data)
        assert response.json()["msg"]=="1条数据删除成功！"
