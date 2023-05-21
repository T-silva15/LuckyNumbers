import os
from main import *

# colored text
from colorama import Back, Fore, Style

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

# option game
def newGame():
    os.system('cls')
    print(f"| / / / / / / / / / /{Fore.GREEN}🍀Lucky Numbers🍀{Fore.WHITE}/ / / / / / / / / / |")
    print(f"| / / / / / / / / / /    Novo Jogo    / / / / / / / / / / |")
    print("|                                                         |")
    print(f"| {Fore.RED}1. {Fore.WHITE}Um jogador                                           |")
    print(f"| {Fore.RED}2. {Fore.WHITE}Dois jogadores                                       |")
    print(f"| {Fore.RED}3. {Fore.WHITE}Voltar                                               |")
    print("|                                                         |")
    print("| / / / / / / / / / / / / / / / / / / / / / / / / / / / / |")
    print("\nIntroduza uma opção: ")
    gm = int(input())

    # choices directions
    if gm == 1:
        #runGame()
        #showMenu()
    #-----------elif gm == 2:
        #funcao
   #---------- elif gm == 3:
        showMenu()




newGame()