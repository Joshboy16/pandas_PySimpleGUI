import PySimpleGUI as sg
import pandas as pd


sg.theme('DarkBrown5')

EXCEL_FILE = 'data_entry1.xlsx'
df = pd.read_excel(EXCEL_FILE)


layout = [
    [sg.Text('Please fill out the following fields')],
    [sg.Text('Name', size=(15,1)),sg.InputText(key='Name')],
    [sg.Text('City', size=(15,1)),sg.InputText(key='City')],
    [sg.Text('Favourite Color', size=(15,1)), sg.Combo(['Green', 'Blue', 'Red'], key='Favourite Color')],
    [sg.Text('I speak', size=(15,1)),
                            sg.Checkbox('German', key='German'),
                            sg.Checkbox('Spanish', key='Spanish'),
                            sg.Checkbox('English', key='English')],
    [sg.Text('No. of children', size=(15,1)), sg.Spin([i for i in range(0,16)],
                                                    initial_value=0, key='Children')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()],
]

window = sg.Window('Simple data entry form', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved')
        clear_input()
window.close()

