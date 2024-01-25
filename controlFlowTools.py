# if elif else 

# match case 

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 300|302|304:     # 一个 case 也可以设置多个匹配条件，条件使用 ｜ 隔开
             return "Redirection"
        case _: # 类似 default 当其他 case 都无法匹配时，匹配这条
            return "Something's wrong with the internet"

mystatus=400
print(http_error(400))


# 循环
# while 在条件不满足才结束循环
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")

# for 语句
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
  print(site)

# for...else 语句用于在循环结束后执行一段代码。
for x in range(6):
    print(x) # 循环主体
else:
    print("Finally finished!") # 循环结束后执行的代码

# for 实例中使用了 break 语句，break 语句用于跳出当前循环体，而且不会执行 else 子句
    # 注意是跳出循环体，也不执行 else
# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
# continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    if site != "Taobao":
        print("not淘宝!")
        continue
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环==============!")
a= range(2,3)
print(list(a))  # range() 在Python2 返回的是一个列表，在python3里面返回的是一个range对象，需要用list()转换成列表


# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')



# rang() 
# len()
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
print(len(a))
for i in range(len(a)):
    print(i,a[i])


# pass

  #题目  
i = sum = 0

while i <= 4:
    print('i---',i)
    sum += i  #sum = sum + i
    print('sum==',sum)
    i = i+1

print(sum)
   