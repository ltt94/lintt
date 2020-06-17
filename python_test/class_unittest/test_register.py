#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: cxa
@contact: 1598828268@qq.com
@site: 
@software: PyCharm
@file: test_register.py
@time: 2020/6/14 15:19
"""
"""
函数入参：
注意：参数传字符串类型，不需要考虑其他类型。
参数1：账号  
参数2：密码1
参数2：密码2 


函数内部处理的逻辑：
   判断是否有参数为空，
    判断账号密码是否在6-18位之间，
    判断账号是否被注册过，
    判断两个密码是否一致。
    上面添加都校验通过才能注册成功，其他情况都注册失败，
各种情况的返回结果如下：  
   注册成功               返回结果：{"code": 1, "msg": "注册成功"}
   有参数为空，            返回结果 {"code": 0, "msg": "所有参数不能为空"}   
   两次密码不一致          返回结果：{"code": 0, "msg": "两次密码不一致"}
   账户已存在             返回结果：{"code": 0, "msg": "该账户已存在"}
   密码不在6-18位之间      返回结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}              
   账号不在6-18位之间      返回结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}


作业要求：请设计用例，对此功能函数进行单元测试，           

提示：上面已经被注册的账号：python26
提示：不需要去看功能函数内部的代码是怎么实现的，也不要改里面的代码，直接复制过去就好，函数内部有bug,自己设计用例去测，测到了自己记录下来
"""
import unittest
from class_unittest.register import register
#from register import register

from ddt import ddt,data
datas = [
    {'user': 'python30', 'password1': '123456', 'password2': '123456','check':{"code": 1, "msg": "注册成功"}},
    {'user': 'python30', 'password1': '123456', 'password2': '','check':{"code": 0, "msg": "所有参数不能为空"}},
    {'user': 'python30', 'password1': '123456', 'password2': '123455','check':{"code": 0, "msg": "两次密码不一致"}},
    {'user': 'python26', 'password1': '123456', 'password2': '123456','check':{"code": 0, "msg": "该账户已存在"}},
    {'user': 'python30', 'password1': '12345', 'password2': '12345','check':{"code": 0, "msg": "账号和密码必须在6-18位之间"}},
    {'user': 'p30', 'password1': '123456', 'password2': '123456','check':{"code": 0, "msg": "账号和密码必须在6-18位之间"}}
]
@ddt
class TestRegister(unittest.TestCase):
    @data(*datas)
    def test_sucess(self,case):
        res = register(case["user"], case['password1'], case['password2'])
        self.assertEqual(res,case["check"])


