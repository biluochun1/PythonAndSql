# 2020-04-15

## zip()
```python
a = [1, 2, 3]
b = ["1", "2", "3"]
c = zip(a, b) # zip两个列表
for e in zip(a, b):
    print(e)

print(list(c))
```

## json
json是一种协议格式。
```python
# 序列化
d = {
    "key1": 1,
    "key2": 2,
}
l = [1,2,3]
# dumps 可以把python的一些容器变成json的字符串
s = json.dumps(l)
print(type(s))

# 反序列化
x =  '{ "name":"John", "age":30, "city":"New York"}'
l = "[1,2,3]"
# loads 方法把一个字符串转换成了一个容器类型
y = json.loads(x)

print(type(y))
print(y["name"])

```