# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     20200608
   Description :
   Author :       lintt
   date：          2020/6/9
-------------------------------------------------
   Change Activity:2020/6/9:
-------------------------------------------------
"""
'''
1， 详细总结类和对象知识点，包括：
类的定义:使用 class 语句来创建一个新类，class之后为类的名称(通常首字母大写)并以冒号结尾
对象的初始化:__init__(),当创建这个类的实例时就会调用该方法
类属性:直接在类中创建的属性,而类属性有且只有1份，
       创建的实例都会继承自唯一的类属性,所有的实例都可以访问类属性，且访问的类属性是同一个，一旦类属性改变就会影响到所有的实例
实例属性:1.类被实例化后才会具有的属性2.一般在_init_()方法中创建并初始化3.直接使用即定义：self.<属性名>4.引用方法：self.<属性名>
实例方法:当被实例化之后，才可以被调用，才可以实现方法体。带有self参数
类方法:由类调用，在方法上面添加装饰器@classmethod来修饰.带有cls参数
静态方法:由类调用，不需要参数，需要装饰器@staticmethod修饰

继承:继承是一种创建新的类的方式，新创建的叫子类，继承的叫父类、超类、基类。子类可以使用父类的属性（特征、技能）
重写:如果父类方法的功能不能满足需求，可以在子类重写父类的方法
super 函数:类继承之后为了调用被重写的父类方法,super().方法名()-调用父类同名方法
'''
'''
2， 定义一个类 Dog, 包含 2 个属性：名字和年龄。
定义一个方法 eat 吃东西。
定义一个类 TeddyDog, 继承 Dog 类， Teddy 在吃东西的时候还会望着你，  定义方法 watch_you.
定义一个类 BabyTeddyDog, 继承 TeddyDog,  BabyTeddy 吃东西不仅会望着你，还会四处转悠， 定义方法 go_around
'''
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print('{}吃东西'.format(self.name))
class TeddyDog(Dog):
    def watch_you(self):
        super().eat()
        print('还会望着你')
class BabyTeddyDog(TeddyDog):
    def go_around(self):
        super().watch_you()
        print('还会四处转悠')

btdog = BabyTeddyDog('小狗',16)
btdog.go_around()