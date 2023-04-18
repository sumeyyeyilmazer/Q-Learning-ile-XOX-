from TicTacToe import TicTacToe
from Agent import Agent

game = TicTacToe() #Oyun nesnesi oluşturulur

agent = Agent(game, 'X',discount_factor = 0.6, episode = 100000) #Eğitilecek agent nesnesi oluşturulur

agent.train_brain_byrandom() # Ajanın eğitimi başlatılır

