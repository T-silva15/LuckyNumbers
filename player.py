import os

# for player
class Player:
    def __init__(self, name):
        self.name = name

# asks player name
def playername():
    # ask player name
    os.system('cls')
    player_name = input("Digite o nome do jogador: ")
    player = Player(player_name)