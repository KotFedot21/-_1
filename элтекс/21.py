import PySimpleGUI as sg
import matplotlib.pyplot as plt
from datetime import date
from datetime import timedelta
plt.rcdefaults()
import numpy as np


## переменные
userID = [69, 12, 123]
d = []


def information_for_the_week(d,userID):
    del d[:]   ### для повторного использования
    current_date = date.today()## дата сегодня
    print(current_date)
    print(current_date.weekday())##номер дня, 0-понедельник
    num = current_date.weekday()
    monday_date = current_date - timedelta(days=num)##получаем дату понедельника
    print(monday_date)
    i = 0
    j=0
    c=0
    current_date2=[]
    while j <= 5: # создает список из дат недели

        current_date1 = str(current_date)
        current_date2.append(current_date1)
        current_date = current_date + timedelta(days=1)

        j+=1

    print (current_date2)
    while i <= 5 : # создает список из дней недели
        d.append(monday_date.day)
        monday_date = monday_date + timedelta(1)
        i += 1

    print(d)

    tasks = [4]
    tasks1 = [1]
    tasks2 = [9]

    task =[tasks,tasks1,tasks2]

    dlina=(len(d))#проверка на кол-во выполненых задач
    for tasks in task:
        while c <= dlina : # создает список из дней недели
            tasks.append(0)
            c += 1

    print(tasks)


"""
    plt.plot(d, tasks, '--r', label=userID[0])
    plt.plot(d, tasks1, ':b', label=userID[1])
    plt.plot(d, tasks2, 'k', label=userID[2])



    plt.legend(fontsize=14)

    plt.show()"""

information_for_the_week(d,userID)
