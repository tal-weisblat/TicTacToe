
from game_setting import * 


# -------------------------------------- GAME-OVER ------------------------------------------
class GameOver():

    def __init__(self, gameOver_text, yes_text, no_text, GAP=20): 
        self.gameOver_text = gameOver_text
        self.yes_text      = yes_text 
        self.no_text       = no_text 
        game_over_text_width  = self.gameOver_text.get_width()
        game_over_text_height = self.gameOver_text.get_height()
        self.game_over_text_x = WIN_WIDTH/2  - game_over_text_width/2
        self.game_over_text_y = WIN_HEIGHT/2 - game_over_text_height/2 
        yes_width  = self.yes_text.get_width()
        no_width   = self.no_text.get_width()
        LEFT_RIGHT_GAP = (game_over_text_width - (yes_width + GAP + no_width))/2 

        # yes 
        yes_x = self.game_over_text_x + LEFT_RIGHT_GAP
        yes_y = self.game_over_text_y + game_over_text_height + GAP
        self.yes_rect = self.yes_text.get_rect() 
        self.yes_rect.topleft = (yes_x,yes_y)

        # no 
        no_x = self.game_over_text_x + LEFT_RIGHT_GAP + yes_width + GAP 
        no_y = self.game_over_text_y + game_over_text_height + GAP 
        self.no_rect = self.no_text.get_rect()
        self.no_rect.topleft = (no_x, no_y)

    def draw(self):
        WIN.fill(CHOCOLATE)
        WIN.blit(self.gameOver_text, (self.game_over_text_x,self.game_over_text_y))
        WIN.blit(self.yes_text, self.yes_rect.topleft)
        WIN.blit(self.no_text,  self.no_rect.topleft)
        pygame.display.update()

    def start_new_game(self, pos, mouse_clicked): 
        
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

            


