# 2020-04-08

https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt


之前我们学了变量、控制结构（if-else、for、while）、List、Dict

## 遍历字典
```python
    CARD_SCORE = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
    }  # 存储牌面和对应的分数
    # key
    for key in CARD_SCORE:
        print(key)
    for key in CARD_SCORE.keys():
        print(key)
    # value
    for value in CARD_SCORE.values():
        print(value)
    # key value
    for key, value in CARD_SCORE.items():
        print(key, value)
```
## 切片
```python
    s = "zyj and wzj"
    l = [1,2,3,4,5,6]
    print(s[0:5])
    print(l[2:4])
```
## break、continue
```python
    for i in range(100):
        if i == 30 :
            break
        print(i)
    for i in range(5):
        if i == 1 :
            continue
        print(i)
```

## 文件操作
```python
    with open("/Three/test.txt", "r") as f:
        
        # f.readline() #读取一行
        # 一行一行读取 常用
        for line in f.readlines():
            s = line.strip().split(".")
            print(s)
        # 读取整个文件内容
        # s = f.read()
        # s = s.strip().split("\n")
        # print(s)
        # for line in s:
        #     s = line.strip().split(",")
        #     print(s)
```