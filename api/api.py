# coding=utf-8

import requests
from config.config import *
import unittest

class Api(object):
    def __init__(self):
        self.session=requests.Session()
    def login(self):
        response=self.session.post(login_url,data=login_data)
        return response
    def queryUserList(self):
        response=self.session.post(url=query_url,data=query_data)
        return response
    def saveuser(self):
        response=self.session.post(url=saveuser_url,data=saveuser_data)
        response.status_code
        return response
if __name__ == '__main__':
    a=Api()
    print(a.login())


