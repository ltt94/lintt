#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: cxa
@contact: 1598828268@qq.com
@site: 
@software: PyCharm
@file: register.py
@time: 2020/6/14 15:10
"""
users = [{'user': 'python26', 'password': '123456'}]


def register(username, password1, password2):
    # 判断是否有参数为空
    if not all([username, password1, password2]):
        return {"code": 0, "msg": "所有参数不能为空"}
    # 注册功能
    for user in users:  # 遍历出所有账号，判断账号是否存在
        if username == user['user']:
            # 账号存在
            return {"code": 0, "msg": "该账户已存在"}
        else:
            if password1 != password2:
                # 两次密码不一致
                return {"code": 0, "msg": "两次密码不一致"}
            else:
                if 6 <= len(username) >= 6 and 6 <= len(password1) <= 18:
                    # 注册账号
                    users.append({'user': username, 'password': password2})
                    return {"code": 1, "msg": "注册成功"}
                else:
                    # 账号密码长度不对，注册失败
                    return {"code": 0, "msg": "账号和密码必须在6-18位之间"}


if __name__ == "__main__":
    res = register('python14', '123456', '123456')
    print(res)
