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

userlist = [
        #69,
        1027,
        #1125
    ]

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
startlist ='2022-02-14'

finilist ='2022-02-18'

gud = '><' + startlist + "|" + finilist


def GetAllIssuesInAllProjects(redmine, userlist, statuslist):
    
    for userid in userlist:
        try:
            ms = redmine.user.get(userid, include='memberships')
            prjc = 0
            for msp in ms.memberships:
                
                for statusid in statuslist:
                    issues = redmine.issue.filter(project_id=msp.project.id, status_id=statusid,updated_on=gud, cf_2=userid)
                    for issue in issues:
                        prjc += 1
                        print(redmine.user.get(userid).firstname, redmine.user.get(userid).lastname)
                        print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                        print('\t\tНомер:', issue.id, 'Статус:', issue.status.name, 'Версия:', issue.fixed_version.name, 'Тема:', issue.subject)
            print('Количество проектов:', prjc)
        except:
            continue
GetAllIssuesInAllProjects(redmine, userlist, statuslist)
