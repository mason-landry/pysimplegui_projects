import PySimpleGUI as sg
from common import check_RPS_winner
import random

sg.theme("SystemDefault")
# Setup pySimpleGUI Window
layout = [[sg.Text('Simple game of rock, paper, scissors. Choose your weapon:')],
          [sg.Button('Rock')],
          [sg.Button('Paper')],
          [sg.Button('Scissors')],
          [sg.Output(size=(50,1), key='-OUTPUT-')]]

# Create the Window
window = sg.Window('Rock, Paper, Scissors', layout)
# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    # Randomly choose opponent's choice:
    opponent_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    winner = check_RPS_winner(event, opponent_choice)
    if winner == True:
        message = 'Opponent threw ' +  opponent_choice + '. You win!'
    elif winner == False:
        message = 'Opponent threw ' + opponent_choice + '. You lose!'
    else:
        message = 'Opponent threw ' + opponent_choice + '''. It's a tie!'''
    window['-OUTPUT-'].update(message)
window.close()


