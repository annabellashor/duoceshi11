# coding=utf-8

import unittest
import requests
# from config.config import *
from api.api import Cms
from config.get_value import queryuser_value
from ddt import ddt,data,unpack
import json
@ddt
class Case(Cms):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.session=Cms().get_session()
    @data(*queryuser_value())
    @unpack
    def test02_queryUserList(self,name,method,url,data,herders,exception):
        response=self.session.request(method=method,url=url,data=json.loads(data))
        assert response.json()==json.loads(exception)
        # print(response.json())
    # def test06_deluser(self):
    #     response=self.session.post(url=deluser_url,data=deluser_data)
    #     assert response.json()["msg"]=="1条数据删除成功！"
    # def test07_deltext(self):
    #     assert self.api.deltext()["msg"]=="1条已数据删除"


if __name__ == '__main__':
    unittest.main()