from redminelib import Redmine
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from datetime import date
from datetime import timedelta
from asyncio import tasks
plt.rcdefaults()
import numpy as np
import calendar
from multiprocessing import Pool
from PIL import Image
from datetime import datetime
from datetime import timedelta
import  re
URL='http://red.eltex.loc'

redmine = Redmine(URL, key=KEY)
#image=Image.open(r'/home/anna/Загрузки/98.png')
userlist = [
        69,
        1027,
        1125
    ]
statuslistс = [
    5
]

statuslist = [

        13,
        3,
        9
    ]
speed=[]
current_date = date.today()
matrix1=[]
date  = date.today()
man=[]
date_1=[]
data0=[]


def error_window():
    layout = [[sg.Text("Неверное название проекта ")],
          [sg.Text(" ", size=(18, 1))],
          [sg.Button("OK", key='OK')]]

    window = sg.Window(" ", layout,
                       return_keyboard_events=True, use_default_focus=False)
    
    # ---===--- Loop taking in user input --- #
    while True:
        event, values = window.read()
        
        if event in ("OK", None):
            print(event, "exiting")
            break

    
    
    window.close()

def project_output(redmine, userid, projec_name):
    matrix=[]

    try:
        ms = redmine.user.get(userid, include='memberships')
        prjc = 0
        for msp in ms.memberships:
            a=[]    

            issues = redmine.issue.filter(project_id=msp.project.id, cf_2=userid)

            r=[]
            f=[]
            t=[]
            if projec_name==msp.project.name:
                for issue in issues:

                    issue.status_name = str(issue.status.name)
                    msp_project_name = str(msp.project.name)
                    a.append(msp_project_name)

                    if issue.status_name=='Resolved':
                        issue_id = str(issue.id)
                        r.append(issue_id)
                        #print('\tPROJECT NAME:', msp.project.name,'\n\t\tНомер:', issue.id, 'Статус:', issue.status.name)
                        #print(r)

                    elif issue.status_name=='Feedback':
                        issue_id = str(issue.id)
                        f.append(issue_id)
                        #print('\tPROJECT NAME:', msp.project.name,'\n\t\tНомер:', issue.id, 'Статус:', issue.status.name)
                        #print(f)

                    elif issue.status_name=='Testing':
                        issue_id = str(issue.id)
                        t.append(issue_id)
                        #print('\tPROJECT NAME:', msp.project.name,'\n\t\tНомер:', issue.id, 'Статус:', issue.status.name)
                        #print(t)
                if len(r)!= 0 or len(f)!= 0 or len(t)!= 0:
                    del a[1:]#для корректного вывода 
                    a.append(r)
                    a.append(f)
                    a.append(t)
                    #print(a)
                    matrix.append(a)
                 

#print(prjc )   
    except:
        print("error")
        
    if len(matrix)==0:
        error_window()
        
    else:
        headings = [ "  Название проекта   ", '    Resolved    ', '     Feedback     ', '     Testing    ' ]
    
        # ------ Window Layout ------
        layout = [[sg.Table(values=matrix, headings=headings, max_col_width=35,
                            background_color='light sky blue',
                            justification='right',
                            num_rows=20,
                            alternating_row_color="steel blue",
                            key='-TABLE-',
                            row_height=15,
                            tooltip='This is a table')]]
    
        # ------ Create Window ------
        window = sg.Window(redmine.user.get(userid).firstname, layout)
    
        # ------ Event Loop ------
        while True:
            event, values = window.read()
            print(event, values)
            if event == sg.WIN_CLOSED:
                break
    
        window.close()



def employee_and_project_selection():
    sg.theme('Reddit')      # Add some color to the window
    
    # Very basic window.  Return values using auto numbered keys
    choices = ("Алексей","Игорь","Алена")#передаем id сотрудников из редмайна
    
    layout = [  [sg.Text('Выберите сотрудника')],[sg.Listbox(choices, size=(40, len(choices)), key='-Name-')],
                [sg.Text('Название проекта', size=(15, 1)), sg.InputText()],
                [sg.Button('Ok')]  ]
    
    window = sg.Window('', layout)
    
    while True:                  # the event loop
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Ok':
            if values['-Name-'][0]=="Алексей":
                userid = 69
                projec_name=values[0]
                print (projec_name)
                project_output(redmine, userid, projec_name)
                break
            if values['-Name-'][0] == "Игорь":
                userid=1027
                projec_name=values[0]
                project_output(redmine, userid, projec_name)
                break
            if values['-Name-'][0] == "Алена":
                userid=1125
                projec_name = values[0]
                project_output(redmine, userid, projec_name)
                break
    window.close()


