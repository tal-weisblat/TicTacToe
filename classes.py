
import pygame 
import time 
import os 

# WINDOW  
WIN_WIDTH  = 400     
WIN_HEIGHT = 450  
pygame.display.set_caption('TicTacToe')                            # title 
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))     # game window (width & height)
#WIN.fill(WHITE)

# COLORS 
WHITE = (255,255,255)  
BLACK = (0,0,0)
RED   = (255,0,0)
CHOCOLATE = (210,105,30)
BROWN = (165,42,42)


BUTTON_WIDTH  = 120
BUTTON_HEIGHT = 120

X_SIZE = 100 
O_SIZE = 100 

FONT_X = pygame.font.SysFont('comicsans', X_SIZE)
FONT_O = pygame.font.SysFont('comicsans', O_SIZE)


CLICK_SOUND = pygame.mixer.Sound(os.path.join('sounds', 'click_sound.mp3')) 

# --------------------------------------- BUTTON --------------------------------------------

class Button():

    def __init__(self,x,y):
        self.x = x 
        self.y = y 
        
        self.button = pygame.Rect(self.x,self.y, BUTTON_HEIGHT, BUTTON_WIDTH)
        
        self.buttonValue = 'empty'  # 2 options ; 'X' or 'O'



    def humanPressed(self,pos,event):
        if (self.button.collidepoint(pos)) and (pygame.mouse.get_pressed()[0] == 1) and (self.buttonValue == 'empty'):
            self.buttonValue = 'X'
            CLICK_SOUND.play()
            pygame.event.post(pygame.event.Event(event))



    def draw(self,pos):
        
        # empty cell 
        if self.button.collidepoint(pos): 
            pygame.draw.rect(WIN, BROWN, self.button)
        else: 
            pygame.draw.rect(WIN, RED, self.button)


        # draw X or O (or none)
        if self.buttonValue == 'X'  : 
            letter = FONT_X.render('X', 100, BLACK) 
        elif self.buttonValue == 'O': 
            letter = FONT_X.render('O', 100, BLACK) 

        if (self.buttonValue == 'X') or (self.buttonValue == 'O'):
            x = self.button.x + BUTTON_WIDTH/2  - letter.get_width()/2
            y = self.button.y + BUTTON_HEIGHT/2 - letter.get_height()/2
            WIN.blit(letter, (x,y))





# -------------------------------------- GAME-OVER ------------------------------------------
class GameOver():

    
    def __init__(self, gameOver_text, yes_text, no_text, GAP=20): 

        self.gameOver_text = gameOver_text
        self.yes_text      = yes_text 
        self.no_text       = no_text 

        
        # for gameOver_text
        gameOverText_width  = self.gameOver_text.get_width()
        gameOverText_height = self.gameOver_text.get_height()
        self.gameOver_text_x = WIN_WIDTH/2  - gameOverText_width/2
        self.gameOver_text_y = WIN_HEIGHT/2 - gameOverText_height/2 

        yes_width  = self.yes_text.get_width()
        no_width   = self.no_text.get_width()

        LEFT_RIGHT_GAP = (gameOverText_width - (yes_width + GAP + no_width))/2 

        # yes 
        yes_x = self.gameOver_text_x + LEFT_RIGHT_GAP
        yes_y = self.gameOver_text_y + gameOverText_height + GAP
        self.yes_rect = self.yes_text.get_rect() 
        self.yes_rect.topleft = (yes_x,yes_y)

        # no 
        no_x = self.gameOver_text_x + LEFT_RIGHT_GAP + yes_width + GAP 
        no_y = self.gameOver_text_y + gameOverText_height + GAP 
        self.no_rect = self.no_text.get_rect()
        self.no_rect.topleft = (no_x, no_y)
    

    def draw(self):
        WIN.fill(CHOCOLATE)
        WIN.blit(self.gameOver_text, (self.gameOver_text_x,self.gameOver_text_y))
        WIN.blit(self.yes_text, self.yes_rect.topleft)
        WIN.blit(self.no_text,  self.no_rect.topleft)
        pygame.display.update()


    def NewGame(self, pos, mouse_clicked): 
        
        
        if (self.yes_rect.collidepoint(pos)) and (pygame.mouse.get_pressed()[0] == 1) and (mouse_clicked == False):
            pygame.event.clear()   # clear all events from queue 
            time.sleep(0.5)
            new_game = True 
            return (new_game)
        
        elif (self.no_rect.collidepoint(pos)) and (pygame.mouse.get_pressed()[0] == 1) and (mouse_clicked == False):
            mouse_clicked = True
            new_game = False 
            return (new_game)
        else:
            return 'not-decided'

            


