"""
======================
Author: 柠檬班-小简
Time: 2020/6/10 21:38
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
"""
定义测试类 ，继承unittest.TestCase
在测试类当中，以test_开头，定义测试函数。
每一个test_开头的函数，就是一个测试用例。
编写用例：
    1、测试数据
    2、测试步骤 
    3、断言：预期结果与实际结果的比对
       AssertionError: 断言失败 - 用例失败
       assert 表达式(True表示通过，False表示失败)
       self.assertXXXXX()
"""

import unittest
from class_unittest.login import login_check


class TestLogin(unittest.TestCase):

    def test_login_ok(self):
        # 1、测试数据 # 2、测试步骤
        res = login_check("python27","lemonban")
        # 3、断言：预期结果与实际结果的比对
        self.assertEqual(res,{"code": 0, "msg": "登录成功"})


    def test_login_wrong_passwd(self):
        res = login_check("python27","lemonban1")
        self.assertEqual(res, {"code": 1, "msg": "账号或密码不正确"})

    def test_login_wrong_user(self):
        res = login_check("python30","lemonban")
        self.assertEqual(res, {"code": 1, "msg": "账号或密码不正确"})
#username=None, password=None
    def test_login_no_passwd(self):
        res = login_check(username = "python27")
        self.assertEqual(res, {"code": 1, "msg": "所有的参数不能为空"})

    def test_login_no_user(self):
        res = login_check(password = "lemonban")
        self.assertEqual(res, {"code": 1, "msg": "所有的参数不能为空"})

