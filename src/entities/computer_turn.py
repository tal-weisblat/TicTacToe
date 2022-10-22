

from game_setting import * 


def computer_turn(board, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9):
    
    time.sleep(0.45)
    i = random.randint(0,8) 
    
    # computer-choice 
    while board[i] != '': i = random.randint(0,8)
     
    # address-board 
    board[i] = 'O' 

    # address gui (with computer choice)
    if i == 0: button_1.button_value = 'O'
    if i == 1: button_2.button_value = 'O'
    if i == 2: button_3.button_value = 'O'
    if i == 3: button_4.button_value = 'O'
    if i == 4: button_5.button_value = 'O'
    if i == 5: button_6.button_value = 'O'
    if i == 6: button_7.button_value = 'O'
    if i == 7: button_8.button_value = 'O'
    if i == 8: button_9.button_value = 'O'
