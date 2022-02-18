from redminelib import Redmine

URL='http://red.eltex.loc'
KEY='08c017a3b50e09357a72e4448cc1aa6f09271755'
redmine = Redmine(URL, key=KEY)
userlist = [69,1027]
statuslist =[3]

def GetAllIssuesInAllProjects(redmine, userlist, statuslist):

    matrix=[]
    for userid in userlist:
        col=0  #кол-во проектов в которых есть задачи ОБЩИЕ
        
        try:
            
            #print(redmine.user.get(userid).firstname, redmine.user.get(userid).lastname)
            ms = redmine.user.get(userid, include='memberships')
            prjc = 0 #кол-во всех проектов в которых учавствует 
            col=0  #кол-во проектов в которых есть задачи 
            for msp in ms.memberships:
                prjc += 1
                #print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                for statusid in statuslist:
                    issues = redmine.issue.filter(project_id=msp.project.id, status_id=statusid, cf_2=userid)
                   
                    for issue in issues:
                        a = []
                        a[0]=(redmine.user.get(userid).firstname)
                        a[1]=(msp.project.name)
                        #a.append(issue.id)
                        #a.append(issue.status.name)
                        #a.append(None)
                        #a.append(None)
                        #matrix.append(a)
                        col+=1
                        print(redmine.user.get(userid).firstname, redmine.user.get(userid).lastname)
                        print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                        print('\t\tНомер:', issue.id, 'Статус:', issue.status.name, 'Версия:', issue.fixed_version.name, 'Тема:', issue.subject)
                        
                        
                        print('Количество проектов:', col)
                        
                        
                        
                        
                #print('Количество проектов:', col)
        except:
            continue
            

     
GetAllIssuesInAllProjects(redmine, userlist, statuslist) 
