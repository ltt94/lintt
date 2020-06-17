# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     20200529_01
   Description :
   Author :       lintt
   date：          2020/6/2
-------------------------------------------------
   Change Activity:2020/6/2:
-------------------------------------------------
"""

'''
1、定义函数：（要求：定义函数处理逻辑。input输入操作在函数之外。）
将用户输入的所有数字相乘之后对20取余数
用户输入的数字个数不确定
'''
def Multiplication(num_list):
    list1 = num_list.split(',')
    list2 = []
    # 把字符串转成数字
    for item in list1:
        item2 = float(item)
        list2.append(item2)
    num = 1
    for item in list2:
        num *= item
    yushu = num % 20
    return yushu

'''
2、编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
'''
def check_length(list):
    if len(list) > 2:
        new_list = list[0:2]
    else:
        new_list = list
    return new_list

'''
3、列表去重
定义一个函数 def remove_element(m_list):，将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
'''
def remove_element(m_list):
    s = set(m_list)
    list3 = list(s)
    return list3

'''
4、编写如下程序（要求：定义函数处理逻辑。input输入操作在函数之外。）
尝试函数封装：
输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
b.根据BMI指数，给与相应提醒
低于18.5： 过轻 18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖
'''
def body_mass_index(height,weight):
    BMI = weight / height ** 2
    if BMI < 18.5:
        msg = '过轻'
    elif 18.5 <= BMI < 25:
        msg = '正常'
    elif 25 <= BMI < 28:
        msg = '过重'
    elif 28 <= BMI < 32:
        msg = '肥胖'
    else:
        msg = '严重肥胖'
    return msg

'''
5， 定义一个函数，传入一个字典和字符串，
判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典
'''
def check_dict(str,dict):
    if str not in dict.values():
        dict['new'] = str
    return dict

'''
6.通过定义一个计算器函数，调用函数传递两个参数，
然后提示选择【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。
'''
def Calculator(num1,num2):
    operation =int(input('请选择操作：【1】加 【2】减【3】乘 【4】除'))
    if operation ==1:
        num3 = num1 + num2
    elif operation ==2:
        num3 = num1 - num2
    elif operation == 3:
        num3 = num1 * num2
    elif operation == 4:
        num3 = num1 / num2
    else:
        print('输入错误')
    return operation

'''
7.一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。
编写一个程序，询问用户的性别和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
（要求：定义函数处理逻辑。但是input输入操作在函数之外。在for循环当中，调用input和自己定义的函数)
'''
def find_cheerers(sex,age):
    nums = 0
    if sex == 'f':
        if 15 <= age <= 22:
            nums += 1
        else:
            print('年龄不合适')
    else:
        print('性别不合适')
    print(nums)
    return nums

if __name__ == '__main__':
    print('##########第一题##########')
    # str1 = input('请输入一串数字：')
    # s = Multiplication(str1)
    # print('余数是{}'.format(s))
    print('##########第二题##########')
    # list1 = [1,'我是列表',8]
    # print(check_length(list1))
    print('##########第三题##########')
    # list3 = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
    # print(remove_element(list3))
    print('##########第四题##########')
    # height = float(input('请输入身高(m):'))
    # weight = float(input('请输入体重(kg):'))
    # print(body_mass_index(height,weight))
    print('##########第五题##########')
    # str5 = '花花'
    # dict5 = {'年龄':18,'性别':'女'}
    # print(check_dict(str5,dict5))
    print('##########第六题##########')
    # print(Calculator(2,3))
    print('##########第七题##########')

    for errol in range(0,10):
        sex = input('请输入性别（f OR m）：')
        age = int(input('请输入年龄：'))
        errol += 1
        nums = find_cheerers(sex, age)
        print(nums)


# for i in range(1,11):
#     age=int(input("please input age:\n"))
#     sex = input("please chose the sex:m-boy,f-girl:\n")
#     if 10<=age<=12:
#         if sex=="f":
#             print("you can join the football team!\n")
#             sum+=1
#         else:
#             print("sex not fit\n")
#     else:
#         print("age not fit\n")
#     print(sum)


