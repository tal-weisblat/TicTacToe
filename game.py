

# new version of TikTacToe 


import pygame 
import os 
import time 
pygame.init()



# COLORS 
WHITE = (255,255,255)  
BLACK = (0,0,0)
RED = (255,0,0)


# WINDOW  
WIN_WIDTH  = 400     
WIN_HEIGHT = 450  
pygame.display.set_caption('TicTacToe')                            # title 
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))     # game window (width & height)
WIN.fill(WHITE)


# SOUNDS 
pygame.mixer.music.load(os.path.join('soundfiles', 'background_music.mp3'))    
pygame.mixer.music.play()
WIN_SOUND  = pygame.mixer.Sound(os.path.join('soundfiles', 'win_sound.wav'))
LOST_SOUND = pygame.mixer.Sound(os.path.join('soundfiles', 'lost_sound.wav'))


# FONTS
X_SIZE = 100 
O_SIZE = 100 
FONT_X = pygame.font.SysFont('comicsans', X_SIZE)
FONT_O = pygame.font.SysFont('comicsans', O_SIZE)


# BUTTON-SETTINGS
BUTTON_WIDTH  = 120
BUTTON_HEIGHT = 120
BUTTONS_GAP   = 5



class Button():

    def __init__(self,x,y):
        self.x = x 
        self.y = y 
        self.button = pygame.Rect(self.x,self.y, BUTTON_HEIGHT, BUTTON_WIDTH)
        self.buttonSign = None  # 2 options ; 'X' or 'O'

    def humanPressed(self,pos,event):
        if (self.button.collidepoint(pos)) and (pygame.mouse.get_pressed()[0] == 1):
             self.buttonSign = 'X'
             pygame.event.post(pygame.event.Event(event))
            
    def draw(self):
        # draw empty rect
        pygame.draw.rect(WIN, RED, self.button)
        # draw X or O (or none)
        if self.buttonSign == 'X'  : letter = FONT_X.render('X', 100, BLACK) 
        elif self.buttonSign == 'O': letter = FONT_X.render('O', 100, BLACK) 
        if (self.buttonSign == 'X') or (self.buttonSign == 'O'):
            x = self.button.x + BUTTON_WIDTH/2  - letter.get_width()/2
            y = self.button.y + BUTTON_HEIGHT/2 - letter.get_height()/2
            WIN.blit(letter, (x,y))


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



# DRAW ALL 
def draw():
    button_1.draw()
    button_2.draw()
    button_3.draw()
    button_4.draw()
    button_5.draw()
    button_6.draw()
    button_7.draw()
    button_8.draw()
    button_9.draw()
    pygame.display.update()



def game():

    board = ['','','','','','','','','']
    clock = pygame.time.Clock()         
    run   = True 
    

    while run:

        clock.tick(60) 
        for event in pygame.event.get():    
            
            # QUIT-GAME
            if event.type == pygame.QUIT: run = False   

            # HUMAN-CLICKED-BUTTONS 
            if event.type == BUTTON_1_X: board[0] = 'X'
            if event.type == BUTTON_2_X: board[1] = 'X'
            if event.type == BUTTON_3_X: board[2] = 'X'
            if event.type == BUTTON_4_X: board[3] = 'X'
            if event.type == BUTTON_5_X: board[4] = 'X'
            if event.type == BUTTON_6_X: board[5] = 'X'
            if event.type == BUTTON_7_X: board[6] = 'X'
            if event.type == BUTTON_8_X: board[7] = 'X'
            if event.type == BUTTON_9_X: board[8] = 'X'

            
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
        

        print(board)
        

        # DRAW-ALL 
        draw()




game()




