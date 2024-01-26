# 以 python3 教程 https://www.runoob.com/python3/python3-basic-syntax.html 为基础
print('hello world!')
import keyword
print(keyword.kwlist)

item_one = 10
item_two = 20
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句
total = item_one +\
item_two
print(total)

# 删除末尾的换行符
print('hello world!', end='')
print('hello world,hi')


# Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割，以下是一个简单的实例：
# sys.stdout:这个方法，调用的就是 file 对象的 write 方法，区别是 file 对象的 write 方法把字符写入到文件中，而 sys.stdout.write 方法把字符写入标准输出中，就是控制台。
# 这个方法与 print 的区别是：print 默认换行，而她默认不换行。
# print 几乎可以打印所有的对象，而 stdout.write 只能接受 str 类型
import sys; x = 5; sys.stdout.write(str(x) + '\n')
print('sys=',sys.stdout)
# stdout 和 print 可以结合使用的案例。https://blog.csdn.net/CityzenOldwang/article/details/78384412



# 执行下面的程序在按回车键后就会等待用户输入：
input("\n\n按下 enter 键后退出。")
input("按下 enter1 键后退出。")


# 代码组
# 缩进相同的一组语句构成一个代码块，我们称之代码组。
# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
# 我们将首行及后面的代码组称为一个子句(clause)
x = int(input("请输入一个数字:"))
if 5<x < 10:
  print("True")
elif x > 10:
  print("False")
else:
  print("None")




# 导入模块
# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *
import sys
print('================Python import mode==========================')
for i in sys.argv:
  print('sys.argv==',i) # 当前目录文件
print(sys.argv)
print('/n python path is',sys.path)
# sys 模块：sys 模块提供了与 Python 解释器和系统相关的功能



# 导入 sys 模块的 argv,path 成员
from sys import argv,path
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path





