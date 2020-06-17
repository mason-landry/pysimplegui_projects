'''Common functions and classes for simple rock paper scissors game using pySimpleGUI'''

def check_RPS_winner(player_choice, opponent_choice):
    # Logic for determining winner:
    if player_choice == 'Rock':
        if opponent_choice == 'Scissors':
            return True
        elif opponent_choice == 'Paper':
            return False
        else:
            return None
    
    elif player_choice == 'Scissors':
        if opponent_choice == 'Paper':
            return True
        elif opponent_choice == 'Rock':
            return False
        else:
            return None
    
    elif player_choice == 'Paper':
        if opponent_choice == 'Rock':
            return True
        elif opponent_choice == 'Scissors':
            return False
        else:
            return None