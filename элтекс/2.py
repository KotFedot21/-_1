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
statuslist =[5]

def GetAllIssuesInAllProjects(redmine, userlist, statuslist):
    for userid in userlist:
        try:
            
            ms = redmine.user.get(userid, include='memberships')
            prjc = 0
            for msp in ms.memberships:
                #prjc += 1
                
                for statusid in statuslist:
                    #prjc += 1
                    issues = redmine.issue.filter(project_id=msp.project.id,updated_on='><2022-01-01|2022-02-02', status_id=statusid, cf_2=userid)
                    for issue in issues:
                        prjc += 1
                        print(redmine.user.get(userid).firstname, redmine.user.get(userid).lastname)
                        print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                        print('\t\tНомер:', issue.id, 'Статус:', issue.status.name, 'Версия:', issue.fixed_version.name,"updated on", issue.updated_on,  'Тема:', issue.subject)
                        print("кол-во задач",prjc)
                #print('Количество проектов:', prjc)
        except:
            continue
        
        
        
GetAllIssuesInAllProjects(redmine, userlist, statuslist) 
