from redminelib import Redmine
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from datetime import date
from datetime import timedelta
plt.rcdefaults()
import numpy as np
URL='http://red.eltex.loc'
KEY='08c017a3b50e09357a72e4448cc1aa6f09271755'
redmine = Redmine(URL, key=KEY)
redmine = Redmine(URL, key=KEY)

userID = [69, 12, 123]

userlist = [
        69,
        #1027,
        #1125
    ]

userid=69

'''69 - Алексей Глебко
1027 - Игорь Быков
1125 - Алена Новобранова'''

'''Статусы тикетов
New - 1
Re-opened - 8
In Progress - 2
Feedback - 13
Resolved - 3
Testing - 9
Closed - 5
Pending - 4
Wait Release - 10
'''
statuslist = [
    5
]

def information_for_the_week():
    d=[]   ### для повторного использования
    current_date = date.today()## дата сегодня
    print(current_date)
    current_d = current_date.weekday()
    print(current_date.weekday())##номер дня, 0-понедельник
    num = current_date.weekday()
    monday_date = current_date - timedelta(days=num)##получаем дату понедельника
    print(monday_date)
    i = 0
    j=0
    c=0
    current_date2=[]
    while j <= 5: # создает список из дат недели

        current_date1 = str(monday_date)
        current_date2.append(current_date1)
        monday_date = monday_date + timedelta(days=1)

        j+=1
    monday_date = current_date - timedelta(days=num)  ##получаем дату понедельника
    print (current_date2)
    return current_date2

def information_for_the_week2():
    d=[]   ### для повторного использования
    current_date = date.today()## дата сегодня
    print(current_date)
    current_d = current_date.weekday()
    print(current_date.weekday())##номер дня, 0-понедельник
    num = current_date.weekday()
    monday_date = current_date - timedelta(days=num)##получаем дату понедельника
    print(monday_date)
    i = 0
    j=0
    c=0
    current_date2=[]
    while i <= 5 : # создает список из дней недели для графика
        d.append(monday_date.day)
        monday_date = monday_date + timedelta(1)
        i += 1
        

    print(d)
    return d

def GetAllIssuesInAllProjects(redmine, userlist,statuslist):
    
    matrix1=[]
    for userid in userlist:
        try:
            th=0
            for current_date2id in information_for_the_week() :
                
                ms = redmine.user.get(userid, include='memberships')
                prjc = 0
                
                for msp in ms.memberships:
                    
                    for statusid in statuslist:
                        issues = redmine.issue.filter(project_id=msp.project.id, status_id=statusid,updated_on=current_date2id, cf_2=userid)
                        for issue in issues:
                            
                            
                            if th!=issue.id:
                                prjc += 1   
                                print(redmine.user.get(userid).firstname, redmine.user.get(userid).lastname)
                                print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                                print('\t\tНомер:', issue.id, 'Статус:', issue.status.name, 'Версия:', issue.fixed_version.name, 'Тема:', issue.subject)
                                th=issue.id
                print('Количество проектов:', prjc)
                            
                
                matrix1.append(prjc)
                print(matrix1)
        
        except:
            continue
    return matrix1

us=str(redmine.user.get(userid).firstname)
s=information_for_the_week2()
h=GetAllIssuesInAllProjects(redmine, userlist, statuslist)
print (s)
print (h)
plt.plot(s, h, '--r',label=us)
plt.legend(fontsize=14)
plt.show()

