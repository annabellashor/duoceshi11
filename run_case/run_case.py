# coding=utf-8

from time import strftime
from utils.HTMLTestRunner3_New import HTMLTestRunner
import unittest
import os
bath_path=os.path.dirname(os.path.dirname(__file__))
report_path=bath_path+"/"+"report"
test_case_path=bath_path+"/"+"test_case"
now=strftime("%Y-%m-%d_%H_%M_%S")
file=report_path+'\\'+now+"api自动化测试报告.html"
f=open(file,'wb')
start_dir=test_case_path
discover=unittest.defaultTestLoader.discover(start_dir=start_dir,pattern="test*.py")
runner=HTMLTestRunner(stream=f,
                      title="api自动化测试报告",
                      description="用例执行情况如下：",
                      tester="小刘")
runner.run(discover)

# print(bath_path)