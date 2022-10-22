
from game_setting import * 


# ----------------------------------------------- DRAW-GAME -------------------------------------------------
def draw_game_board(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9):
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
