# coding=utf-8

import requests
from config.config import *
import unittest

class Api(object):
    def __init__(self):
        self.session=requests.Session()
    def login(self):
        response=self.session.post(login_url,data=login_data)
        return response.json()
    def queryUserList(self):
        response=self.session.post(url=query_url,data=query_data)
        return response.json()
        print(response.json())
    def saveuser(self):
        response=self.session.post(url=saveuser_url,data=saveuser_data)
        return response.json()
        print(response.json())
    def findtext(self):
        response=self.session.post(url=findtext_url,data=findtext_data)
        return response.json()
        print(response.json())
    def savetext(self):
        response=self.session.post(url=savetext_url,data=savetext_data)
        return response.json()
        print(response.json())
    def deluser(self):
        response=self.session.post(url=deluser_url,data=deluser_data)
        return response.json()
        print(response.json())
    def deltext(self):
        response=self.session.post(url=deltext_url,data=deltext_data)
        return response.json()
        print(response.json())
if __name__ == '__main__':
    a=Api()
    a.login()
    print(a.deltext())


