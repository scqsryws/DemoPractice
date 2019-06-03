while 1:
    a = int(input("请输入a的比分"))
    b = int(input("请输入b的比分"))
    if a == 15 or b == 15:
        print("比赛结束")
        break
    elif a == 7 and b == 0:
        print("比赛结束")
        break
    elif a == 0 and b == 7:
        print("比赛结束")
        break