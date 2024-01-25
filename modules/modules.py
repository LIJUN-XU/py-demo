# import 语句
# 当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入
# 搜索路径是一个解释器会先进行搜索的所有目录的列表。如想要导入模块 support，需要把命令放在脚本的顶端

import support
support.print_func("world")





# 一个模块只会被导入一次，不管你执行了多少次 import。这样可以防止导入模块被一遍又一遍地执行。
# 当我们使用 import 语句的时候，Python 解释器是怎样找到对应的文件的呢？
# 这就涉及到 Python 的搜索路径，搜索路径是由一系列目录名组成的，Python 解释器就依次从这些目录中去寻找所引入的模块。
# 这看起来很像环境变量，事实上，也可以通过定义环境变量的方式来确定搜索路径。
# 搜索路径是在 Python 编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在 sys 模块中的 path 变量
import sys
print(sys.path)
# https://www.runoob.com/python3/python3-module.html








# from modulesName import functionName
# from modulesName import *   引入模块的所有方法






# __name__属性
# 一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
# 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
# __name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格
# 在 support.py 中
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')






#dir() 函数
#  内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
print(dir(support))  
print(dir())  





#标准模块
#https://www.runoob.com/python3/python3-module.html 
#repeat





# 包
# 包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
# 比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。
# 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
#https://www.runoob.com/python3/python3-module.html
#repeat