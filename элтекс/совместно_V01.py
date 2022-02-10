import matplotlib.pyplot as plt
from datetime import date
from datetime import timedelta
import calendar
## если хотим определить за последнюю неделю
##1
d = []
def information_for_the_week(d):

    current_date = date.today()## дата сегодня
    print(current_date)
    print(current_date.weekday())##номер дня, 0-понедельник
    num = current_date.weekday()
    monday_date = current_date - timedelta(days=num)##получаем дату понедельника
    print(monday_date)
    i = 0
    while i <= num :
        d.append(monday_date.day)
        monday_date = monday_date + timedelta(1)
        i += 1

    print(d)

userID = [ 69, 12, 123]
tasks = [4,5,7,1]
tasks1 = [1,3,1,5]
tasks2 = [0,7,20,3]


information_for_the_week(d)
plt.plot(d, tasks, '--r', label=userID[0])
plt.plot(d, tasks1, ':b', label=userID[1])
plt.plot(d, tasks2, 'k', label=userID[2])

""""
# Be sure to only pick integer tick locations.
for axis in [ax.xaxis, ax.yaxis]:
    axis.set_major_locator(ticker.MaxNLocator(integer=True))
"""
plt.legend(fontsize=14)

plt.show()
