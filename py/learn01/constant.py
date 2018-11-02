# -*- coding: utf-8 -*-

## 字符串
String = "I am a string"
String01 = 'I am also a string'
String02 = '''I am also a string'''

print(String + "\t" +String01)

## 布尔值
boolean = True
boolean01 = False

print(boolean)
print(boolean01)
## 数值
v_float = 0.133
v_int = 1002
v_kexuejishu = 1.97e9

## 列表
x=[0,1,2,3,67,5,6,7,8,9]
y=[x,x,x]
print(x[4])
x[0]=9
y[0][4]=98
x[0]=x[0]-1

print(x)
print(y)

litr = ['ds','ds','sdds',22,boolean,v_float,0.33] # 多种类型复合，嵌套
print(litr)

## 字典,键-值对

dict_v = {'k01':76,'k02':'v02','k03':x}

print(dict_v['k01'])
print(dict_v['k02'])
print(dict_v['k03'])
