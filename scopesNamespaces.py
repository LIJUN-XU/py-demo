# 一般有三种命名空间
# 内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
# 全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
# 局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）
# var1 是全局名称

var1 = 5
def some_func():
 
    # var2 是局部名称
    var2 = 6
    def some_inner_func():
 
        # var3 是内嵌的局部名称
        var3 = 7
        print(var1, var2, var3)
    some_inner_func()
some_func()    
# 作用域
        


# global 和 nonlocal关键字
# 当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。
num = 1
def fun1():
  # global num  # 需要使用 global 关键字声明
  # print(num)  # 在 local namespace 里面有定义 global namespace 同样的参数时，无法获取到全局变量，需要使用 global.
  num = 123
  print(num)
fun1()
print(num)



# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了

# 这样就会报错 因为 test 函数中的 a 使用的是局部，未定义，无法修改。 与上面的 global 一样
a = 10
def test():
    a = a + 1
    print(a)
test()





