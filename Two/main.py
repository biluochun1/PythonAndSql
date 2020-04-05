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


if __name__ == '__main__':
    d = ["Red Tao", "Black Tao", "Square", "MeiHua"]
    v = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
    total_res = get_all_combination(d, v)
    print(total_res)

