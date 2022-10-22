

from game_setting import * 



# --------------------------------------- BUTTON --------------------------------------------
class Button():

    def __init__(self,x,y):
        self.x = x 
        self.y = y 
        self.button = pygame.Rect(self.x,self.y, BUTTON_HEIGHT, BUTTON_WIDTH)
        self.button_value = 'empty'  # 2 options ; 'X' or 'O'

    def human_pressed(self,pos,event):
        if (self.button.collidepoint(pos)) and (pygame.mouse.get_pressed()[0] == 1) and (self.button_value == 'empty'):
            self.button_value = 'X'
            CLICK_SOUND.play()
            pygame.event.post(pygame.event.Event(event))

    def draw(self,pos):
        if self.button.collidepoint(pos): # empty cell 
            pygame.draw.rect(WIN, BROWN, self.button)
        else: 
            pygame.draw.rect(WIN, RED, self.button)

        if self.button_value == 'X': # draw X or O (or none)
            letter = FONT_X.render('X', 100, BLACK) 
        elif self.button_value == 'O': 
            letter = FONT_X.render('O', 100, BLACK) 

        if (self.button_value == 'X') or (self.button_value == 'O'):
            x = self.button.x + BUTTON_WIDTH/2  - letter.get_width()/2
            y = self.button.y + BUTTON_HEIGHT/2 - letter.get_height()/2
            WIN.blit(letter, (x,y))



