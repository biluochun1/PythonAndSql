# 2020-04-16

## 面向对象
## 类
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name + " walk")

    def talk(self):
        print(self.name + " talk")


p1 = Person(name="zyj", age=18)
p1.walk()
p1.talk()
p2 = Person(name="wzj", age=18)
p2.walk()
p2.talk()

```
一个类一般有两部分组成，属性和方法（行为）

## pandas
```python
import pandas #导入包
```
```python
# 从一个json的文件里面读取内容到一个pandas.dataframe结构里面
def read_json_to_df(path="/Users/weizijian/Downloads/PythonTeaching/Seven/score.txt"):
    with open(path, "r") as f:
        s = json.loads(f.read())
    df = json_normalize(s)
    return df
```

Pandas的主要数据类型

- DataFrame（二维表）
- Series（一维序列）
- Index（行索引，行级元数据）
