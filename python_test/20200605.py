# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     20200605
   Description :
   Author :       lintt
   date：          2020/6/8
-------------------------------------------------
   Change Activity:2020/6/8:
-------------------------------------------------
"""
'''
第一题
类属性怎么定义？ 实例属性怎么定义？
# 类属性是同一个类中所有实例共有的，在类体中独立定义，引用时要用“类名.类变量名”（中间一个.号）形式引用，如果某个实例对其修改，则影响这个类中所有实例
实例属性既使在同一个类中也是互不关联，互不影响。定义是使用“self.属性名”，调用时也使用它
第二题
实例方法中的self代表什么
# self在类方法中代表的是类，即Class,即class self;
# self在实例方法中代表是实例对象，即object self
第三题
类中__init__方法在什么时候会调用的？（简答）
#在实例化类对象的时候调用
'''


'''
5、封装一个学生类Student，(自行分辨定义为类属性还是实例属性，方法定义为实例方法)
-  属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩，
-  方法一：计算总分，
   方法二：计算三科平均分，
   方法三：打印学生的个人信息：我的名字叫XXX，年龄：xxx,性别：xxx。
'''
class Studengt:
    def __init__(self,name,age,sex,english_score,match_score,chinese_score):
        #self.sf = sf
        self.name = name
        self.age = age
        self.sex =sex
        self.english_score = english_score
        self.match_score = match_score
        self.chinese_score = chinese_score
    def score(self):
        score = self.english_score + self.match_score + self.chinese_score
        return  score
    def average(self):
        average = (self.english_score + self.match_score + self.chinese_score)/3
        return average
    def massage(self):
        print('我的名字叫{}，年龄：{},性别：{}'.format(self.name,self.age,self.sex))

name = input('请输入姓名：')
age = int(input('请输入年龄：'))
sex =input('请输入性别：')
english_score = float(input('请输入英语分数：'))
match_score = float(input('请输入数学分数：'))
chinese_score = float(input('请输入语文分数：'))
stu = Studengt(name,age,sex,english_score,match_score,chinese_score)
print(stu.score())
print(stu.average())
stu.massage()



