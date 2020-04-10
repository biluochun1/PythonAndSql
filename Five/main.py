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
    l = []
    for i in range(100):
        l.append(0)
    print(l)
    l = [i / (i + 1) for i in range(20)]
    print(l)
    l = [[i * j for i in range(4)] for j in range(3)]
    print(l)
    print(l[1][3])
    l = [i / (i + 1) for i in range(20) if i > 5]
    print(l)
