




# TODO :
# add AI-player
# add a new/quit game gui at the end of a game 
# add new FONTS for new/quit-game button + quistion 
# create functionality for both Yes and No buttons
# outline Yes and No buttons at the game-over screen while mouse-cursor hover above 
# improve Tie option 

# BUG : restrict human-player from checking non-empty buttons (at this current version it's possible)




import pygame 
import os 
import random
import time 
pygame.init()


from classes import Button



# COLORS 
WHITE = (255,255,255)  
BLACK = (0,0,0)
RED   = (255,0,0)
CHOCOLATE = (210,105,30)
BROWN = (165,42,42)


# WINDOW  
WIN_WIDTH  = 400     
WIN_HEIGHT = 450  
pygame.display.set_caption('TicTacToe')                            # title 
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))     # game window (width & height)
WIN.fill(WHITE)


# SIZE OF O & X
X_SIZE = 100 
O_SIZE = 100 


# FONT
GAME_OVER_FONT  = pygame.font.SysFont('comicsans', 40) 
YES_NO_FONT     = pygame.font.SysFont('comicsans', 25)
FONT_X = pygame.font.SysFont('comicsans', X_SIZE)
FONT_O = pygame.font.SysFont('comicsans', O_SIZE)

# RENDER
gameOver_text = GAME_OVER_FONT.render('Game over',1, BLACK)    
yes_text      = YES_NO_FONT.render('Yes', 1, BLACK)
no_text       = YES_NO_FONT.render('No',1, BLACK)    



# SOUNDS 
pygame.mixer.music.load(os.path.join('sounds', 'background_music.mp3'))    
pygame.mixer.music.play()
WIN_SOUND   = pygame.mixer.Sound(os.path.join('sounds', 'win_sound.wav'))
LOST_SOUND  = pygame.mixer.Sound(os.path.join('sounds', 'lost_sound.wav'))
CLICK_SOUND = pygame.mixer.Sound(os.path.join('sounds', 'click_sound.mp3')) 



# BUTTON-SETTINGS
BUTTON_WIDTH  = 120
BUTTON_HEIGHT = 120
BUTTONS_GAP   = 5


# BUTTONS-COORDINATES
button_1_x   = (WIN_WIDTH - 3*BUTTON_WIDTH - 2*BUTTONS_GAP)*(0.5)
button_2_x   = button_1_x + BUTTON_WIDTH + BUTTONS_GAP
button_3_x   = button_1_x + 2*BUTTON_WIDTH + 2*BUTTONS_GAP
button_123_y = (WIN_HEIGHT - 3*BUTTON_HEIGHT - 2*BUTTONS_GAP)*(0.5)
button_4_x   = button_1_x
button_5_x   = button_2_x
button_6_x   = button_3_x
button_456_y = button_123_y +  BUTTON_HEIGHT +  BUTTONS_GAP
button_7_x   = button_1_x
button_8_x   = button_2_x
button_9_x   = button_3_x
button_789_y = button_123_y + 2*BUTTON_HEIGHT + 2*BUTTONS_GAP


# BUTTONS
button_1 = Button(button_1_x,button_123_y)
button_2 = Button(button_2_x,button_123_y)
button_3 = Button(button_3_x,button_123_y)
button_4 = Button(button_4_x,button_456_y)
button_5 = Button(button_5_x,button_456_y)
button_6 = Button(button_6_x,button_456_y)
button_7 = Button(button_7_x,button_789_y)
button_8 = Button(button_8_x,button_789_y)
button_9 = Button(button_9_x,button_789_y)


# EVENTS (two for each button)
BUTTON_1_X = pygame.USEREVENT + 1
BUTTON_2_X = pygame.USEREVENT + 2
BUTTON_3_X = pygame.USEREVENT + 3
BUTTON_4_X = pygame.USEREVENT + 4
BUTTON_5_X = pygame.USEREVENT + 5
BUTTON_6_X = pygame.USEREVENT + 6
BUTTON_7_X = pygame.USEREVENT + 7
BUTTON_8_X = pygame.USEREVENT + 8
BUTTON_9_X = pygame.USEREVENT + 9
GAME_OVER  = pygame.USEREVENT + 10
COMPUTER_TURN = pygame.USEREVENT + 11 



