
from game_setting import * 



# ---------------------------------- CHECK-RESULTS --------------------------------------
def check_result(board, player): 
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
            
            pygame.event.post(pygame.event.Event(GAME_OVER))
            

    
