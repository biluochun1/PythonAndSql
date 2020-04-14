# 2020-04-14

## Tuple
```python
t = (1,2,3)
# list [] 有序的可变容器 dict {} key-value tuple () 有序的不可变的容器

# 遍历tuple、判断元素在不在集合里面 和 list 方法一致
for e in t:
    print(e)
a = 3
if a in t:
    print("exist")

# 特性 不可变
t[0] = 7 #TypeError: 'tuple' object does not support item assignment
```

## Set
```python
s = set() # 集合 比较常用的特性 就是 元素不重复 ； 可以求交集 并集 差集
s.add(1)
s.add(2)
s.add(3)
print(s)
```

## str join
```python
l = ["q","w","e","r"]

print("!".join(l))
# 把list每个元素用!链接
```


## 爬虫
```python
import requests
requests.get() #它是一种最常用的请求，通常用来返回一个页面（html页面、图片、视频等等）
requests.post() #它是一种第二常用的请求，通常用来提交表单（通常是账号密码）数据，收到服务端返回的json数据
requests.delete() #通常对应删除数据的请求
requests.put() #通常对应修改数据的请求
```

```python
import requests  # 一个用来请求的包
from bs4 import BeautifulSoup  # 用来解析html的一把枪

url = " https://www.pwccn.com/zh/careers/students/internship.html"  # 请求链接

resp = requests.get(url=url)  # 发起一个请求，收到回复

html_doc = resp.content.decode("utf-8")  # 将 resp 以 utf-8 的编码格式做成字符串给  html_doc

soup = BeautifulSoup(html_doc, 'html.parser')  # 使用html.parser来 解析 html
```