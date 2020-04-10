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
def max_list_two(l:list):
    return max(l)

if __name__ == '__main__':
    print(max_list([2,3,9,4,5,6,7]))
    print(max_list_two([1,2,3,4,5,6]))

    d = {
        "wzj":"zyj"
    }
    print(d.get("wzj"))
    print(d.get(0))
