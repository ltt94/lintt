# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     20200520
   Description :
   Author :       lintt
   date：          2020/5/21
-------------------------------------------------
   Change Activity:2020/5/21:
-------------------------------------------------
"""
"""1、现在有字符串：str1 = 'python cainiao 666'

    1、请找出第 5 个字符。  
    2、请复制一份字符串，保存为 str_two(使用赋值哦)
    3、请找出最中间的字符。（字符串长度是偶数。）
"""
str1 = 'python cainiao 666'
#1、请找出第 5 个字符
print(str1[4])
#2、请复制一份字符串，保存为 str_two(使用赋值哦)
str_two = str1[:]
print(str_two)
#3、请找出最中间的字符。（字符串长度是偶数。）
len1 = int(len(str1)/2)
print(str1[len1])


"""
2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，和重量，最后计算出应该支付的金额！
（不需要校验数据，都传入数字就可以了。）
 (使用input方法获取用户输入哦)
"""
price = float(input("请输入橘子价格："))
weight = float(input("请输入橘子重量："))
total = weight*price
print("橘子总价为：" , total)


"""3.演练字符串操作
my_hobby = "Never stop learning!"
截取从 位置2 ~ 位置6 的字符串
截取从 位置2 ~ 末尾 的字符串
截取从 开始位置~ 位置6 的字符串
截取完整的字符串
从 索引3 开始，每2个字符中取一个字符
截取字符串末尾两个字符
字符串的倒序
说明：“位置”指的是字符所处的位置（比如位置1，指的是第一个字符“N”），
      “索引”指的是字符的索引值（比如索引0， 代表的是第一个字符“N”）
"""
my_hobby = "Never stop learning!"
print('截取从 位置2 ~ 位置6 的字符串:',my_hobby[2:5])
print('截取从 位置2 ~ 末尾 的字符串：',my_hobby[2:])
print('截取从 开始位置~ 位置6 的字符串：',my_hobby[:5])
print('截取完整的字符串：',my_hobby[:])
print(my_hobby[3::2])
print(my_hobby[-2:-1])
print(my_hobby[::-1])