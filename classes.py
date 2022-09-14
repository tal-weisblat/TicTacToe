
import pygame 



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

class Button():

    def __init__(self,x,y):
        self.x = x 
        self.y = y 
        
        self.button = pygame.Rect(self.x,self.y, BUTTON_HEIGHT, BUTTON_WIDTH)
        
        self.buttonSign = 'empty'  # 2 options ; 'X' or 'O'

    def humanPressed(self,pos,event):
        if (self.button.collidepoint(pos)) and (pygame.mouse.get_pressed()[0] == 1):
             self.buttonSign = 'X'
             pygame.event.post(pygame.event.Event(event))
            
    def draw(self,pos):
        
        # empty cell 
        if self.button.collidepoint(pos): 
            pygame.draw.rect(WIN, BROWN, self.button)
        else: 
            pygame.draw.rect(WIN, RED, self.button)


        # draw X or O (or none)
        if self.buttonSign == 'X'  : 
            letter = FONT_X.render('X', 100, BLACK) 
        elif self.buttonSign == 'O': 
            letter = FONT_X.render('O', 100, BLACK) 

        if (self.buttonSign == 'X') or (self.buttonSign == 'O'):
            x = self.button.x + BUTTON_WIDTH/2  - letter.get_width()/2
            y = self.button.y + BUTTON_HEIGHT/2 - letter.get_height()/2
            WIN.blit(letter, (x,y))

