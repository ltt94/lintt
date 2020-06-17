# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     1
   Description :
   Author :       lintt
   date：          2020/6/5
-------------------------------------------------
   Change Activity:2020/6/5:
-------------------------------------------------
"""
import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")
from selenium import webdriver
import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        # 创建浏览器对象
        self.driver = webdriver.chrome()
        # 设置网页加载时间
        self.driver.implicitly_wait(15)
        # 定义url(setUP创建时首次执行的url)
        self.url = 'http://139.9.119.10:9010/'
    def Test_login(self):
        # 发起请求
        self.driver.get(self.url)
        # 找到用户名的输入框 placeholder="登录账号"
        #username = self.driver.find_element_by_id('id_username')
        username = self.driver.find_element_by_css_seletor("[placeholder='登录账号']")
        # 输入姓名
        username.send_keys('lintt')
        # 找到密码输入框
        #password = self.driver.find_element_by_id('id_password')
        password = self.driver.find_element_by_css_seletor("[placeholder='登录密码']")
        # 输入密码
        password.send_keys('12345678')
        # 点击登录按钮
        #self.driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
        self.driver.find_element_by_class_name("loginbtn")
        # if password=='123456' and username=='admin':
        #     print '登录成功'
        # else:
        #     # 设置网页加载时间
        #     self.driver.implicitly_wait(15)
        #     # 获取页面错误信息
        #     text = self.driver.find_element_by_xpath('//div[@class="alert alert-danger errornote"]/p/text()')
        #     print text



    # 结束请求
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()