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

def GetAllIssuesInAllProjects(redmine, userlist, statuslist):
    #prjc = 0
    
    for userid in userlist:
        try:
            
            ms = redmine.user.get(userid, include='memberships')
            prjc = 0
            for msp in ms.memberships:
               
                
                for statusid in statuslist:
                    #prjc += 1
                    issues = redmine.issue.filter(project_id=msp.project.id,updated_on='><2022-02-01|2022-02-22', status_id=statusid, cf_2=userid)
                    
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

print(GetAllIssuesInAllProjects(redmine, userlist, statuslist))


name = ("Алексей","Игорь", "Алена")
y_pos = np.arange(len(name))
    
plt.bar(y_pos, speed, align='center', alpha=0.5)
plt.xticks(y_pos, name)
plt.ylabel('Задачи ')
plt.title('Сотрудники')
    
plt.show()



"""def information_for_the_day ():
    current_date = datetime.datetime.today().replace(microsecond=0)
    print(current_date)
    zero_time = current_date - timedelta(minutes=current_date.minute,seconds=current_date.second,hours=current_date.hour)##получаем начало дня
    print (zero_time)
    while zero_time <= current_date :
        print ("информация за 5 минуту ")
        zero_time= zero_time + timedelta(minutes=5)
        print(zero_time)
information_for_the_day()
"""
