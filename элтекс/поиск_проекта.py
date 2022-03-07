from redminelib import Redmine
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from date
from datetime import timedelta

plt.rcdefaults()
import numpy as np

URL = 'http://red.eltex.loc'
KEY = '08c017a3b50e09357a72e4448cc1aa6f09271755'
redmine = Redmine(URL, key=KEY)
redmine = Redmine(URL, key=KEY)

userlist = [
    # 69,
    1027,
    # 1125
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

    13,
    3,
    9
]


def GetAllIssuesInAllProjects(redmine,userid, projec_name, statuslist):

    try:
        ms = redmine.user.get(userid, include='memberships')
        prjc = 0
        for msp in ms.memberships:
            prjc += 1
            for statusid in statuslist:
                issues = redmine.issue.filter(project_id=msp.project.id,projec_name=msp.project.name, status_id=statusid, cf_2=userid)
                for issue in issues:
                    print(redmine.user.get(userid).firstname, redmine.user.get(userid).lastname)
                    print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                    print('\t\tНомер:', issue.id, 'Статус:', issue.status.name, 'Версия:', issue.fixed_version.name,
                          'Тема:', issue.subject)
        print('Количество проектов:', prjc)
    except:
        continue




sg.theme('Topanga')      # Add some color to the window

# Very basic window.  Return values using auto numbered keys
choices = ("Алексей","Игорь","Алена")#передаем id сотрудников из редмайна

layout = [  [sg.Text('Выберите сотрудника')],[sg.Listbox(choices, size=(40, len(choices)), key='-Name-')],
            [sg.Text('Название проекта', size=(15, 1)), sg.InputText()],
            [sg.Button('Ok')]  ]

window = sg.Window('Pick a color', layout)

while True:                  # the event loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Ok':
        if values['-Name-'][0]=="Алексей":
            userid = 69
            projec_name=values[0]
            GetAllIssuesInAllProjects(redmine, userid, projec_name, statuslist)
            break
        if values['-Name-'][0] == "Игорь":
            userid=1027
            projec_name=values[0]
            GetAllIssuesInAllProjects(redmine, userid, projec_name, statuslist)
            break
        if values['-Name-'][0] == "Алена":
            userid=1125
            projec_name = values[0]
            GetAllIssuesInAllProjects(redmine, userid, projec_name, statuslist)
            break
window.close()

