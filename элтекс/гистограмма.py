import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

from redminelib import Redmine
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from datetime import date
from datetime import timedelta
from simplejson.tests.test_speedups import has_speedups
plt.rcdefaults()
import numpy as np

URL='http://red.eltex.loc'
KEY='08c017a3b50e09357a72e4448cc1aa6f09271755'
redmine = Redmine(URL, key=KEY)
userlist = [69,1027,1125]
statuslist =[5]
speed=[]
current_date = date.today()## дата сегодня

def GetAllIssuesInAllProjects(redmine, userlist, statuslist,current_date ):
    #prjc = 0
    current_date1 = str(current_date)
    for userid in userlist:
        try:
            
            ms = redmine.user.get(userid, include='memberships')
            prjc = 0
            for msp in ms.memberships:
               
                
                for statusid in statuslist:
                    #prjc += 1
                    issues = redmine.issue.filter(project_id=msp.project.id,updated_on= current_date1, status_id=statusid, cf_2=userid)
                    
                    for issue in issues:
                        
                        #print(redmine.user.get(userid).firstname, redmine.user.get(userid).lastname)
                        #print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                        #print('\t\tНомер:', issue.id, 'Статус:', issue.status.name, 'Версия:', issue.fixed_version.name,"updated on", issue.updated_on,  'Тема:', issue.subject)
                        prjc += 1
                        #print("кол-во задач",prjc)
                        #speed.append(prjc)
         
            speed.append(prjc)    #print('Количество проектов:', prjc)
        except:
            continue
        

    
    return speed

print(GetAllIssuesInAllProjects(redmine, userlist, statuslist,current_date))


name = ("Алексей","Игорь", "Алена")
y_pos = np.arange(len(name))
    
plt.bar(y_pos, speed, align='center', alpha=0.5)
plt.xticks(y_pos, name)
plt.ylabel('Задачи ')
plt.title('Сотрудники')
    
plt.show()
