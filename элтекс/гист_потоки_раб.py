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
from все1 import speed
plt.rcdefaults()
import datetime
import numpy as np

URL='http://red.eltex.loc'
KEY='08c017a3b50e09357a72e4448cc1aa6f09271755'
redmine = Redmine(URL, key=KEY)
userlist = [69,1027,1125]
statuslist =[5]

current_date = date.today()## дата сегодня

def function_for_the_day(userid):
    th=[]
    prjc=0
    current_date1 = str(current_date)
    ms = redmine.user.get(userid, include='memberships')
    
    
    for msp in ms.memberships:
        try:
            issues = redmine.issue.filter(project_id=msp.project.id,updated_on= current_date1, status_id=5, cf_2=userid)
            
            for issue in issues:
                th.append(issue.id)
                
        
        except:
            print("Error")
    
    
    th1 = list(set(th))
    print(th1)
    prjc=len(th1)
    print(prjc)

    return prjc    #print('Количество проектов:', prjc)

def histogram(redmine, userlist, statuslist):
    #prjc = 0

    tasks=[]
    speed=0


    try:
        
        agents = 3
        chunksize = 1
        with Pool(processes=agents) as pool:
            result = pool.map(function_for_the_day, userlist, chunksize)
        print(result)
 
    except:
            print("Error2")

    return result 


def output_of_statistics_for_the_day(): 
    
    
    r=histogram(redmine, userlist, statuslist)
    name =[]
    for us in userlist:
        name.append(redmine.user.get(us).firstname)
        
    y_pos = np.arange(len(name))
        
    plt.bar(y_pos, r, align='center', alpha=0.5)
    plt.xticks(y_pos, name)
    plt.ylabel('Задачи ')
    plt.title('Сотрудники')
        
    plt.show()
    

    
output_of_statistics_for_the_day()
