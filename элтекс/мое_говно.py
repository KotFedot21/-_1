import PySimpleGUI as sg
import matplotlib.pyplot as plt
from datetime import date
from datetime import timedelta
plt.rcdefaults()
import numpy as np


## переменные
userID = [69, 12, 123]
d = []


def information_for_the_week(d,userID):
    del d[:]   ### для повторного использования
    current_date = date.today()## дата сегодня
    print(current_date)
    print(current_date.weekday())##номер дня, 0-понедельник
    num = current_date.weekday()
    monday_date = current_date - timedelta(days=num)##получаем дату понедельника
    print(monday_date)
    i = 0
    while i <= num :
        d.append(monday_date.day)
        monday_date = monday_date + timedelta(1)
        i += 1

    print(d)

    tasks = [4, 5, 5]
    tasks1 = [1, 3, 3]
    tasks2 = [0, 7, 4]

    plt.plot(d, tasks, '--r', label=userID[0])
    plt.plot(d, tasks1, ':b', label=userID[1])
    plt.plot(d, tasks2, 'k', label=userID[2])

    """ax = plt.figure().gca()
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))"""

    plt.legend(fontsize=14)

    plt.show()




def information_for_the_day():


    name = ("Алексей", "Игорь", "Александр", "Владислав")

    y_pos = np.arange(len(name))
    speed = [8, 7, 12, 4]
    plt.bar(y_pos, speed, align='center', alpha=0.5)
    plt.xticks(y_pos, name)
    plt.ylabel('Задачи ')
    plt.title('Сотрудники')

    plt.show()


def ID(userID):
    sg.theme('Reddit')

    layout = [
        [sg.Text('Please enter your ID')],
        [sg.Text('ID', size=(15, 1)), sg.InputText()],
        [sg.OK()]
    ]
    window = sg.Window('New User', layout)
    event, values = window.read()
    window.close()

    userID.append(values[0])
    print(userID)



def employee_table():
    sg.theme('Reddit')

    data = [['rocsptjach', 161, 570, 844],
            ['jwsqgvyatn', 380, 524, 697],
            ['egeflqdyvd', 813, 138, 834],
            ['vkrguwdoaw', 642, 607, 209],
            ['rygewgrzst', 670, 570, 499],
            ['stsfbznqtn', 419, 540, 638],
            ['szycvyypig', 786, 581, 489],
            ['rixofzlgil', 483, 243, 970],
            ['yzqrqhtwvt', 213, 887, 55],
            ['rurwvjivsy', 75, 110, 795],
            ['dimuvsdwan', 630, 840, 842],
            ['xnmcmlyyjh', 284, 936, 368],
            ['xogepbuatb', 309, 408, 181],
            ['zpiuwvnfcz', 770, 750, 652]]

    headings = ['User', "Название проекта ", 'номер задачи', 'Статус']

    # ------ Window Layout ------
    layout = [[sg.Table(values=data, headings=headings, max_col_width=35,
                        # background_color='light blue',
                        justification='right',
                        num_rows=20,
                        alternating_row_color='lightyellow',
                        key='-TABLE-',
                        row_height=35,
                        tooltip='This is a table')],
              [sg.Button('Выход')]]

    # ------ Create Window ------
    window = sg.Window('Загруженность', layout)

    # ------ Event Loop ------
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break

    window.close()


sg.theme('SystemDefault')
sg.SetOptions(element_padding=(0,0))

#----- переменные ------#
text_font=('Consolas',12)
#-----макет меню ---#
menu_def =[ ['Статистика',['день','неделя','указать']],
            ['Загруженность',['Resolved',"Feedback","Testing"]],
            ['Добавить',['ID']],
            ["Начать"]]
#-----Макет формы----#
layout = [
    [sg.Menu(menu_def, tearoff=False)]]
window = sg.Window('Editor', layout=layout, margins=(0,0), resizable=True, return_keyboard_events=True, finalize=True)

#----Цикл обработки событий ----#
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event =='Exit':
        break
    elif event in ('день'):
        information_for_the_day()

    elif event in ('Показать загруженность'):
        employee_table()

    elif event in ('ID'):
        ID(userID)


    elif event in ('неделя'):
        information_for_the_week(d,userID)


window.read()
