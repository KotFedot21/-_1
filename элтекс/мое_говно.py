import PySimpleGUI as sg
import matplotlib.pyplot as plt
from datetime import date
from datetime import timedelta

d = []
def information_for_the_week(d):

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



sg.theme('SystemDefault')
sg.SetOptions(element_padding=(0,0))

#----- переменные ------#
text_font=('Consolas',12)
#-----макет меню ---#
menu_def =[ ['Статистика',['день','неделя','указать']],
            ['Загруженность'],
            ['Добавить',['ID','состояние']]]
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
        information_for_the_week(d)

        userID = [69, 12, 123]
        tasks = [4, 5]
        tasks1 = [1, 3]
        tasks2 = [0, 7]

        plt.plot(d, tasks, '--r', label=userID[0])
        plt.plot(d, tasks1, ':b', label=userID[1])
        plt.plot(d, tasks2, 'k', label=userID[2])

        """ax = plt.figure().gca()
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))"""

        plt.legend(fontsize=14)

        plt.show()



#------Функции------#


window.read()
