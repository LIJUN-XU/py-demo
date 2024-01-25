# ; try/except
# 一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行
# 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
# 最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。
while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise   


# try/except...else
# try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。

# else 子句将在 try 子句没有发生任何异常的时候执行。
# try 执行代码
# except 发生异常时执行的代码
# else 没有异常时执行的代码
# finally 无论是否发生异常都会执行的代码
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
    finally:
        print('这句话，无论异常是否发生都会执行。')

# raise 触发异常
        raise Exception('这是一个异常')

# try-finally 语句
        
        #https://www.runoob.com/python3/python3-errors-execptions.html