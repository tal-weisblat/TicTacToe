

import pygame 
import os 
import random
import time 
pygame.init()


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

# O & X sizes 
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
CLICK_SOUND = pygame.mixer.Sound(os.path.join('resources/sound', 'click.mp3')) 
WIN_SOUND   = pygame.mixer.Sound(os.path.join('resources/sound', 'win.wav'))
LOST_SOUND  = pygame.mixer.Sound(os.path.join('resources/sound', 'lost.wav'))
pygame.mixer.music.load(os.path.join('resources/sound', 'background.mp3'))    
pygame.mixer.music.play()



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

# EVENTS
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
