# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     judge
   Description :
   Author :       lintt
   date：          2020/6/11
-------------------------------------------------
   Change Activity:2020/6/11:
-------------------------------------------------
"""
class Judge:
    @staticmethod
    def get_judge(str1,str2):
        if str1 == str2:
            judge = 'true'
        else:
            judge = 'false'
        return judge
