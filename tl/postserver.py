import requests

# 参数用字典表达
'''
data = {"type": "yuantong", "postid": "806028516749165814"}
url = "http://www.kuaidi100.com/query"
result = requests.post(url, data)
remes = result.json()
print(remes)
print(remes["data"])
'''

#
# def redback(a = input("请输入红包金额")):
#     try:
#         a = float(a)
#         if 0.01 <= a <= 200:
#             print("发出红包啦！")
#         else:
#             redback(a = input("请输入红包金额"))
#     except Exception as e:
#         redback(a = input("请输入红包金额"))
#
# redback()


# 断言
# assert 实际结果 == 期望结果