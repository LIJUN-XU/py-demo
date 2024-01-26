# Python两种输出值的方式: 
# 表达式语句
# print() 函数
# 第三种方式是使用文件对象的 write() 方法



# 输出的形式更加多样,str.format() 函数来格式化输出值
# 输出的值转成字符串，可以使用 repr() 或 str() 函数来实现

# str()： 函数返回一个用户易读的表达形式
# repr()： 产生一个解释器易读的表达形式
#  repr() 函数可以转义字符串中的特殊字符,参数可以是 python 的任何对象
hello = 'hello, runoob\n hihi'
print(hello)
print(repr(hello))
print(str(hello))



# rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
#  ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串
# zfill(), 它会在数字的左边填充 0






# str.format() 
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))

# 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换
# 在括号中的数字用于指向传入对象在 format() 中的位置
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))

# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

#位置及关键字参数可以任意的结合
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))

#!a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化
import math
print('常量 PI 的值近似为： {!r}。'.format(math.pi))

# 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
  print('{0:10} ==> {1:10d}'.format(name, number))


# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。

# 最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值 :
  print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

  print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
  # print(**table)


line = '==================='
print(line)








# input()
# filename：包含了你要访问的文件名称的字符串值
  # mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
# open(filename, mode)
  

# Using the with statement is generally preferred over directly using open() because it ensures that the file is properly saved and closed after the block of code is executed. This helps to avoid resource leaks and makes the code more readable.
# if you're not using the with keywors,then you should call f.close() to close the file and immediately free up any system resources used by it.
# 打开一个文件
f = open("./test.txt", "r+") # w+

# with open("./test.txt", "w") as f:
  # f.write("这是一个测试文件，用于测试文件读写的功能。")
# r+ 虽然光标是从文件开头开始输入数据，但是，它会把原来的数据覆盖，输入多少覆盖多少

f.write( "Python 是一个非s常好w的d语w言。\n是的，的确非常好!!\n" )


str = f.read()
print('e===',str)

print('f==================')
f.seek(0,0)   # 如果 open 的 mode 是 w+ ，光标则会在文件的末尾，所以 无论是 read 还是 readline 读取到的数据都是空。 再写完数剧或者读完数据后使用seek（）要将光标移到文件开头
str = f.readline() #会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行
print(str)

f.seek(0,0)
str = f.readlines()  #将返回该文件中包含的所有行
print(str)

# 用于返回文件当前的读/写位置
print(f.tell())

# offset 表示相对于 whence 参数的偏移量，from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾
# f.seek(offset, from_what) 
# seek(-x,2)：表示从文件的结尾往前移动x个字符
# from_what 值为默认为0


# 关闭打开的文件
f.close()   # 使用 with open(),不需要在调用 close()














# pickle 模块
#   python的pickle模块实现了基本的数据序列和反序列化。

# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。

# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
# pickle.dump(obj, file, [,protocol])
  
# 基本接口：
# x = pickle.load(file)
  # 注解：从 file 中读取一个字符串，并将它重构为原来的python对象。
  # file: 类文件对象，有read()和readline()接口。
print(line)
import pickle,pprint,json

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
print(selfref_list)
output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()



#使用pickle模块从文件中重构python对象
# pkl_file = open('data.pkl', 'rb')

# data1 = pickle.load(pkl_file)
# pprint.pprint(data1)

# data2 = pickle.load(pkl_file)
# pprint.pprint(data2)

# pkl_file.close()



data = {"filename": "f1.txt", "create_time": "today", "size": 111}
with open("data.json", "w") as f:
    json.dump(data, f)

print("直接当纯文本读：")
with open("data.json", "r") as f:
    print(f.read())

print("用 json 加载了读：")
with open("data.json", "r") as f:
    new_data = json.load(f)
    print(new_data)
print("字典读取：", new_data["filename"])




# https://mofanpy.com/tutorials/python-basic/interactive-python/pickle-json
# json & pickle



