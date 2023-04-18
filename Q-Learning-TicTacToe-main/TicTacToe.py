import numpy as np

class TicTacToe:
    
    
    def __init__(self):
        self.current_state = np.zeros(9, dtype = np.int8)
        self.winner = None
        self.player = 1  
        
    
    def get_current_game(self):
        return self.current_state
    
    def get_current_game_tuple(self):
        return tuple(self.current_state)

    def get_available_positions(self):
        return(np.argwhere(self.current_state==0).ravel()) 
        # [0, 1, 3, 6, 8]

    def reset_game(self):
        self.current_state = np.zeros(9, dtype = np.int8)
        self.player = 1

    def get_player(self):
        return self.player

    """
     Aksiyon gerçekleştirilir
    """
    def make_move(self, action): # x==1 , o==-1
        if action in self.get_available_positions():
            self.current_state[action] = self.player
            self.player *= -1
        else:
            print('Mevcut değil')
     
    
    def is_winner(self, isgame = False):
        winner_coordinates = np.array([[0,1,2], [3, 4, 5], [6, 7, 8],
                                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                                [0, 4, 8], [2, 4, 6]])
        for coordinate in winner_coordinates:
            total = sum(self.current_state[coordinate])
            if total == 3: # X kazandı
                self.winner = 1
                self.reset_game()
                return 1
            elif total == -3: # O kazandı
                self.winner = -1
                self.reset_game()
                return -1
            elif sum(self.current_state == 1) == 5: # berabere
                self.winner = -2
                self.reset_game()
                return -2
        return False
