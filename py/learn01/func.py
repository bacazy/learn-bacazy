# -*- coding: utf-8 -*-

x=12

y = 2 * x + 5

print("x",x,"y",y)

x=13
y = 2 * x + 5

print("x",x,"y",y)

def func_name(x):
    y = x * 2 + 5
    return y


def func_name1(x):
    return x*2+5


print(func_name(12))
print(func_name1(18))