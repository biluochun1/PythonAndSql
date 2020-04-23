import pandas as pd
import numpy as np

# 用值构建一个Series：由默认index和values组成
series1 = pd.Series(np.random.randn(4))
print(series1)
# print(series1[0:6])  # series的切片
# 对Series进行过滤
# print(series1 > 0)
# print(series1[series1 > 0])
# print(series1 * 2)
# print(series1 + 1)
# f_np = np.frompyfunc(lambda x: x + 1, 1, 1)
# print(f_np(series1))

series2 = pd.Series(series1.values, index=['norm_' + str(i) for i in range(len(series1.values))])
# print(series2)
# print(series2.index)
print(series2[["norm_0"]])
print("norm_4" in series2)

Series3_Dict = {"Japan": "Tokyo", "S.Korea": "Seoul", "China": "Beijing"}

Series3_pdSeries = pd.Series(Series3_Dict)

print(Series3_pdSeries)

# 从一个列表来得到dataframe
dataNumPy = np.asarray([['Japan', 'Tokyo', 4000], ['S.Korea', 'Seoul', 1300], ['China', 'Beijing', 9100]])

df1 = pd.DataFrame(dataNumPy, columns=['nation', 'capital', 'GDP'])

print(df1)
#  从一个字典来得到dataframe
dataDict = {'nation': ['Japan', 'S.Korea', 'China'], 'capital': ['Paris', 'Seoul', 'Beijing'],
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

print(df2[(df2['GDP'] < 2000) | (df2.GDP > 8000)])  # dataframe[condition] -> condition = subcondition & subcondition
print(df2[df2.GDP < 5000])

data = pd.date_range("01-01-2020", periods=5).format(formatter=lambda x: x.strftime('%d-%m-%Y'))

print(data)

df2["pop"] = [100, 230, 900]
df2.index = [4, 5, 6]

print(df2)
print(df1)

print(pd.merge(df2, df1, on="nation"))


# python 所有的东西 都是对象（实例） object  类型叫 class  class创造object过程 实例化
