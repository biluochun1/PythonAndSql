# 2020-04-04


## 语言的通用结构
- 输入输出
- 变量类型
- 控制结构
- 数据结构
- 函数
- 面向对象 Advanced
- 包管理 Advanced
- 语言特性 Advanced


## 环境配置
- Anaconda  conda 环境（目的是为了简化环境配置，拆箱即用） 一堆科学计算包集成，同时配置了包管理。同时conda自带了python3。
```shell script
conda list //显示已经安装的包
conda install pkgname //安装包 使用conda安装
pip install pkgname //安装包 使用pip安装
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pkgname // 指定国内清华源，加速下载
```
- IDE （Pycharm）开发者工具，一个编译环境，用来写代码，执行代码。


## 常用shell
```shell script
cd Downloads //切换目录
ls //查看目录
```


## 运行第一个程序
```shell script
//1.命令行运行
python main.py 

//2.ide运行 绿色箭头
```


## 输出
```shell script
print("")
```


## 注释
```python
# code
# ide 注释快捷键 command + /
```


## 变量和运算
```shell script
//C style
//int a  = 10;
a = 10;
//+ - * / 四个运算
//整形（整数），浮点数（0.5）
//字符串 支持 + （两个 字符串相加） * num
s = " zyj and wzj "
print("s:",s)
lenth = len(s) #得到s的长度
print("lenth:",lenth)
print("s first letter[0]:",s[0]) # 得到s的第一个字母
s2 = s.strip() #处理字符串的前后（只处理前后）的空格
print(s2)
//bool True False
//查看类型
b = True
type(b)
//类型转换
c = int(b)
//if判断条件里面
print(s==s2)
False
print(s!=s2)
True
//并或
and or
print(0 and 0)
0
print(0 or 1)
1
print(0 or 0)
0
print(1 and 0)
0
```


## 数据结构
### list 一个有序的元素集合
```python 
# list 每个元素 有 索引 和 值
l1 = [1,2,3]
l2 = []

l2.append(2) #添加元素
l2.append("t") #append 接受的参数是element 元素 
l3 = l1 + l2 # 两个列表直接相加 然后赋值l3
l1.extend(l2) #extend 接受的参数是 list ，对l1后累加列表

l1[0]# 访问元素

# list len长度
len(l1)
//计算元素值为1的元素数量
l1.count(1)
//弹出最后一个元素
l1.pop()
//反转list
l1.reverse()    #反转
reversed()
```