def user_data_for_the_period(userid):
    matrix1=[]
    for dat in data0:
        print(dat)
        th=[]
        th1 =[]
        ms = redmine.user.get(userid, include='memberships')
        prjc = 0
        for msp in ms.memberships:
            try:
                issues = redmine.issue.filter(project_id=msp.project.id, status_id=5,updated_on=dat, cf_2=userid)
                for issue in issues:
                    

                    print(redmine.user.get(userid).firstname, redmine.user.get(userid).lastname)
                    print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                    print('\t\tНомер:', issue.id, 'Статус:', issue.status.name, 'Версия:', issue.fixed_version.name, 'Тема:', issue.subject)
                    th.append(issue.id)
                    
                th1 = list(set(th))
                
            except:
                print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                print("Доступ к проекту запрещен")

            prjc=len(th1)
            
            

        matrix1.append(prjc)
        print(matrix1)

    print(matrix1)
    return matrix1

def Calendar(redmine, userlist):

    sg.theme('Reddit')
    layout = [[sg.Text('Выберите дату', key='-TXT-')],

          [sg.Input(key='-IN3-', size=(20,1)), sg.CalendarButton('Начало ', title='Pick a date any date', no_titlebar=True,
                                                                 close_when_date_chosen=False,  target='-IN3-',
                                                                 begin_at_sunday_plus=1, month_names=('Январь', 'Февраль',
                                                                                                      'Март', 'Апрель', 'Май',
                                                                                                      'Июнь', 'Июль', 'Август',
                                                                                                      'Сентябрь', 'Октябрь',
                                                                                                      'Ноябрь', 'Декабрь'),
                                                                 day_abbreviations=( 'ВС','ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ'))],
          [sg.Input(key='-IN2-', size=(20,1)), sg.CalendarButton('Завершение',  title='Pick a date any date', no_titlebar=True,
                                                                 close_when_date_chosen=False,  target='-IN2-',
                                                                 begin_at_sunday_plus=1, month_names=('Январь', 'Февраль',
                                                                                                      'Март', 'Апрель', 'Май',
                                                                                                      'Июнь', 'Июль', 'Август',
                                                                                                      'Сентябрь', 'Октябрь',
                                                                                                      'Ноябрь', 'Декабрь'),
                                                                 day_abbreviations=( 'ВС','ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ'))],
          [sg.Button('OK')]]

    window = sg.Window('window', layout)
    
    

    while True:
        event, values = window.read()
        print( event, values)
        #print( tuple(values))
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'OK':
            first_date = values['-IN3-']
            end_date = values['-IN2-']
            print( tuple(end_date))
            print (first_date, end_date)

            s=" ".join(first_date)
            a=re.sub(r"\s+", "", s)
            a= a[:-8]
            d=datetime.strptime(a, '%Y-%m-%d').date()
            print(d)
            

            s1=" ".join(end_date)
            a1=re.sub(r"\s+", "", s1)
            a1= a1[:-8]
            d1=datetime.strptime(a1, "%Y-%m-%d").date()
            print(d1)
            

            del data0[:]
            del date_1[:]
            data0.append(str(d))
            date_1.append(d.day)
            while d<d1:
                d = d + timedelta(days=1)
                data0.append(str(d)) 
                date_1.append(d.day)
        
            print(data0)
            print(date_1)
        
            window.close()
        
            agents = 3#кол-во сотр
            chunksize = 1
            with Pool(processes=agents) as pool:
                result = pool.map(user_data_for_the_period, userlist, chunksize)
            print(result)
        
            #return result
        
        
            name =[]
            for us in userlist:
                name.append(redmine.user.get(us).firstname)
            index = np.arange(len(date_1))#кол-во дат
            lin=['g','b','m']#g,b,r,c,m,y
            bw=0.05
            x=len(date_1)
            plt.axis([0,x,0,5])
            for res, us, li in zip(result, userlist, lin):
                    plt.bar(index, res, bw, color=li, label=redmine.user.get(us).firstname)
                    index=index+bw
            #plt.figure(figsize=(10, 10))#в дюймах
            index = np.arange(len(date_1))
            plt.xticks(index+2*bw,date_1)
            
        
            plt.legend(fontsize=14)
            plt.show()

