'''
goods = [
{"name":"电脑","price":1999},
{"name":"鼠标","price":10},
{"name":"游艇","price":20},
{"name":"美女","price":998}
]

功能需求：
要求用户输入自己拥有总资产
例如：2000，显示商品列表，让用户根据序号选择商品，加入购物车购买
如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
'''

money = int(input("请输入您的总资产："))
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]

for i in range(0, 4):
    print(i+1, goods[i]["name"], goods[i]["price"])


Num = input("请输入选择序号").split(',')
sum = 0
for i in Num:
    i = int(i)
    i = i-1
    sum = sum + goods[i]["price"]

if sum <= money:
    money = money - sum
    print("购买成功，余额为{}".format(money))
else:
    print("账户余额不足")