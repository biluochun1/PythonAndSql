# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

def output_casenumber(sentence: str):
    u = []
    l = []
    for char in sentence:
        if char.isupper():
            u.append(char)
        if char.islower():
            l.append(char)

    return u, l, len(u), len(l)


# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# # Suppose the following input is supplied to the program:
# # 1,2,3,4,5,6,7,8,9


# 3 输入两个列表，返回乘积 （实现一个矩阵乘法）
def matrix_mul(l1: list, l2: list):
    l1_row = len(l1)
    l1_col = len(l1[0])
    l2_row = len(l2)
    l2_col = len(l2[0])
    res = [[0 for i in range(l1_row)] for j in range(l2_col)]

    for i in range(l1_row):
        for j in range(l2_col):
            for k in range(l1_col):
                res[i][j] += l1[i][k] * l2[k][j]
    return res


# l1 = [[1, 2, 3],
#       [1, 4, 3]] #l1[1][k] k = 0,1,2
# l2 = [[1, 2],
#       [1, 1],
#       [1, 1]]  #[2,1,1] l2[k][1] k = 0,1,2
# res = [[0,0],
#        [0,0]]
# # res 第 i，j 位置的元素 是等于 l1 的第 i 行 和 l2 的第 j列 进行 先乘法再求和
# print(matrix_mul(l1, l2))

# 1 1 2 3 5 8 13 21 34
# f(n)  = f(n-1)+f(n-2)
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


# f5
# f4      f3
# f3   f2
# f2 f1

# 4 With a given list （ex.[1,2,3,4,5,6]）, write a program to print
# the first half values in one line and the last half values in one line.
def solution4(s: str):
    pass


# Write a program to compute 1/2+2/3+3/4+...+n/n+1
def cal_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i / (i + 1)
    return sum
    # return [i / (i + 1) for i in range(1, n + 1)]



def replace(path, symbol):
    with open(path, "r") as f:
        for line in f.readlines():
            s = line.strip().split(symbol)
            s = s[0] + " love " + s[1]
            print(s)


if __name__ == '__main__':
    replace("/Users/weizijian/Downloads/PythonTeaching/Four/test.txt", ",")
