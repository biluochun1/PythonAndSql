# one_list = [1, 2, 3, 6, 5, 5, 6]
# print("one list", one_list)
# print("one_list[0]", one_list[0])
# one_list.remove(6)
# print("one list remove after", one_list)

import pandas
import requests
import matplotlib.pyplot as plt
import numpy as np


# l1 = [[1,2,3],[4,5,6]]
# l2 = [[2,2,2],[2,2,2]]
# m1 = numpy.asarray(l1)
# m2 = numpy.asarray(l2)
# print(l1)
# print(m1.shape)
#
# print(m1.reshape(1,6))
#
def show_a_photo():
    t = np.arange(0.0, 5.0, 0.1)
    s = np.exp(-t) + np.sin(2 * np.pi * t) + 1
    nse = np.random.normal(0.0, 0.3, t.shape) * s

    fig, (vax, hax) = plt.subplots(1, 2, figsize=(12, 6))

    vax.plot(t, s + nse, '^')
    vax.vlines(t, [0], s)
    # By using ``transform=vax.get_xaxis_transform()`` the y coordinates are scaled
    # such that 0 maps to the bottom of the axes and 1 to the top.
    vax.vlines([1, 2], 0, 1, transform=vax.get_xaxis_transform(), colors='r')
    vax.set_xlabel('time (s)')
    vax.set_title('Vertical lines demo')

    hax.plot(s + nse, t, '^')
    hax.hlines(t, [0], s, lw=2)
    hax.set_xlabel('time (s)')
    hax.set_title('Horizontal lines demo')

    plt.show()


if __name__ == '__main__':  # 程序的入口
    s = " zyj and wzj "
    print("s:", s)
    lenth = len(s)  # 得到s的长度
    print("lenth:", lenth)
    print("s first letter[0]:", s[0])  # 得到s的第一个字母
    s2 = s.strip()  # 处理字符串的前后（只处理前后）的空格
    print(s2)
    print("%d,%f,%s" % (10, 1.0, "love u"))
    print("s is {}".format(s))
    print(type([1,2,3,4].count(1)))
    l = [1,2,3,4]