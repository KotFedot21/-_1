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

userlist = [
        #69,
        1027,
        #1125
    ]

statuslist = [

        13,
        3,
        9
    ]


def GetAllIssuesInAllProjects(redmine, userlist,statuslist):
    matrix=[]
    for userid in userlist:
        try:
            ms = redmine.user.get(userid, include='memberships')
            prjc = 0
            for msp in ms.memberships:
                a=[]    

                issues = redmine.issue.filter(project_id=msp.project.id, cf_2=userid)



                r=[]
                f=[]
                t=[]
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
                if len(r)!= 0 or len(f)!= 0 or len(t)!= 0:
                    del a[1:]#для корректного вывода 
                    a.append(r)
                    a.append(f)
                    a.append(t)
                    #print(a)
                    matrix.append(a)

  #print(prjc )   
        except:
            continue

    headings = [ "   Название проекта    ", '    Resolved    ', '     Feedback     ', '     Testing    ' ]

    # ------ Window Layout ------
    layout = [[sg.Table(values=matrix, headings=headings, max_col_width=35,
                        background_color='light sky blue',
                        justification='right',
                        num_rows=20,
                        alternating_row_color="steel blue",
                        key='-TABLE-',
                        row_height=35,
                        tooltip='This is a table')],
              [sg.Button('Выход')]]

    # ------ Create Window ------
    window = sg.Window(redmine.user.get(userid).firstname, layout)

    # ------ Event Loop ------
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break

    window.close()

GetAllIssuesInAllProjects(redmine, userlist,statuslist)
