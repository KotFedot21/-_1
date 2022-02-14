import PySimpleGUI as sg
import random
import string

sg.theme('Reddit')

data = [['rocsptjach', 161, 570, 844 ],
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

headings = ['Название проекта', "user1", 'user 2', 'user 3']

# ------ Window Layout ------
layout = [[sg.Table(values=data, headings=headings, max_col_width=35,
                    #background_color='light blue',
                    justification='right',
                    num_rows=20,
                    alternating_row_color='lightyellow',
                    key='-TABLE-',
                    row_height=35,
                    tooltip='This is a table')],
          [sg.Button('Выход')]]

# ------ Create Window ------
window = sg.Window('The Table Element', layout)

# ------ Event Loop ------
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break

window.close()
