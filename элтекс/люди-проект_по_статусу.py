import PySimpleGUI as sg
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
# import PySimpleGUIQt as sg
statuslist = [

    13,
    3,
    9,
    1,
    2,
    8,
    5,
    4,
    10
]
userlist = [
        69,
        1027,
        1125
    ]
filt=[]

def sbor_dann():    
    # ----------- Create the 3 layouts this Window will display -----------
    layout1 = [[sg.Text('Выберите статус')],
               *[[sg.CB(f'Cтатус {i}')] for i in statuslist ],
               [sg.Text('Название проекта', size=(15, 1)), sg.InputText()]]# вставляем сюда список состояний
    
    
    # ----------- Create actual layout using Columns and a row of Buttons
    layout = [[sg.Column(layout1, key='-COL1-')],
              [sg.Button('Cycle Layout'),  sg.Button('Exit')]]
    
    window = sg.Window(' ', layout)
    
    layout = 1  # The currently visible layout
    while True:
        event, values = window.read()
        g=[]
        for key in values:
            g.append(values[key])
        #print(g)#True/Fals
        dictionary_of_states = dict(zip(statuslist ,g))#переим в состояния
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Cycle Layout':
            window[f'-COL{layout}-'].update(visible=False)
            window[f'-COL{layout}-'].update(visible=True)
            ST='-Status-'
            print(ST)
    
   
    print (dictionary_of_states)
    return dictionary_of_states
    window.close()
    
#print(sbor_dann())

def analiz():# переименуй!!!!! получение необходимого статус листа

    w=sbor_dann()
    for key in w:
        if w[key]==True:
            filt.append(key)
    print(filt)
    return filt  #далее используется этот статус лист 
analiz()

def GetAllIssuesInAllProjects(redmine, userlist,filt ):
    print(filt)
    for userid in userlist:
        try:
            ms = redmine.user.get(userid, include='memberships')
            
                
            prjc = 0
            for msp in ms.memberships:
                try:
                    prjc += 1
                    for statusid in filt:
                        issues = redmine.issue.filter(project_id=msp.project.id, status_id=statusid, cf_2=userid)
                        for issue in issues:
                            print(redmine.user.get(userid).firstname, redmine.user.get(userid).lastname)
                            print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                            print('\t\tНомер:', issue.id, 'Статус:', issue.status.name, 'Версия:', issue.fixed_version.name, 'Тема:', issue.subject)
                            #print('Количество проектов:', prjc)
                
                except:
                    print(redmine.user.get(userid).firstname, redmine.user.get(userid).lastname)
                    print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                    print('\t\tНомер:', issue.id, 'Статус:', issue.status.name, 'Версия:', issue.fixed_version.name, 'Тема:', issue.subject)

        except:
            continue
GetAllIssuesInAllProjects(redmine, userlist, filt)



