from redminelib import Redmine

from datetime import date
from redminelib import Redmine  
from datetime import datetime  
from datetime import timedelta  
##time = datetime.now()  

time = datetime.date(2022, 1, 12)

##checktime = time -timedelta(minutes = 5) 



URL='http://red.eltex.loc'
KEY='08c017a3b50e09357a72e4448cc1aa6f09271755'
redmine = Redmine(URL, key=KEY)
userlist = [
        69
    ]

statuslist = [
        1
    ]
def GetAllIssuesInAllProjects(redmine, userlist, statuslist, time):
    for userid in userlist:
        try:
            print(redmine.user.get(userid).firstname, redmine.user.get(userid).lastname)
            ms = redmine.user.get(userid, include='memberships')
            prjc = 0
            for msp in ms.memberships:
                prjc += 1
               ## print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                for statusid in statuslist:
                    issues = redmine.issue.filter(project_id = msp.project.id, status_id = statusid, created_on = '>=%s'%time.strftime('%Y-%m-%d'),cf_2=userid)
                    for issue in issues:
                        print('\t\tНомер:', issue.id, 'Статус:', issue.status.name, 'Версия:', issue.fixed_version.name, 'Тема:', issue.subject)
                print('Количество проектов:', prjc)
        except:
            continue
                