# DRAW ALL 
def draw_game_board():
    WIN.fill(WHITE)
    pos = pygame.mouse.get_pos()
    button_1.draw(pos)
    button_2.draw(pos)
    button_3.draw(pos)
    button_4.draw(pos)
    button_5.draw(pos)
    button_6.draw(pos)
    button_7.draw(pos)
    button_8.draw(pos)
    button_9.draw(pos)
    pygame.display.update()



def check_results(board, player): 
    if  (((board[0] == board[1] == board[2]) and (board[2] != '')) or\
         ((board[3] == board[4] == board[5]) and (board[5] != '')) or\
         ((board[6] == board[7] == board[8]) and (board[8] != ''))):
            
            if player == 'human'     : WIN_SOUND.play() 
            elif player == 'computer': LOST_SOUND.play()
            time.sleep(1)
            pygame.event.post(pygame.event.Event(GAME_OVER))

    elif ((board[0] == board[3] == board[6]) and (board[6] != '')) or\
         ((board[1] == board[4] == board[7]) and (board[7] != '')) or\
         ((board[2] == board[5] == board[8]) and (board[8] != '')):
            
            if player == 'human'   : WIN_SOUND.play() 
            elif player == 'computer': LOST_SOUND.play() 
            time.sleep(1)
            pygame.event.post(pygame.event.Event(GAME_OVER))

    elif ((board[0] == board[4] == board[8]) and (board[8] != '')) or\
         ((board[2] == board[4] == board[6]) and (board[6] != '')):
            
            if player == 'human'   : WIN_SOUND.play() 
            elif player == 'computer': LOST_SOUND.play()
            time.sleep(1)
            pygame.event.post(pygame.event.Event(GAME_OVER))

    # TIE:
    elif ( (board[0] != '') and (board[1] != '') and (board[2] != '') and
           (board[3] != '') and (board[4] != '') and (board[5] != '') and
           (board[6] != '') and (board[7] != '') and (board[8] != '')) :   
            
            print('TIE')
            pygame.event.post(pygame.event.Event(GAME_OVER))

    


def computer_turn(board):
    
    time.sleep(0.45)

    # computer-choice 
    i = random.randint(0,8)
    while board[i] != '': i = random.randint(0,8)
    
    # address-board 
    board[i] = 'O' 

    # address gui (with computer choice)
    if i == 0: button_1.buttonSign = 'O'
    if i == 1: button_2.buttonSign = 'O'
    if i == 2: button_3.buttonSign = 'O'
    if i == 3: button_4.buttonSign = 'O'
    if i == 4: button_5.buttonSign = 'O'
    if i == 5: button_6.buttonSign = 'O'
    if i == 6: button_7.buttonSign = 'O'
    if i == 7: button_8.buttonSign = 'O'
    if i == 8: button_9.buttonSign = 'O'
    
    


def initiate_buttons():
    button_1.buttonSign = None
    button_2.buttonSign = None
    button_3.buttonSign = None
    button_4.buttonSign = None
    button_5.buttonSign = None
    button_6.buttonSign = None
    button_7.buttonSign = None
    button_8.buttonSign = None
    button_9.buttonSign = None






