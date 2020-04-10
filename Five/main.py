# average of list
def average_list(l: list):
    return sum(l) / len(l)


# max list
# method one
def max_list(l: list):
    max = 0
    for e in l:
        if max < e:
            max = e
        else:
            pass
    return max


# method two
def max_list_two(l: list):
    return max(l)


def wirte_file(path):  # 如果这个path不存在，那么会新建
    with open(path, "w") as fw:
        # fw.write(str([1, 2, 3]))
        fw.write("zyj" + " love " + "wzj" + "\n")  # zyj love wzj
        for i in range(3000):
            fw.write("zyj" + " love " + "wzj" + "\n")


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    d = {
        "wzj": 1,
        "zyj": 2
    }
    a = 3
    b = "wzj"
    c = "w"
    if a in l:
        print(a, "exist")
    if b in d:
        print(b, "exist")
    if c not in d:
        print(c, "not exist")
