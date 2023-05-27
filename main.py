import os
from desc import showDescription
import time
import colorama
from game import *

# colored text
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

# game name and creators
def showPage():
    os.system('cls')
    # LuckyNumbers logo in AXCII
    print(f"{Fore.GREEN}\n ___      __   __  _______  ___   _  __   __    __    _  __   __  __   __  _______  _______  ______    _______ \n|   |    |  | |  ||       ||   | | ||  | |  |  |  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |  |       |\n|   |    |  | |  ||       ||   |_| ||  |_|  |  |   |_| ||  | |  ||       || |_|   ||    ___||   | ||  |  _____|\n|   |    |  |_|  ||       ||      _||       |  |       ||  |_|  ||       ||       ||   |___ |   |_||_ | |_____ \n|   |___ |       ||      _||     |_ |_     _|  |  _    ||       ||       ||  _   | |    ___||    __  ||_____  |\n|       ||       ||     |_ |    _  |  |   |    | | |   ||       || ||_|| || |_|   ||   |___ |   |  | | _____| |\n|_______||_______||_______||___| |_|  |___|    |_|  |__||_______||_|   |_||_______||_______||___|  |_||_______|")
    # authors of the game
    print(f"\n{Fore.RED}-------------------------------------{Back.WHITE}{Fore.BLACK}Jogo de: Filipe Nunes e Tiago Isidro{Back.RESET}{Fore.RED}-------------------------------------")
    input("\nPressione uma tecla para avançar...")

# Player initialization
player1 = " "
board1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# create bot 
player2 = " "
board2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def chooseGame():
    os.system('cls')
    while True:         # loops until valid answer
        os.system('cls')
        # asks user for the game he wants to play
        print(f"{Fore.RED}1. {Fore.WHITE} Jogar com dois Jogadores")
        print(f"{Fore.RED}2. {Fore.WHITE} Jogar contra um Bot")
        x = input(f"{Fore.GREEN}Introduza uma opção: ")
        if x in ['1','2']:
            x = int(x)
            break
    return x            # returns user decision
    
# window configuration
def showMenu():
    while True:         # loops until user provides a valid input
        # menu creation
        os.system('cls')
        print(f"| / / / / / / / / / /{Fore.GREEN}🍀Lucky Numbers🍀{Fore.WHITE}/ / / / / / / / / / |")
        print(f"| / / / / / / / / / /       MENU      / / / / / / / / / / |")
        print("|                                                         |")
        print(f"| {Fore.RED}1. {Fore.WHITE}Iniciar uma partida                                  |")
        print(f"| {Fore.RED}2. {Fore.WHITE}Carregar uma partida a partir de um ficheiro         |")
        print(f"| {Fore.RED}3. {Fore.WHITE}Descrição do jogo                                    |")
        print(f"| {Fore.RED}4. {Fore.WHITE}Sair                                                 |")
        print("|                                                         |")
        print("| / / / / / / / / / / / / / / / / / / / / / / / / / / / / |")
        op1 = input("Introduza uma opção: ")
        if op1 in ['1','2','3','4']:
            op = int(op1)
            break  # Break out of the loop if a valid number is input
        
    # runs program based on the user's input
    if op == 1:
        x = chooseGame()
        if x == 1:
            twoPlayerGame(player1, player2, board1, board2)
        else:
            botGame(player1, board1, board2)
            
    elif op == 2:
        os.system('exit')
    elif op == 3:
        showDescription()
        showMenu()
    elif op == 4:
        os.system('cls')
        print(f"{Fore.RED}\nSessão Terminada!\n\n")
        os.system('exit')

# calling function to start LuckyNumbers 
showPage()
showMenu()