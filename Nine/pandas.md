# 2020-04-19
## Pandas
```python
import pandas #导入包
```

## Pandas的主要数据类型

- DataFrame（二维表）
- Series（一维序列）
- Index（行索引，行级元数据）

```python
import pandas as pd
import numpy as np
```
## Series 长枪 （一维列表）
```python
#用值构建一个Series：由默认index和values组成
series1 = pd.Series(np.random.randn(10))
print(series1)
'''
0    0.855957
1    0.270582
2    0.652333
3   -0.828324
4    1.810720
5   -1.993580
6    0.002996
7    1.028447
8   -0.412869
9   -0.857103
dtype: float64'''
print(series1[0:6]) #series的切片
'''
0    0.855957
1    0.270582
2    0.652333
3   -0.828324
4    1.810720
5   -1.993580
dtype: float64'''
#对Series进行过滤
print(series1>0)  
'''
0     True
1     True
2     True
3    False
4     True
5    False
'''
print(series1[series1 > 0])
'''0    0.978434
1    0.084593
3    2.295333
5    1.251542
6    0.614743
7    0.679780
9    0.431317
dtype: float64
'''
print(series1 * 2)
print(series1 + 1)
'''
0   -1.004706
1   -0.453379
2   -0.159363
3    0.389423
dtype: float64
0    0.497647
1    0.773311
2    0.920318
3    1.194711
dtype: float64'''

# 通过创建一个自定义函数来处理series
f_np = np.frompyfunc(lambda x: x + 1, 1, 1)
print(f_np(series1))


#通过index属性为Series指定索引名称
series2 = pd.Series(series1.values, index=['norm_' + str(i) for i in range(len(series1.values))])
print(series2)
'''
0   -0.895256
1   -0.521580
2   -2.024371
3   -0.010896
dtype: float64
norm_0   -0.895256
norm_1   -0.521580
norm_2   -2.024371
norm_3   -0.010896
dtype: float64'''
print(series2[["norm_0"]])
print("norm_4" in series2)
'''
norm_0   -0.355004
dtype: float64
False
'''
# 通过字典来定义
Series3_Dict = {"Japan": "Tokyo", "S.Korea": "Seoul", "China": "Beijing"}

Series3_pdSeries = pd.Series(Series3_Dict)

print(Series3_pdSeries)
```

## DataFrame:pandas的战锤（数据表，二维数组）

```python
# 从一个列表来得到dataframe
dataNumPy = np.asarray([['Japan', 'Tokyo', 4000], ['S.Korea', 'Seoul', 1300], ['China', 'Beijing', 9100]])

df1 = pd.DataFrame(dataNumPy, columns=['nation', 'capital', 'GDP'])

print(df1)
#  从一个字典来得到dataframe
dataDict = {'nation': ['Japan', 'S.Korea', 'China'], 'capital': ['Tokyo', 'Seoul', 'Beijing'],
            'GDP': [4900, 1300, 9100]}

df2 = pd.DataFrame(dataDict)

print(df2)
# 从另外一个dataframe获取
df3 = pd.DataFrame(df2, columns=["GDP"])

# 获取行
# print(type(df2[1:2])) #<class 'pandas.core.frame.DataFrame'>
# loc方式获取一行 （感觉用的不多）
# print(type(df2.loc[1])) #<class 'pandas.core.series.Series'>

# 切片 iloc[row,col]
print(df2.iloc[1, 1])  # 1行1列元素
print(df2.iloc[1:3, 1:3])  # 1,2行的1，2列
print(df2.iloc[1:3, :])  # 空:空 默认赋值为 0:len

print(df2.iloc[1:3, ::2])

# 过滤数据
print(df2[(df2['GDP'] < 2000) | (df2.GDP > 8000)]) # dataframe[condition] -> condition = subcondition & subcondition
print(df2[df2.GDP < 5000])

# 生成日期
data = pd.date_range("01-01-2020", periods=5).format(formatter=lambda x: x.strftime('%d-%m-%Y'))

print(data)
```



## 切片操作
常用的切片表达式
start:end  -> [start,end)
start: -> [start,len)
:end -> [0,end)
: -> [0,len)
对于一个完整的切片的表达式
start:end:step 默认 步长1 如果步长是-1的话，往左边跳，就是反转
::-1 -> 空:空:-1 -> len:0:-1
```python
l1 = [1,2,3,4]
print(l1[::-1])
'''
[4, 3, 2, 1]
'''
```
