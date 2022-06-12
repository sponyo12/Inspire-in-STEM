from optparse import Values
import PySimpleGUI as sg
import pandas as pd

#add some colour to the window
sg.theme('Darkteal9')

#EXCEL_FILE='Book1.xlsx'
#df = pd.read_excel(EXCEL_FILE)


layout = [
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Name',size=(15,1)), sg.InputText(key='Name')],
    [sg.Text('Email',size=(15,1)),sg.InputText(key='Email')],
    [sg.Text('Phone NO',size=(15,1)),sg.InputText(key='Phone NO')],
    [sg.Text('I speak', size=(15,1)),
                            sg.Checkbox('Kiswahili',key='Kiswahili'),
                            sg.Checkbox('English',key='English')],
    [sg.Text('Age ',size=(15,1)), sg.Spin([i for i in range(0,100)])], 
    [sg.Submit(),sg.Exit()]
]

window =sg.Window('Simple data entry form',layout)

while True:
    event, values = window.read()
    if event ==sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        #df = df.append(values, ignore_index=True)
        #df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved!')
window.close()        