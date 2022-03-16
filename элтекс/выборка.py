import PySimpleGUI as sg

# import PySimpleGUIQt as sg

"""
 Demo - Multiple layouts in a single window that are swapped in and out
 If you've ever wanted to replace the contents of a window with another layout then perhaps
 this demo is for you. You cannot actually change the layout of a window dynamically, but what
 you can do is make elements visible and invisible. 

 To "swap out" a portion of a window, use a Column element for that portion. Add multiple Columns
 on the same row and make only 1 of them active at a time
"""

# ----------- Create the 3 layouts this Window will display -----------
layout1 = [[sg.Text('This is layout 1 - It is all Checkboxes')],
           *[[sg.CB(f'Checkbox {i}')] for i in range(5)]]# вставляем сюда список состояний


# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(layout1, key='-COL1-')],
          [sg.Button('Cycle Layout'),  sg.Button('Exit')]]

window = sg.Window('Swapping the contents of a window', layout)

layout = 1  # The currently visible layout
while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Cycle Layout':
        window[f'-COL{layout}-'].update(visible=False)
        window[f'-COL{layout}-'].update(visible=True)

window.close()
