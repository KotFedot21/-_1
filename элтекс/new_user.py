import PySimpleGUI as sg
sg.theme('Reddit') 
userID = [ 69, 12, 123]
layout = [
    [sg.Text('Please enter your ID')],
    [sg.Text('ID', size=(15, 1)), sg.InputText()],
    [sg.OK()]
    ]
window = sg.Window('New User', layout)
event, values = window.read()
window.close()

userID.append(values[0])
print (userID)

#ee
