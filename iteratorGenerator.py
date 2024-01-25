# 迭代器有两个基本的方法：iter() 和 next()
line = '======================'
list = [1,2,3,4]
it = iter(list)
print(next(it))


print(line)
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
 
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)



# yield

print(line)
def countdown(n):
    while n > 0:
        yield n
        n -= 1
generator = countdown(5)
# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1