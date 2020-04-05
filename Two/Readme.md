# 2020-04-05



## 数据结构
### Dict Key-Value集合，常常通过Key来迅速拿到Val，或者包含了一层映射关系
```python
d = {} #花括号来new一个字典
d = {
    "name":"zyj",
    "age":18,
}
# {'name': 'zyj', 'age': 18}
print(d)
print(d.get("name")) # dict 第一个访问key的方法
print(d["age"])
d["salary"] = "30w" # 放置一个元素
print(d)
```

## 控制流程
### if...else...
```python
if score > 21 :
    print("lose")
else:
    print("win")
```
### for...
```python
card_score_dict = {
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
} # 存储牌面和对应的分数
hand_cards = ["2","3","4"] # list
for card in hand_cards:
    print(card_score_dict.get(card))

for i in range(len(hand_cards)):
    print(hand_cards[i])
```
### while...
```python
while score <= 50:
    score += 20
    print(score)
```