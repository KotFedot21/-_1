
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
from PIL import Image
from datetime import datetime
from datetime import timedelta
import  re
URL='http://red.eltex.loc'
KEY = '08c017a3b50e09357a72e4448cc1aa6f09271755'

redmine = Redmine(URL, key=KEY)
#image=Image.open(r'/home/anna/Загрузки/98.png')
userlist = [
        69,
        1027,
        1125
    ]


statuslist = [

        13,
        3,
        9
    ]
speed=[]
current_date = date.today()
matrix1=[]
date  = date.today()
man=[]
date_1=[]
data0=[]


def error_window():
    layout = [[sg.Text("Неверное название проекта ")],
          [sg.Text(" ", size=(18, 1))],
          [sg.Button("OK", key='OK')]]

    window = sg.Window(" ", layout,
                       return_keyboard_events=True, use_default_focus=False)
    
    # ---===--- Loop taking in user input --- #
    while True:
        event, values = window.read()
        
        if event in ("OK", None):
            print(event, "exiting")
            break

    
    
    window.close()

def project_output(redmine, userid, projec_name):
    matrix=[]

    try:
        ms = redmine.user.get(userid, include='memberships')
        prjc = 0
        for msp in ms.memberships:
            a=[]    

            issues = redmine.issue.filter(project_id=msp.project.id, cf_2=userid)

            r=[]
            f=[]
            t=[]
            if projec_name==msp.project.name:
                for issue in issues:

                    issue.status_name = str(issue.status.name)
                    msp_project_name = str(msp.project.name)
                    a.append(msp_project_name)

                    if issue.status_name=='Resolved':
                        issue_id = str(issue.id)
                        r.append(issue_id)
                        #print('\tPROJECT NAME:', msp.project.name,'\n\t\tНомер:', issue.id, 'Статус:', issue.status.name)
                        #print(r)

                    elif issue.status_name=='Feedback':
                        issue_id = str(issue.id)
                        f.append(issue_id)
                        #print('\tPROJECT NAME:', msp.project.name,'\n\t\tНомер:', issue.id, 'Статус:', issue.status.name)
                        #print(f)

                    elif issue.status_name=='Testing':
                        issue_id = str(issue.id)
                        t.append(issue_id)
                        #print('\tPROJECT NAME:', msp.project.name,'\n\t\tНомер:', issue.id, 'Статус:', issue.status.name)
                        #print(t)
                        """
                   elif issue.status_name=='New':
                        issue_id = str(issue.id)
                        n.append(issue_id)######
                        
                        
                    elif issue.status_name=='Re-opened':
                        issue_id = str(issue.id)
                        re.append(issue_id)
                        
                        
                    elif issue.status_name=='In Progress':
                        issue_id = str(issue.id)
                        ip.append(issue_id)
                        
                    elif issue.status_name=='Closed':
                        issue_id = str(issue.id)
                        c.append(issue_id)
                        
                    elif issue.status_name=='Pending':
                        issue_id = str(issue.id)
                        p.append(issue_id)
                        
                    elif issue.status_name=='Wait Release':
                        issue_id = str(issue.id)
                        w.append(issue_id) """                  
                    
                if len(r)!= 0 or len(f)!= 0 or len(t)!= 0:
                    del a[1:]#для корректного вывода 
                    a.append(r)
                    a.append(f)
                    a.append(t)
                    #print(a)
                    matrix.append(a)
                 

#print(prjc )   
    except:
        print("error")
        
    if len(matrix)==0:
        error_window()
        
    else:
        
        headings = [ "  Название проекта   ", '    Resolved    ', '     Feedback     ', '     Testing    ' ]
    
        # ------ Window Layout ------
        layout = [[sg.Table(values=matrix, headings=headings, max_col_width=35,
                            background_color='light sky blue',
                            justification='right',
                            num_rows=20,
                            alternating_row_color="steel blue",
                            key='-TABLE-',
                            row_height=15,
                            tooltip='This is a table')]]
    
        # ------ Create Window ------
        window = sg.Window(redmine.user.get(userid).firstname, layout)
    
        # ------ Event Loop ------
        while True:
            event, values = window.read()
            print(event, values)
            if event == sg.WIN_CLOSED:
                break
    
        window.close()



def employee_and_project_selection():
    sg.theme('Reddit') # Add some color to the window
    
    # Very basic window.  Return values using auto numbered keys
    choices=[]
    for userid in userlist:
        firstname=(redmine.user.get(userid).firstname)#вывести на экран 
        lastname=(redmine.user.get(userid).lastname)
        choices.append(firstname+" "+lastname)#project_output(redmine, userid, projec_name)

    print (choices)
    
    dic = dict(zip( choices,userlist))#список для программы на соответствие 
    
    print (dic)
    
    
    layout = [  [sg.Text('Выберите сотрудника')],[sg.Listbox(choices, size=(40, len(choices)), key='-Name-')],
            [sg.Text('Выберите статус')],[sg.Listbox(statuslist, size=(40, len(statuslist)), key='-Status-')],
            [sg.Text('Название проекта', size=(15, 1)), sg.InputText()],
            [sg.Button('Ok')]  ]
    
    window = sg.Window('', layout)
    
    while True:
                  # the event loop
        event, values = window.read()
        print( event, values)
        if event == sg.WIN_CLOSED:
            break
        if event == 'Ok':
            for key in dic:
                if values['-Name-'][0]==key:
                    userid=dic[key]
                    ST='-Status-'
                    projec_name=values[0]
                    project_output(redmine, userid, projec_name,)
                    break

    window.close()
employee_and_project_selection()
