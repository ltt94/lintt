# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     20200507-02
   Description :
   Author :       lintt
   date：          2020/5/28
-------------------------------------------------
   Change Activity:2020/5/28:
-------------------------------------------------
"""
# 石头剪刀布游戏
import random
print('###################################################################')
print('---石头剪刀布游戏开始---')
print('请按下面提示出拳：'
      '石头【1】  剪刀【2】  布【3】  退出【4】')
list1 = ['石头','剪刀','布']
computer = random.randint(1,3)#1,2,3,4
t2 = list1[computer-1]
print(computer,t2)


n = int(input('请输入你的选项：'))
t1 = list1[n-1]
print(n,t1)
while n <= 4:
    if n != 4:
        if n > computer:
            print('您的出拳：{},电脑出拳：{},您失败了'.format(t1,t2))
            n = int(input('请再次输入你的选项：'))
        elif n < computer:
            print('您的出拳：{},电脑出拳：{},您胜利了'.format(t1, t2))
            n = int(input('请再次输入你的选项：'))
        else:
            print('您的出拳：{},电脑出拳：{},此局平局'.format(t1, t2))
            n = int(input('请再次输入你的选项：'))
    else:
        print('退出程序')
        break

print('###################################################################')
print('---周几游戏---')
weekList = ['周一','周二','周三','周四','周五','周末' ]
week = int(input('请输入数字：'))
while 1:
    if week < 6:
        print('今天是{}'.format(weekList[week-1]))
        break
    elif week ==6 or week == 7:
        print('今天是周末')
        break
    else:
        print('输入错误，请重新输入')
        week = int(input('请输入数字：'))
