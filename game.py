

from game_setting import * 

from src.objects.button    import Button
from src.objects.game_over import GameOver 
from src.entities.check_result import check_result
from src.entities.computer_turn import * 
from src.gui.draw_game import * 



# instances 
button_1 = Button(button_1_x,button_123_y) # buttons
button_2 = Button(button_2_x,button_123_y)
button_3 = Button(button_3_x,button_123_y)
button_4 = Button(button_4_x,button_456_y)
button_5 = Button(button_5_x,button_456_y)
button_6 = Button(button_6_x,button_456_y)
button_7 = Button(button_7_x,button_789_y)
button_8 = Button(button_8_x,button_789_y)
button_9 = Button(button_9_x,button_789_y)
gameOver = GameOver(gameOver_text, yes_text, no_text) # game-over 

    

def game():
    
    new_game = False 
    mouse_clicked = False 
    board = ['','','','','','','','','']
    clock = pygame.time.Clock()         
    game_over = False 
    run   = True 

    while run:

        clock.tick(60) 
        for event in pygame.event.get():    
            
            if event.type == GAME_OVER  : game_over = True  
            if event.type == pygame.QUIT: run = False   

            # computer
            if (event.type == COMPUTER_TURN) and (run == True) and (game_over == False):
                computer_turn(board, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9)
                draw_game_board(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9)
                check_result(board,'computer')

            # human 
            if (event.type == BUTTON_1_X) and (mouse_clicked == False):
                mouse_clicked = True
                board[0] = 'X'
                check_result(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))           
            if (event.type == BUTTON_2_X) and (mouse_clicked == False):  
                mouse_clicked = True
                board[1] = 'X'
                check_result(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))
            if (event.type == BUTTON_3_X) and (mouse_clicked == False): 
                mouse_clicked = True
                board[2] = 'X'
                check_result(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))
            if (event.type == BUTTON_4_X) and (mouse_clicked == False): 
                mouse_clicked = True
                board[3] = 'X'
                check_result(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))
            if (event.type == BUTTON_5_X) and (mouse_clicked == False): 
                mouse_clicked = True
                board[4] = 'X'
                check_result(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))
            if (event.type == BUTTON_6_X) and (mouse_clicked == False): 
                mouse_clicked = True
                board[5] = 'X'
                check_result(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))
            if (event.type == BUTTON_7_X) and (mouse_clicked == False): 
                mouse_clicked = True
                board[6] = 'X'
                check_result(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))
            if (event.type == BUTTON_8_X) and (mouse_clicked == False): 
                mouse_clicked = True
                board[7] = 'X'
                check_result(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))
            if (event.type == BUTTON_9_X) and (mouse_clicked == False): 
                mouse_clicked = True
                board[8] = 'X'
                check_result(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))


        # button clicked 
        if not game_over:
            pos = pygame.mouse.get_pos()
            button_1.human_pressed(pos, BUTTON_1_X)
            button_2.human_pressed(pos, BUTTON_2_X)
            button_3.human_pressed(pos, BUTTON_3_X)
            button_4.human_pressed(pos, BUTTON_4_X)
            button_5.human_pressed(pos, BUTTON_5_X)
            button_6.human_pressed(pos, BUTTON_6_X)
            button_7.human_pressed(pos, BUTTON_7_X)
            button_8.human_pressed(pos, BUTTON_8_X)
            button_9.human_pressed(pos, BUTTON_9_X)
            
        # init mouse 
        if (pygame.mouse.get_pressed()[0] == 0): mouse_clicked = False 

        # game-over
        if game_over: 
            button_1.button_value = 'empty'  # init buttons
            button_2.button_value = 'empty'
            button_3.button_value = 'empty'
            button_4.button_value = 'empty'
            button_5.button_value = 'empty'
            button_6.button_value = 'empty'
            button_7.button_value = 'empty'
            button_8.button_value = 'empty'
            button_9.button_value = 'empty'
            gameOver.draw()
            
            # yes-no
            pos = pygame.mouse.get_pos()
            new_game = gameOver.start_new_game(pos, mouse_clicked)
            if new_game != 'not-decided': 
                if new_game: 
                    game()
                    break   # for recursion purposes 
                else: break
            continue

        draw_game_board(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9)

    
if __name__ == '__main__':
    game()






