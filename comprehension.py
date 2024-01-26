# 列表(list)推导式
# [表达式 for 变量 in 列表] 
# [out_exp_res for out_exp in input_list]

# 或者 

# [表达式 for 变量 in 列表 if 条件]
# [out_exp_res for out_exp in input_list if condition]

# out_exp_res：列表生成元素表达式，可以是有返回值的函数。
# for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
# if condition：条件语句，可以过滤列表中不符合条件的值。

names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper() for name in names if len(name)>3]
print(new_names)





# 字典推导式
# { key_expr: value_expr for value in collection }
# 或
# { key_expr: value_expr for value in collection if condition }





# 集合推导式
# { expression for item in Sequence }
# 或
# { expression for item in Sequence if conditional }
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# 元组推导式（生成器表达式）
# 与其他推导式不同的，元组推导式返回的结果是一个生成器对象。
# (expression for item in Sequence )
# 或
# (expression for item in Sequence if conditional )
a = (x for x in range(1,10))
print(a)  #生成器对象
print(tuple(a))

a = [x for x in range(1,10)]
print(a)  #列表
