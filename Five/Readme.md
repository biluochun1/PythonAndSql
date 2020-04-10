# 2020-04-10

## Review

## 变量

```python
i = 0 #赋值过程，把0赋值给i
i = [1,2,3] #i被赋值成了一个list

内存1（0）			内存2（[1,2,3]）

				i (引用)
```

### 基本数据类型

```python
int float bool str(暂且理解)
# 类型的转换
a = int(3.5)
a = float(3)
a = bool(0)
a = str(1) # "1" != 1  前面是个str 后面是个int
```

```python
a = "i love u"
a.strip() #处理str前后空白字符 如空格、换行、制表符等等
a.split(" ") #把字符串根据传入的分割符号进行切分，返回切分后的str list
#还有一些判断字符串大小写的方法 ……

len(s) # len 函数可以返回字符串的长度
for char in s:
  #可以通过for循环对字符串遍历，char是每个字符
s[i] #返回第i个字符
for i in range(len(s)):
  s[i] #可以通过for循环对字符串遍历，得到每个字符，和上面方法等价

  
#切片操作
a[0:5] # a[start:end] 返回从a的第start位置到end位置的子序列
```

### 数据结构（集合）

#### List

```python
l = [] #创建一个空list
l.append(1)
l.append("zyj")
# 访问list
# 索引访问
l[0] # 返回第一个元素
# 遍历访问
for e in l:
  pass
for i in range(len(l)):
  pass #l[i]
```

#### Dict

```python
d = {}
d["wzj"] = "zyj"
# key访问
print(d["wzj"])   
print(d.get("wzj"))
# 遍历方式
for key in d.keys():
  pass
for val in d.values():
  pass
for key,val in  d.items():
  pass
```

## 控制结构

```python
if condition:
  pass

if condition:
  pass
else:
  pass

for i in range(start,end):
	pass
```

## 函数

```python
def funtion_name(param1,param2):
  return res1,res2

z,w = func(x,y)
```

- 参数的作用范围只在函数内部
- 函数内部的局部变量作用范围也只在函数内部
- 函数可以有多个返回值
- def 只是定义这个函数（包括内部实现），调用函数还需要显式调用

## 文件操作

```python
def readfile(path): #如果这个path不存在，那么会 错误 no such file or directory
  with open(path,"r") as f:
    for line in f.readlines():
      pass #操作每一行

def wirtefile(path): #如果这个path不存在，那么会新建
  with open(path, "w") as fw:
    fw.write("zyj"+" love "+"wzj"+"\n") # zyj love wzj
    for i in range(3000):
      fw.write("zyj"+" love "+"wzj"+"\n")
```



