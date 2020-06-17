# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       lintt
   date：          2020/6/2
-------------------------------------------------
   Change Activity:2020/6/2:
-------------------------------------------------
"""
sum=0 #满足条件的总人数
for i in range(1,11):
    age=int(input("please input age:\n"))
    sex = input("please chose the sex:m-boy,f-girl:\n")
    if 10<=age<=12:
        if sex=="f":
            print("you can join the football team!\n")
            sum+=1
        else:
            print("sex not fit\n")
    else:
        print("age not fit\n")
    print(sum)