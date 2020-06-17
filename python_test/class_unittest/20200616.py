# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     20200616
   Description :
   Author :       lintt
   date：          2020/6/16
-------------------------------------------------
   Change Activity:2020/6/16:
-------------------------------------------------
"""
import os
from openpyxl import load_workbook
DirPath = os.path.dirname(os.path.abspath(__file__))

filePath = os.path.join(DirPath,'注册测试用例数据.xlsx')
wb = load_workbook(filePath)
sh = wb['Sheet1']
titles = []
for item in list(sh.rows)[0]:
    titles.append(item.value)
print(titles)
#方式一
#data_list = []
# for item in list(sh.rows)[1:]:
#     value_dict = {}
#     #print(item)
#     for index in range(len(item)):
#         #print(item[index].value)
#         value_dict[titles[index]] = item[index].value
#         #print(value_dict)
#     data_list.append(value_dict)
# print(data_list)
#方式二
data_list = []
for item in list(sh.rows)[1:]:
    value_list = []
    for i in item:
        value_list.append(i.value)
    data = dict(zip(titles,value_list))
    data_list.append(data)
print(data_list)