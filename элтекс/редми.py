from redminelib import Redmine

from datetime import date
from redminelib import Redmine  
from datetime import datetime  
from datetime import timedelta  
time = datetime.now()  
##checktime = time -timedelta(minutes = 5) 



URL=' '
KEY=' '
redmine = Redmine(URL, key=KEY)
userlist = [
        69
    ]

statuslist = [
        1
    ]
def GetAllIssuesInAllProjects(redmine, userlist, statuslist):
    for userid in userlist:
        try:
            print(redmine.user.get(userid).firstname, redmine.user.get(userid).lastname)
            ms = redmine.user.get(userid, include='memberships')
            prjc = 0
            for msp in ms.memberships:
                prjc += 1
                print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                for statusid in statuslist:
                    issues = redmine.issue.filter(project_id = msp.project.id, status_id = statusid, created_on = '>=%s'%checktime.strftime('%Y-%m-%d'),cf_2=userid)
                    for issue in issues:
                        print('\t\tНомер:', issue.id, 'Статус:', issue.status.name, 'Версия:', issue.fixed_version.name, 'Тема:', issue.subject)
                print('Количество проектов:', prjc)
        except:
            continue
                
