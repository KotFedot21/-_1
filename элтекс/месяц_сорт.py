from redminelib import Redmine
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from datetime import date
from datetime import timedelta
from asyncio import tasks
plt.rcdefaults()
import numpy as np
import calendar
from multiprocessing import Pool
date  = date.today()

URL='http://red.eltex.loc'
KEY='08c017a3b50e09357a72e4448cc1aa6f09271755'
redmine = Redmine(URL, key=KEY)

userlist = [
        69,
        1027,
        1125
    ]
statuslistс = [
    5
]

statuslist = [

        13,
        3,
        9
    ]
speed=[]
current_date = date.today()
tasks=[]
matrix1=[]



def collecting_data_for_the_month(redmine, userlist,man):
    tasks=[]
    for userid in userlist:
        matrix1=[]
        for ma in man:
            th=[]
            ms = redmine.user.get(userid, include='memberships')
            prjc = 0
            for msp in ms.memberships:
                try:
                    issues = redmine.issue.filter(project_id=msp.project.id, status_id=5,updated_on=ma, cf_2=userid)
                    for issue in issues:
    
                        print(redmine.user.get(userid).firstname, redmine.user.get(userid).lastname)
                        print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                        print('\t\tНомер:', issue.id, 'Статус:', issue.status.name, 'Версия:', issue.fixed_version.name, 'Тема:', issue.subject)
                        th.append(issue.id)
                        
                    th1 = list(set(th))
                    
                except:
                    print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                    print("Доступ к проекту запрещен")

                prjc=len(th1)
                
                

            matrix1.append(prjc)
            print(matrix1)
        tasks.append(matrix1)
        print(tasks)

    return tasks

       
def statistics_for_the_month():    
    man=[]
    d=[]


    date_1= date.replace(day=calendar.monthrange(date.year, date.month)[0])
    date_2= date.replace(day=calendar.monthrange(date.year, date.month)[1])
    while date_1<=date:
        cur_date1 = str(date_1)
        d.append(date_1.day)
        man.append(cur_date1)
        date_1 = date_1 + timedelta(1)
    
    print(man)
    print(d)
    
    h=collecting_data_for_the_month(redmine,userlist,man)
    
    lin=['r','b','k']
    for hi, us, li in zip(h, userlist, lin):
        plt.plot(d, hi, li, label=redmine.user.get(us).firstname)
    #plt.figure(figsize=(10, 10))#в дюймах
    plt.xlim([0,31])
    plt.ylim([0, 5])
    plt.legend(fontsize=14)
    plt.show()
    
statistics_for_the_month()
