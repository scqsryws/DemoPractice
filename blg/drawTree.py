# 分支树
from turtle import Turtle


def tree(plist, l, a, f):
    if l > 5:
        lst = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)

            lst.append(p)
            lst.append(q)
        tree(lst, l * f, a, f)



def main():
    p = Turtle()
    # 笔尺寸
    p.pensize(5)
    # 笔颜色
    p.color("green")
    # 隐藏箭头
    p.hideturtle()

    #
    p.getscreen()
    # 画笔转向
    p.left(90)

    # 提笔
    p.penup()
    # 移动画笔到（x，y）处
    p.goto(0, 0)
    # 落笔
    p.pendown()

    tree([p], 200, 65, 0.6375)


main()


