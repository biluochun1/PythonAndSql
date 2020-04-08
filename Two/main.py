import simplegui

def get_total_card():
    d = ["Red Tao", "Black Tao", "Square", "MeiHua"]
    v = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

    total = [i + " " + j for j in v for i in d]
    print(total)


def add(x, y):
    print(x + y)
    get_total_card()
    return x + y


def minus(x, y):
    print(x - y)


def get_all_combination(l1, l2):
    total_res = []
    for i in l1:
        for j in l2:
            total_res.append(i + " " + j)
    return total_res


def cal_height(h, count):
    d = 0
    l = []
    for i in range(0, count):
        if i == 0:
            d += h
        else:
            d += 2 * h
        h = h / 2
        l.append((d, h))
    return d, l


if __name__ == '__main__':
    print(cal_height(100, 10))
    print(cal_height(500, 20))