def user_data_for_the_month(userid):
    matrix1=[]
    for ma in man:
        th=[]
        ms = redmine.user.get(userid, include='memberships')
        prjc = 0
        for msp in ms.memberships:
            try:
                issues = redmine.issue.filter(project_id=msp.project.id, status_id=5,updated_on=ma, cf_2=userid)
                for issue in issues:

                    print(redmine.user.get(userid).firstname, redmine.user.get(userid).lastname)
                    print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                    print('\t\tНомер:', issue.id, 'Статус:', issue.status.name, 'Версия:', issue.fixed_version.name, 'Тема:', issue.subject)
                    th.append(issue.id)
                    
                th1 = list(set(th))
                
            except:
                print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                print("Доступ к проекту запрещен")

            prjc=len(th1)
            
            

        matrix1.append(prjc)
        print(matrix1)

    print(matrix1)
    return matrix1

def statistics_for_the_month(redmine, userlist):

    
    agents = 3#кол-во сотр
    chunksize = 1
    with Pool(processes=agents) as pool:
        result = pool.map(user_data_for_the_month, userlist, chunksize)
    print(result)

    return result

def monthly_schedule():

    d=[]

    
    date_01= date.replace(day=calendar.monthrange(date.year, date.month)[0])
    date_2= date.replace(day=calendar.monthrange(date.year, date.month)[1])
    while date_01<=date:
        cur_date1 = str(date_01)
        d.append(date_01.day)
        man.append(cur_date1)
        date_01 = date_01 + timedelta(1)

    print(man)
    print(d)
    
    h=statistics_for_the_month(redmine,userlist)
    
    lin=['r','b','k']
    for hi, us, li in zip(h, userlist, lin):
        plt.plot(d, hi, li, label=redmine.user.get(us).firstname)

    plt.xlim([0,31])
    plt.ylim([0, 5])
    plt.legend(fontsize=14)
    plt.show()

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
    


def fearless_table(redmine, userl,statuslist):
    matrix=[]
    for userid in userl:
        try:
            ms = redmine.user.get(userid, include='memberships')
            prjc = 0
            for msp in ms.memberships:
                try:
                    a=[]    
    
                    issues = redmine.issue.filter(project_id=msp.project.id, cf_2=userid)
    
                    r=[]
                    f=[]
                    t=[]
                    for issue in issues:
    
                        issue.status_name = str(issue.status.name)
                        msp_project_name = str(msp.project.name)
                        a.append(msp_project_name)
    
                        if issue.status_name=='Resolved':
                            issue_id = str(issue.id)
                            r.append(issue_id)
                            #print('\tPROJECT NAME:', msp.project.name,'\n\t\tНомер:', issue.id, 'Статус:', issue.status.name)
                            #print(r)
    
                        elif issue.status_name=='Feedback':
                            issue_id = str(issue.id)
                            f.append(issue_id)
                            #print('\tPROJECT NAME:', msp.project.name,'\n\t\tНомер:', issue.id, 'Статус:', issue.status.name)
                            #print(f)
    
                        elif issue.status_name=='Testing':
                            issue_id = str(issue.id)
                            t.append(issue_id)
                            #print('\tPROJECT NAME:', msp.project.name,'\n\t\tНомер:', issue.id, 'Статус:', issue.status.name)
                            #print(t)
                    if len(r)!= 0 or len(f)!= 0 or len(t)!= 0:
                        del a[1:]#для корректного вывода 
                        a.append(r)
                        a.append(f)
                        a.append(t)
                        #print(a)
                        matrix.append(a)
                except:
                    print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                    print("Доступ к проекту запрещен")
  #print(prjc )   
        except:
            print("error2")
            continue

    headings = [ "     Название проекта      ", '           Resolved            ', '           Feedback           ', '          Testing          ' ]

    # ------ Window Layout ------
    layout = [[sg.Table(values=matrix, headings=headings, max_col_width=35,
                        background_color='light sky blue',
                        auto_size_columns=True,
                        #display_row_numbers=True, номер строки
                        justification='right',
                        num_rows=28,
                        alternating_row_color="steel blue",
                        key='-TABLE-',
                        row_height=35,
                        tooltip='This is a table')],
              ]

    # ------ Create Window ------
    window = sg.Window(redmine.user.get(userid).firstname, layout)

    # ------ Event Loop ------
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break

    window.close()


