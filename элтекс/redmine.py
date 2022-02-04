#!/usr/bin/python3

from redminelib import Redmine


URL='http://red.eltex.loc'
KEY='2d3b622576170e6b31bd4d4547c83be4e7cc91c1'
redmine = Redmine(URL, key=KEY)

userlist = [
        69,
        1027,
        1125
    ]

'''69 - Алексей Глебко
1027 - Игорь Быков
1125 - Алена Новобранова'''

'''Статусы тикетов
New - 1
Re-opened - 8
In Progress - 2
Feedback - 13
Resolved - 3
Testing - 9
Closed - 5
Pending - 4
Wait Release - 10
'''

statuslist = [
        1,
        13,
        3,
        9
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
                    issues = redmine.issue.filter(project_id=msp.project.id, status_id=statusid, cf_2=userid)
                    for issue in issues:
                        print('\t\tНомер:', issue.id, 'Статус:', issue.status.name, 'Версия:', issue.fixed_version.name, 'Тема:', issue.subject)
                print('Количество проектов:', prjc)
        except:
            continue
                
            