def game():
    
    mouse_clicked = False 
    board = ['','','','','','','','','']
    clock = pygame.time.Clock()         
    game_over = False 
    run   = True 



    while run:

        clock.tick(60) 
        for event in pygame.event.get():    
            

            # GAME-OVER
            if (event.type == GAME_OVER): game_over = True  

            # QUIT-GAME
            if event.type == pygame.QUIT: run = False   


            # COMPUTER-TURN 
            if (event.type == COMPUTER_TURN) and (run == True) and (game_over == False):
                computer_turn(board)
                draw_game_board()
                check_results(board,'computer')


            # HUMAN-CLICKED-BUTTONS 
            if (event.type == BUTTON_1_X) and (mouse_clicked == False):
                
                print('button_1 pressed')
                CLICK_SOUND.play()
                mouse_clicked = True
                board[0] = 'X'
                check_results(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))
                
            if (event.type == BUTTON_2_X) and (mouse_clicked == False):  
                CLICK_SOUND.play()
                mouse_clicked = True
                board[1] = 'X'
                check_results(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))

            if (event.type == BUTTON_3_X) and (mouse_clicked == False): 
                CLICK_SOUND.play()
                mouse_clicked = True
                board[2] = 'X'
                check_results(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))

            if (event.type == BUTTON_4_X) and (mouse_clicked == False): 
                CLICK_SOUND.play()
                mouse_clicked = True
                board[3] = 'X'
                check_results(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))

            if (event.type == BUTTON_5_X) and (mouse_clicked == False): 
                CLICK_SOUND.play()
                mouse_clicked = True
                board[4] = 'X'
                check_results(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))

            if (event.type == BUTTON_6_X) and (mouse_clicked == False): 
                CLICK_SOUND.play()
                mouse_clicked = True
                board[5] = 'X'
                check_results(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))

            if (event.type == BUTTON_7_X) and (mouse_clicked == False): 
                CLICK_SOUND.play()
                mouse_clicked = True
                board[6] = 'X'
                check_results(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))

            if (event.type == BUTTON_8_X) and (mouse_clicked == False): 
                CLICK_SOUND.play()
                mouse_clicked = True
                board[7] = 'X'
                check_results(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))

            if (event.type == BUTTON_9_X) and (mouse_clicked == False): 
                CLICK_SOUND.play()
                mouse_clicked = True
                board[8] = 'X'
                check_results(board,'human')
                pygame.event.post(pygame.event.Event(COMPUTER_TURN))

            
        # BUTTON-ClICKED
        pos = pygame.mouse.get_pos()
        button_1.humanPressed(pos, BUTTON_1_X)
        button_2.humanPressed(pos, BUTTON_2_X)
        button_3.humanPressed(pos, BUTTON_3_X)
        button_4.humanPressed(pos, BUTTON_4_X)
        button_5.humanPressed(pos, BUTTON_5_X)
        button_6.humanPressed(pos, BUTTON_6_X)
        button_7.humanPressed(pos, BUTTON_7_X)
        button_8.humanPressed(pos, BUTTON_8_X)
        button_9.humanPressed(pos, BUTTON_9_X)
        if (pygame.mouse.get_pressed()[0] == 0): mouse_clicked = False 
        


        if game_over: 
            GAP = 20
            
            # for gameOver_text
            gameOverText_width  = gameOver_text.get_width()
            gameOverText_height = gameOver_text.get_height()
            gameOver_text_x = WIN_WIDTH/2  - gameOverText_width/2
            gameOver_text_y = WIN_HEIGHT/2 - gameOverText_height/2 

            yes_width  = yes_text.get_width()
            no_width   = no_text.get_width()

            LEFT_RIGHT_GAP = (gameOverText_width - (yes_width + GAP + no_width))/2 

            # yes 
            yes_x = gameOver_text_x + LEFT_RIGHT_GAP
            yes_y = gameOver_text_y + gameOverText_height + GAP
            yes_rect = yes_text.get_rect() 
            yes_rect.topleft = (yes_x,yes_y)

            # no 
            no_x = gameOver_text_x + LEFT_RIGHT_GAP + yes_width + GAP 
            no_y = gameOver_text_y + gameOverText_height + GAP 
            no_rect = no_text.get_rect()
            no_rect.topleft = (no_x, no_y)
             

            # EVENTS 
            pos = pygame.mouse.get_pos() 
            if (yes_rect.collidepoint(pos)) and (pygame.mouse.get_pressed()[0] == 1) and (mouse_clicked == False):
                initiate_buttons()
                time.sleep(0.5)
                game()
                run = False     # for recursion purposes 
                break
            
            if (no_rect.collidepoint(pos)) and (pygame.mouse.get_pressed()[0] == 1) and (mouse_clicked == False):
                mouse_clicked = True
                run = False 
                break

            
            WIN.fill(CHOCOLATE)
            WIN.blit(gameOver_text, (gameOver_text_x,gameOver_text_y))
            WIN.blit(yes_text, yes_rect.topleft)
            WIN.blit(no_text, no_rect.topleft)
            
            pygame.display.update()
            continue 


        
        draw_game_board()

    

if __name__ == '__main__':
    game()






