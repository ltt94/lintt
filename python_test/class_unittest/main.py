#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: cxa
@contact: 1598828268@qq.com
@site: 
@software: PyCharm
@file: main.py
@time: 2020/6/14 15:19
"""
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
s = unittest.TestLoader().discover(r"D:\LTT\python")
with open('report.html','wb') as fs:
    runner = HTMLTestRunner(fs,title='单元测试报告',tester='亭子')
    runner.run(s)
