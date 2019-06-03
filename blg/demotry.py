# a = [1,2,3,4,5]
b = sum(a)
print(b)

# 阶乘递归
def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n - 1)
