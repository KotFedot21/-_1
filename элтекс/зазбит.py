import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
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

def function_for_the_day(ms,th,current_date1,userid):
    for msp in ms.memberships:
        try:
            issues = redmine.issue.filter(project_id=msp.project.id,updated_on= current_date1, status_id=5, cf_2=userid)
            
            for issue in issues:
                th.append(issue.id)
        
        except:
            print("Error")
    return th

def GetAllIssuesInAllProjects(redmine, userlist, statuslist,current_date):
    #prjc = 0
    matrix=[]
    tasks=[]
    current_date1 = str(current_date)
    for userid in userlist:
        try:
            th=[]
            ms = redmine.user.get(userid, include='memberships')
            
            
            function_for_the_day(ms,th,current_date1,userid)
            
            
            th1 = list(set(th))
            prjc=len(th1)
            speed.append(prjc)    #print('Количество проектов:', prjc)
            
        except:
            continue

    return speed

def output_of_statistics_for_the_day(): 
    
    
    GetAllIssuesInAllProjects(redmine, userlist, statuslist,current_date)
    name =[]
    for us in userlist:
        name.append(redmine.user.get(us).firstname)
        
    y_pos = np.arange(len(name))
        
    plt.bar(y_pos, speed, align='center', alpha=0.5)
    plt.xticks(y_pos, name)
    plt.ylabel('Задачи ')
    plt.title('Сотрудники')
        
    plt.show()
    

    
output_of_statistics_for_the_day()
