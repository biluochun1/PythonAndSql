# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0],
# [0, 1, 2, 3, 4],
# [0, 2, 4, 6, 8]]


def generate_matrix(x, y):
    # res = [[0 for j in range(y)] for i in range(x)]

    # l = [0 for i in range(x)]
    res = []
    for i in range(x):
        res.append([])
        for j in range(y):
            res[i].append(0)
    print(res)


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


def iterator_dict():
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


# def count_list(l):
#     d = {}
#     for e in l:
#         # d[str(e)] = l.count(e)
#         d.update({str(e):l.count(e)})
#
#     return d
#
#
#
# if __name__ == '__main__':
#     # generate_matrix(5, 5)
#     # iterator_dict()
#     l = [1,2,2,2,2,2,2,4,5,5,6]


# print(count_list(l))

def count_list(l):
    d = {}
    for i in l:
        d.update({str(i): l.count(i)})
    return d


# def count_file_line(path):
#     with open(path, "r") as f:
#         return len(f.readlines())
#
#

if __name__ == '__main__':
    path = "///////main.py"
    # print(count_file_line(path))
    print(path.find("One"))


