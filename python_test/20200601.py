#!/usr/bin/env python 
# encoding: utf-8 

"""
@version: v1.0
@author: cxa
@contact: 1598828268@qq.com
@site: 
@software: PyCharm
@file: 20200601.py
@time: 2020/6/2 23:04
"""
"""
1、有以下数据来自于一个嵌套字典的列表（可自定义这个列表），格式如下：
person_info = [{"name":"yuze", "age": 18, "gender": "男", "hobby": "假正经", "motto": "I am yours"} ,  .... 其他]
创建一个txt文本文件，来添加数据
a.第一行添加如下内容：
name,age,gender,hobby,motto

b.从第二行开始，每行添加具体用户信息，例如：
yuze,17,男,假正经, I am yours
cainiao,18,女,看书,Lemon is best!
"""
person_info = [{"name":"yuze", "age": 17, "gender": "男", "hobby": "假正经", "motto": "I am yours"},
               {"name":"cainiao", "age": 18, "gender": "女", "hobby": "看书", "motto": "Lemon is best!"}]
with open('./data/test.txt','w',encoding="utf-8") as f:
    f.write('name,age,gender,hobby,motto\n')
    #把字段的关键字取出来作为标题
    title = []
    for item in person_info:
        for key in item.keys():
            if key not in title:
                title.append(key)
    f.write(' \t '.join(title)+'\n')
    # person_info[0].values() 是dict_value，不能直接写入文件，要转换成str，数字也要转换成str
    #写入第一个字典
    f.write(" \t ".join('%s' %id for id in person_info[0].values()) + '\n')
    # 写入第二个字典
    f.write(" \t ".join('%s' % id for id in person_info[1].values()) + '\n')

'''
编写如下程序
有两行数据，存放在txt文件里面(手动建立文件，并添加如下数据)：
url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
url:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000

请利用上课所学知识，把txt里面的两行内容，取出然后返回如下格式的数据：（可定义函数）
[{'url':'/futureloan/mvc/api/member/register','mobile':'18866668888','pwd':'123456'},
{'url':'/futureloan/mvc/api/member/recharge','mobile':'18866668888','amount':'1000'}]
'''
def data(open_path,read_path):
    with open(open_path,'w',encoding='utf-8') as file:
        file.write('url:/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456\nurl:/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000')
    rf = open(read_path,'r')
    list1 = rf.readlines()
    #print(list1)
    list2 = []
    for items in list1:
        # print(items.split('@'))
        dict1 = {}
        for item in items.split('@'):
            # print(item)
            dict1[item.split(':')[0]] = item.split(':')[1]
            #print(dict1)
            list2.append(dict1)
    #print(list2)
    return list2

if __name__ == '__main__':
    path = './data/test0601_02'
    data = data(path,path)
    print(data)