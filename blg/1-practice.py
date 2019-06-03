'''
# （1）字符串拼接
str1 = input("请输入")
str2 = input("请输入")

print("第一个人的名字叫{}，第二个人的名字叫{}".format(str1, str2))
'''

'''
# (2)整数序列求和
def add(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(sum)


N = int(input("请输入一个正整数"))
add(N)
'''

'''
# (3)打印99乘法表
# way1
for row in range(1, 10):
    for col in range(1, row + 1):
        z = str(row * col)
        print(z.zfill(2), end=" ")
    print("")
'''
'''
# way2
for i in range(1,10):
    for j in range(1,i + 1):
        print("{}*{}={:2}".format(j,i,i*j), end = " ")
    print("")
'''

'''
# 计算10的阶乘

def f(n):
    if n == 1:
        return 1
    else:
        return f(n-1) * n


sum = 0
for i in range(1, 11):
    sum += f(i)
print("sum = {}".format(sum))
'''
'''
# 猴子吃桃
n = 1
for i in range(1,5):
    n = (n + 1)*2
    print("n=",n)
print(n)'''

'''
# 健康食谱输出
food = ["青菜", "黄瓜", "番茄", "鸡蛋", "五花肉"]
for x in range(0,5):
    for y in range(0,5):
        if x != y:
            Food = food[x] + food[y]
            print(Food)
'''
'''
# 五角星绘制

import turtle

turtle.fillcolor("red")
turtle.begin_fill()
for i in range(0,5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()
'''
'''
# 太阳花
from turtle import Turtle

t = Turtle()
t.pencolor("red")
t.fillcolor("yellow")
t.begin_fill()
t.hideturtle()
while 1:
    t.forward(200)
    t.left(110)
    if abs(t.pos()) < 1:
        break
t.end_fill()
'''

'''
# 绘制彩色螺旋线

import turtle
import time


turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red","yellow","purple","blue"]
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x % 4])
    turtle.left(91)
turtle.tracer(True)
# input()   可以有效解决闪退问题，或者下面的方法
time.sleep(20)
'''
'''
# 温度转换
def TTo(T=input('')):
    if T[-1] == "f" or T[-1] == "F":
        Tn = float(T[:-1])
        t = (Tn - 32) / 1.8
        tt = '%.2f' % t
        print("{}C".format(tt))
    elif T[-1] == "c" or T[-1] == "C":
        Tn = float(T[:-1])
        t = Tn * 1.8 + 32
        tt = '%.2f' % t
        print("{}F".format(tt))
    else:
        print("输入格式错误")


TTo()
'''
'''
n = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
c = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "零"]

p = (input(""))
l = ""
for i in p:
    for x in n:
        if i == x:
            indx = n.index(i)
            C = c[indx]
            l = l + C
print(l)'''

# a = eval(input())
# print("{:+>30.3f}".format(pow(a, 0.5)))


# 常用格式化：
#
# tpl = "i am {}, age {}, {}".format("nick", 18, 'jenny')
# print(tpl)
# tpl = "i am {}, age {}, {}".format(*["nick", 18, 'jenny'])
# print(tpl)
# tpl = "i am {0}, age {1}, really {0}".format("nick", 18)
# print(tpl)
# tpl = "i am {0}, age {1}, really {0}".format(*["nick", 18])
# print(tpl)
# tpl = "i am {name}, age {age}, really {name}".format(name="nick", age=18)
# print(tpl)
# tpl = "i am {name}, age {age}, really {name}".format(**{"name": "nick", "age": 18})
# print(tpl)
# tpl = "i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33])
# print(tpl)
# tpl = "i am {:s}, age {:d}, money {:f}".format("nick", 18, 88888.1)
# print(tpl)
# tpl = "i am {:s}, age {:d}, money {:0.2f}".format("nick", 18, 88888.111111111111)
# print(tpl)
# tpl = "i am {:s}, age {:d}".format(*["nick", 18])
# print(tpl)
# tpl = "i am {name:s}, age {age:d}".format(name="nick", age=18)
# print(tpl)
# tpl = "i am {name:s}, age {age:d}".format(**{"name": "nick", "age": 18})
# print(tpl)
# tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
# print(tpl)
# tpl = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
# print(tpl)
# tpl = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)
# print(tpl)
# y = 0


# for i in range(2,100):
#     for x in range(2,i//2):
#         if i % x == 0:
#             continue
# else:
#     y = y + i
# print(y)


# TemChange.py
# Tempstr = input("请输入变量：")
# if Tempstr[-1] in ['f','F']:
#     T = float(Tempstr[:-1])
#     C = (T - 32) / 1.8
#     print('%.2f' % C)
#     print('{:.2f}'.format(C))
#     print(round(C, 2))

import keyword
print(keyword.kwlist)