# 列表
# https://www.runoob.com/python3/python3-data-structure.html
# Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能。
# 将列表当做堆栈使用
# 将列表当作队列使用
# 列表推导式


# del 语句
# 使用 del 语句可以从一个列表中根据索引来删除一个元素，而不是值来删除元素。这与使用 pop() 返回一个值不同
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

# 可以用 del 删除实体变量
del a




# 元组和序列
# 元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号， 不过括号通常是必须的（如果元组是更大的表达式的一部分）
t = 12345, 54321, 'hello!'





# 集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
#可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}



# 字典
# 构造函数 dict() 直接从键值对元组列表中构建字典
a = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
  print (k, v)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
  for i, v in enumerate(['tic', 'tac', 'toe']):
    print (i, v)
# 同时遍历两个或更多的序列，可以使用 zip() 组合。
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
  print ('What is your {0}?  It is {1}.'.format(q, a))

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数。
for i in reversed(range(1, 10, 2)):
    print(i)

# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值。
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print(sorted(basket))
for f in sorted(set(basket)):
    print(f)