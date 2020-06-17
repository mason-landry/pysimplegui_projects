import PySimpleGUI as sg
import random

sg.theme("SystemDefault")
# Setup pySimpleGUI Window
operations = [' + ',' - ',' * ',' / ']
layout = [[sg.Text('Simple Calculator: Input numbers and choose operation.')],
          [sg.Text('Press calculate when ready')],

          [sg.Input('', size=(10,1)), sg.Combo(operations, default_value=operations[0]), sg.Input('', size=(10,1))],
          [sg.Button('Calculate'), sg.Button('Reset')],
          [sg.Output(size=(30,1), key='-OUTPUT-')]]

# Create the Window
window = sg.Window('Simple Calculator', layout)
# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    num1 = int(values[0])
    operation = values[1]
    num2 = int(values[2])
    if operation == operations[0]:
        result = num1 + num2
    elif operation == operations[1]:
        result = num1 - num2
    print(result)
    