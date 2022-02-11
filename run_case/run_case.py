# coding=utf-8

from time import strftime
from utils.HTMLTestRunner3_New import HTMLTestRunner
import unittest
now=strftime("%Y-%m-%d_%H_%M_%S")
file=r"C:\python\api_auto\report"+'\\'+now+"api自动化测试报告.html"
f=open(file,'wb')
start_dir=r"C:\python\api_auto\test_case"
discover=unittest.defaultTestLoader.discover(start_dir=start_dir,pattern="test*.py")
runner=HTMLTestRunner(stream=f,
                      title="api自动化测试报告",
                      description="用例执行情况如下：",
                      tester="小刘")
runner.run(discover)
