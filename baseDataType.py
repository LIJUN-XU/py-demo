# 基础数据类型
# python 中的变量不需要声明。但是在使用之前必须赋值，只有赋值后变量才会被创建

# a,b,c 都赋值为 1. 从后向前赋值.
a = b = c = 1

# a 赋值为 1，b 赋值为 2，c 赋值为runningNoob
a,b,c = 1,2,"runningNoob"


# 常见的数据类型 6 个
# 不可变数据 ：Number, String,Tuple（元组） 
# 可变数据：List,  Set（集合）, Dictionary







# Number（数字）
# Python3 支持 int、float、bool、complex（复数）。

# 注意：Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
a = 1
b = True
print('1==',a + b)
# isissubclass(), isinstance(), type()

# 数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数, ** 返回乘方
print(2//4,2/4,2**3)



# String（字符串）
# 加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，与之结合的数字为复制的次数
str = 'Runoob'

print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
print (str + "TEST") # 连接字符串

a = True
b = False

# 逻辑运算符
print(a and b) # False  &&
print(a or b)  # True   ||
print(not a)  # False     !

# 类型转换
print(int(a)) 
print(float(b)) 
# print(str(a))





# Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

# 元组中的元素类型也可以不相同

# 1、与字符串一样，元组的元素不能修改。
# 2、元组也可以被索引和切片，方法一样。
# 3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
# 4、元组也可以使用+操作符进行拼接。
tup2 = (20,) # 一个元素，需要在元素后添加逗号




# List（列表）
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
print(a)
a[2:5] = [13, 14, 15]     #js
print(a)

a[2:5] = []  # 将对应的元素值设置为 []  类似删除这几个原神
print(a)

a = [1, 2, 3, 4, 5, 6]
print(a[-3:-1])   # a[-1:-3] 不生效，只能从右往左数    js
a[-1:-3] = ['a']
print(a)
# Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2
print(a[1:5:2])
# 如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：
print(a[::-1])


# Set（集合）
# 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# 无序，可变，存储的元素是唯一的，不会有重复的元素

d = {'Google', 'Runoob', 'Taobao', 'Facebook', 'Zhihu', 'Baidu'}
e = set()
f = {} # dictionary
print(d,e,f,type(f),type(e))

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print('2==',a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素



# Dictionary（字典）
# 基本与 js 对象一致
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
tinydict['name'] = '222'
tinydict['site2'] = 'www.222.com'
print(tinydict)



# 构造函数 dict()
a = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(a)

a = dict(Runoob=1, Google=2, Taobao=3)
print(a)
# 构造函数 dict() 


a = {x: x**2 for x in (2, 4, 6)}
print(a)
# python 推导式 https://www.runoob.com/python3/python-comprehensions.html






# bytes 类型
# bytes 类型表示的是不可变的二进制序列,元素是整数值（0 到 255 之间的整数），而不是 Unicode 字符
# bytes 类型通常用于处理二进制数据，比如图像文件、音频文件、视频文件等等。
# 创建 bytes 对象的方式有多种，最常见的方式是使用 b 前缀
# bytes() 函数的第一个参数是要转换的对象，第二个参数是编码方式，如果省略第二个参数，则默认使用 UTF-8 编码
x = bytes("hello", encoding="utf-8")
print(x)
x = b"hello"
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b"world"  # 拼接操作，得到 b"helloworld"
print(z,z[0])
print(z[0] == b'h')
print(z[0] == ord('h'))
# ord() 函数用于将字符转换为相应的整数值




