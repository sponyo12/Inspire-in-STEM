from optparse import Values
import PySimpleGUI as sg
import pandas as pd

#add some colour to the window
sg.theme('Darkteal9')

layout = [
    [sg.Text('SIGN UP:')],
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Name',size=(15,1)), sg.InputText(key='Name')],
    [sg.Text('Email',size=(15,1)),sg.InputText(key='Email')],
    [sg.Text('Phone NO',size=(15,1)),sg.InputText(key='Phone NO')],
    [sg.Text('Password',size=(15,1)),sg.InputText(key='Password')],
    [sg.Text('I speak', size=(15,1)),
                            sg.Checkbox('Kiswahili',key='Kiswahili'),
                            sg.Checkbox('English',key='English')],
    [sg.Text('Age ',size=(15,1)), sg.Spin([i for i in range(0,100)])], 
    [sg.Submit(),sg.Exit()],
    [sg.Button('LOG IN:')],
    [sg.Log_in()]
]

window =sg.Window('Simple data entry form',layout)

while True:
    event, values = window.read()
    if event ==sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        sg.popup('Data saved!')
    if event == 'LOG IN:':
        sg.popup(
            
                [sg.Text('Name',size=(15,1)), sg.InputText(key='Name')],
                [sg.Text('Email',size=(15,1)),sg.InputText(key='Email')],
                [sg.Text('Phone NO',size=(15,1)),sg.InputText(key='Phone NO')],
                [sg.Text('password',size=(15,1)),sg.InputText(key='password')],
        )

window.close()        