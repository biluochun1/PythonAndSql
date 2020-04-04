# one_list = [1, 2, 3, 6, 5, 5, 6]
# print("one list", one_list)
# print("one_list[0]", one_list[0])
# one_list.remove(6)
# print("one list remove after", one_list)

import numpy
import pandas
import requests

# l1 = [[1,2,3],[4,5,6]]
# l2 = [[2,2,2],[2,2,2]]
# m1 = numpy.asarray(l1)
# m2 = numpy.asarray(l2)
# print(l1)
# print(m1.shape)
#
# print(m1.reshape(1,6))
#


if __name__ == '__main__': # 程序的入口
    s = " zyj and wzj "
    print("s:",s)
    lenth = len(s) #得到s的长度
    print("lenth:",lenth)
    print("s first letter[0]:",s[0]) # 得到s的第一个字母
    s2 = s.strip() #处理字符串的前后（只处理前后）的空格
    print(s2)