def information_for_the_week():
    d=[]   ### для повторного использования
    current_date = date.today()## дата сегодня
    print(current_date)
    current_d = current_date.weekday()
    print(current_date.weekday())##номер дня, 0-понедельник
    num = current_date.weekday()
    monday_date = current_date - timedelta(days=num)##получаем дату понедельника
    print(monday_date)

    j=0

    current_date2=[]
    while j <= 4: # создает список из дат недели

        current_date1 = str(monday_date)
        current_date2.append(current_date1)
        monday_date = monday_date + timedelta(days=1)

        j+=1
    monday_date = current_date - timedelta(days=num)  ##получаем дату понедельника
    print (current_date2)
    return current_date2

def information_for_the_week2():
    d=[]   ### для повторного использования
    current_date = date.today()## дата сегодня
    print(current_date)
    current_d = current_date.weekday()
    print(current_date.weekday())##номер дня, 0-понедельник
    num = current_date.weekday()
    monday_date = current_date - timedelta(days=num)##получаем дату понедельника
    print(monday_date)
    i = 0

    current_date2=[]
    while i <= 4 : # создает список из дней недели для графика
        d.append(monday_date.day)
        monday_date = monday_date + timedelta(1)
        i += 1
        

    print(d)
    return d

def egjstgh(userid):
    
    
    for current_dateid in information_for_the_week() :

        th=[]
        ms = redmine.user.get(userid, include='memberships')
        prjc = 0
        
        for msp in ms.memberships:
            try:
            
                issues = redmine.issue.filter(project_id=msp.project.id, status_id=5,updated_on=current_dateid, cf_2=userid)

                
                for issue in issues:

                    print(redmine.user.get(userid).firstname, redmine.user.get(userid).lastname)
                    print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                    print('\t\tНомер:', issue.id, 'Статус:', issue.status.name, 'Версия:', issue.fixed_version.name, 'Тема:', issue.subject)
                    th.append(issue.id)
                    
                th1 = list(set(th))
                
            except:
                print('\tPROJECT NAME:', msp.project.name, 'ID:', msp.project.id)
                print("Доступ к проекту запрещен")

            prjc=len(th1)
            
            

        matrix1.append(prjc)
        print(matrix1)
    #tasks.append(matrix1)
    return matrix1

def GetAllIssuesInAllProjects(redmine, userlist):

    

    agents = 3
    chunksize = 1
    with Pool(processes=agents) as pool:
        result = pool.map(egjstgh, userlist, chunksize)
        
    print(result)
    return result



def statistics_for_the_week():
    s=information_for_the_week2()
    h=GetAllIssuesInAllProjects(redmine, userlist)
    name =[]
    for us in userlist:
        name.append(redmine.user.get(us).firstname)
    index = np.arange(5)#кол-во дат
    lin=['g','b','m']#g,b,r,c,m,y
    bw=0.2
    plt.axis([0,4.5,0,5])
    for hi, us, li in zip(h, userlist, lin):
            plt.bar(index, hi, bw, color=li, label=redmine.user.get(us).firstname)
            index=index+bw
    #plt.figure(figsize=(10, 10))#в дюймах
    index = np.arange(5)
    plt.xticks(index+2*bw,s)
    

    plt.legend(fontsize=14)
    plt.show()
#######


#########
sg.theme('SystemDefault')
sg.SetOptions(element_padding=(0,0))

#----- переменные ------#
text_font=('Consolas',12)
#-----макет меню ---#
menu_def =[ ['Статистика',['день','неделя','месяц',"указать диапозон"]],
            ['Загруженность',['Алексей',"Игорь","Алена","Указать прокет"]],
            ["Начать"]]
#-----Макет формы----#
layout = [
    [sg.Menu(menu_def, tearoff=False)]]#,[sg.Image(data=image)]
window = sg.Window('Editor', layout=layout, margins=(0,0), resizable=True, return_keyboard_events=True, finalize=True, size=(850,350))


#----Цикл обработки событий ----#
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event =='Exit':
        break
    
    elif event in ('день'):
        output_of_statistics_for_the_day()
 

    elif event in ('Алексей'):
        userl=[69]
        fearless_table(redmine, userl,statuslist)
        
    elif event in ('Игорь'):
        userl=[1027]
        fearless_table(redmine, userl,statuslist)
        
    elif event in ('Алена'):
        userl=[1125]
        fearless_table(redmine, userl,statuslist)

    elif event in ('месяц'):
        monthly_schedule()

    elif event in ('неделя'):
        statistics_for_the_week()
        
    elif event in ('указать диапозон'): 
        Calendar(redmine, userlist)
        
    elif event in ("Указать прокет"):
        employee_and_project_selection()
        
window.read()
