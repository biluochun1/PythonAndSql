# date = ["1.24", "2.1", "2.8", "2.15", "2.22", "2.29", "3.7", "3.14", "3.21", "3.28", "4.4", "4.11", "4.18"]
# new_case = []
# new_death = []
# cases = []
# cured = []
# deaths = []
# with open("date.txt", "r") as f:
#     for line in f.readlines():
#         s = line.strip().split("\t")
#         new_case.append(int(s[0]))
#         new_death.append(int(s[2]))
#         cases.append(int(s[4]))
#         cured.append(int(s[6]))
#         deaths.append(int(s[8]))
#
# print(date)
# print(new_case)
# print(new_death)
# print(cases)
# print(cured)
# print(deaths)
#
# ['1.24', '2.1', '2.8', '2.15', '2.22', '2.29', '3.7', '3.14', '3.21', '3.28', '4.4', '4.11', '4.18']
# [444, 2590, 2656, 2009, 648, 573, 44, 20, 46, 45, 30, 99, 16]
# [16, 45, 89, 142, 97, 35, 27, 10, 6, 5, 3, 0, 0]
# [1287, 14380, 33738, 57416, 51606, 35329, 20533, 10734, 5549, 2691, 1376, 1138, 1041]
# [38, 328, 2659, 9419, 22888, 41625, 57065, 66911, 72244, 75448, 76964, 77575, 77062]
# [41, 304, 811, 1665, 2442, 2870, 3079, 3199, 3261, 3300, 3329, 3339, 4632]
#
# data = []
# for y in range(3):
#     for x in range(len(date)):
#         if y == 0:
#             data.append([y, x, cases[x]])
#         if y == 1:
#             data.append([y, x, deaths[x]])
#         if y == 2:
#             data.append([y, x, cured[x]])
#

date = []
confirm = []
leiji = []
death = []
with open("new_data.txt", "r") as f:
    for line in f.readlines():
        s = line.strip().split("\t")
        print(s)
        date.append(s[0])
        confirm.append(int(s[1]))
        leiji.append(int(s[3]))
        death.append(int(s[5]))
print(date)
print(confirm)
print(leiji)
print(death)

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(20, 350)
l1 = plt.plot(date, confirm, marker = "o", label='The number of confirmed cases that day')
l2 = plt.plot(date, leiji, marker = "+", label='The cumulative number of cured cases', ls=":")
l3 = plt.plot(date, death, marker = "*", label='The cumulative number of deaths', lw=3)
# plt.plot(date, confirm, 'ro-', date, leiji, 'g+-', date, death, 'b^-')
# plt.title('The Lasers in Three Conditions')
plt.xlabel('date')
plt.ylabel('number')
plt.legend()
plt.show()
