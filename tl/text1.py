def collect():
    global s
    sex = input("请输入性别（m/f）：")
    if sex == "m":
        print("这个孩子不可以加入球队")
    elif sex == "f":
        age = int(input("请输入年龄："))
        if (10 <= age) and (age <= 12):
            print("这个孩子可以加入球队")
            s = s+1
        else:
            print("这个孩子不可以加入球队")
    else:
        print("输入错误，请重新输入")
        collect()
    return s


s = 0


for i in range(1, 11):
    collect()
    print(i)
print(collect())
