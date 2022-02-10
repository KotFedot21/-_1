import matplotlib.pyplot as plt
userID = [
    69,
    12,
    123
]
tasks = [
    4,
    5,
    7

]

tasks1 = [
    1,
    3,
    10

]

tasks2 = [
    0,
    7,
    20

]

dat = [
    7,
    14,
    21
]

plt.plot(dat, tasks, '--r', label=userID[0])
plt.plot(dat, tasks1, ':b', label=userID[1])
plt.plot(dat, tasks2, 'k', label=userID[2])
plt.legend(fontsize=14)

plt.show()
