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
userlist = [69]
statuslist =[3,9,13]

def GetAllIssuesInAllProjects(redmine, userlist, statuslist):

    matrix=[]
    for userid in userlist:
        #col=0  #кол-во проектов в которых есть задачи ОБЩИЕ
        
        try:
            
            #print(redmine.user.get(userid).firstname, redmine.user.get(userid).lastname)
            ms = redmine.user.get(userid, include='memberships')
            prjc = 0 #кол-во всех проектов в которых учавствует 
            #col=0  #кол-во проектов в которых есть задачи 
            for msp in ms.memberships:
                prjc += 1
                #print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                for statusid in statuslist:
                    issues = redmine.issue.filter(project_id=msp.project.id, status_id=statusid, cf_2=userid)
                   
                    for issue in issues:
                        a = []
                        
                        redmine_user_ge_firstname = str(redmine.user.get(userid).firstname)
                        #a.append(redmine_user_ge_firstname)
                        

                        msp_project_name = str(msp.project.name)
                        a.append(msp_project_name)
                        
                                                
                        issue_id = str(issue.id)
                        #a.append(issue_id)
                        
                        
                    
                        issue.status_name = str(issue.status.name)
                        
                        
                        #сравнение строк для определения 
                        
                        if issue.status_name=='Resolved':
                            a.append(issue_id)
                            a.append("----")
                            a.append("----")
                        elif issue.status_name=='Feedback':   
                            a.append("----")
                            a.append(issue_id)
                            a.append("----")
                        elif issue.status_name=='Testing':
                            a.append("----")
                            a.append("----")
                            a.append(issue_id)   
                          
                        matrix.append(a)
                        
                        
                        #print('Количество проектов:', col)
                        
                        
                        
                        
                #print('Количество проектов:', col)
        except:
            continue
            
    headings = [ "   Название проекта    ", '    Resolved    ', '     Feedback     ', '     Testing    ' ]

    # ------ Window Layout ------
    layout = [[sg.Table(values=matrix, headings=headings, max_col_width=35,
                        # background_color='light blue',
                        justification='right',
                        num_rows=20,
                        alternating_row_color='lightyellow',
                        key='-TABLE-',
                        row_height=35,
                        tooltip='This is a table')],
              [sg.Button('Выход')]]

    # ------ Create Window ------
    window = sg.Window('Aлексей', layout)

    # ------ Event Loop ------
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break

    window.close()
     
GetAllIssuesInAllProjects(redmine, userlist, statuslist)  


