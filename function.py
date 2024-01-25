# def 函数名（参数列表）:
#     函数体
def max(a, b):
    if a > b:
        return a
    else:
        return b
 
a = 2
b = 6
print(max(a, b))



# 不定长参数
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 加了两个星号 ** 的参数会以字典的形式导入。
# 如果单独出现星号 *，则星号 * 后的参数必须用关键字传入
def f(a,b,*,c):
    print(c)
    return a+b+c
f(1,2,c=4)  #关键字传入



#lambda
# 匿名函数
x = lambda a : a + 10
print(x(5))

# 将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数
def myfunc(n):
  return lambda a : a * n
 
mydoubler = myfunc(2)
mytripler = myfunc(3)
 
print(mydoubler(11))
print(mytripler(11))






# 不带参数值的 return 语句返回 None




# 强制位置参数
# Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
# 在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

# f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
# f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式
f(10, 20, 30, d=40, e=50, f=60)




# 以下哪个符号用于从包中导入模块 
# .