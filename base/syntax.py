#
#





# ----------------------
# 命名规范
# ----------------------


"""
在 Python 里，标识符有字母、数字、下划线组成。
在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
Python 中的标识符是区分大小写的。
以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入；
以双下划线开头的 __foo 代表类的私有成员；以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
"""

# ----------------------
# 多行语句
# ----------------------
'''
Python语句中一般以新行作为为语句的结束符
但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：
'''

total = "11" + \
        "22" + \
        "33"
print(total)

"""
语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：
"""
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)

# ----------------------
# 注释写法
# ----------------------

# -*- coding: UTF-8 -*-
# 文件名：test.py


'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

# ----------------------
# 数据类型
# ----------------------

# 创建一个整型对象，值为1，三个变量被分配到相同的内存空间上
a = b = c = 1

# 以上实例，两个整型对象1和2的分配给变量 a 和 b，字符串对象 "john" 分配给变量 c。
a, b, c = 1, 2, "john"

"""
标准数据类型
在内存中存储的数据可以有多种类型。
例如，一个人的年龄可以用数字来存储，他的名字可以用字符来存储。
Python 定义了一些标准类型，用于存储各种类型的数据。
Python有五个标准的数据类型：
    Numbers（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Dictionary（字典）
"""

var1 = 1
var2 = 2
var3 = 3
# 使用del语句删除一些对象的引用,删除单个或多个对象的引用
del var1
del var2, var3

# Numbers（数字）
"""
int	        long	                  float	          complex
10	      51924361L	                   0.0	           3.14j
100	      -0x19323L	                   15.20	       45.j
-786	  0122L	                       -21.9	       9.322e-36j
080	      0xDEFABCECBDAECBFBAEl	       32.3e+18	       .876j
-0490	  535633629843L	               -90.	           -.6545+0J
-0x260	  -052318172735L	           -32.54e100	   3e+26J
0x69 	 -4721885298529L	           70.2E-12	       4.53e-7j

Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
"""

# String（字符串）
str = 'Hello World!'

print(str)  # 输出完整字符串
print(str[0])  # 输出字符串中的第一个字符
print(str[2:5])  # 输出字符串中第三个至第五个之间的字符串
print(str[2:])  # 输出从第三个字符开始的字符串
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 输出连接的字符串

# Hello World!
# H
# llo
# llo World!
# Hello World!Hello World!
# Hello World!TEST


# List（列表）
t_list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(t_list)  # 输出完整列表
print(t_list[0])  # 输出列表的第一个元素
print(t_list[1:3])  # 输出第二个至第三个的元素
print(t_list[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)  # 输出列表两次
print(t_list + tinylist)  # 打印组合的列表

# ['runoob', 786, 2.23, 'john', 70.2]
# runoob
# [786, 2.23]
# [2.23, 'john', 70.2]
# [123, 'john', 123, 'john']
# ['runoob', 786, 2.23, 'john', 70.2, 123, 'john']



# Tuple（元组）
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出第二个至第三个的元素
print(tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)  # 输出元组两次
print(tuple + tinytuple)  # 打印组合的元组

# ('runoob', 786, 2.23, 'john', 70.2)
# runoob
# (786, 2.23)
# (2.23, 'john', 70.2)
# (123, 'john', 123, 'john')
# ('runoob', 786, 2.23, 'john', 70.2, 123, 'john')

tuple = ('runoob', 786, 2.23, 'john', 70.2)
t_list = ['runoob', 786, 2.23, 'john', 70.2]
tuple[2] = 1000  # 元组中是非法应用
t_list[2] = 1000  # 列表中是合法应用

# Dictionary（字典）
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tiny_dict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # 输出键为'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tiny_dict)  # 输出完整的字典
print(tiny_dict.keys())  # 输出所有键
print(tiny_dict.values())  # 输出所有值

# This is one
# This is two
# {'dept': 'sales', 'code': 6734, 'name': 'john'}
# ['dept', 'code', 'name']
# ['sales', 6734, 'john']



# 数据类型转换
'''
函数                      描述
int(x [,base])          将x转换为一个整数
long(x [,base] )        将x转换为一个长整数
float(x)                将x转换到一个浮点数
complex(real [,imag])   创建一个复数
str(x)                  将对象 x 转换为字符串
repr(x)                 将对象 x 转换为表达式字符串
eval(str)               用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)                将序列 s 转换为一个元组
list(s)                 将序列 s 转换为一个列表
set(s)                  转换为可变集合
dict(d)                 创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)            转换为不可变集合
chr(x)                  将一个整数转换为一个字符
unichr(x)               将一个整数转换为Unicode字符
ord(x)                  将一个字符转换为它的整数值
hex(x)                  将一个整数转换为一个十六进制字符串
oct(x)                  将一个整数转换为一个八进制字符串
'''
