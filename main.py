import os
from desc import showDescription
import time
import colorama
from game import *

# colored text
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

# game name and creators
def showpage():
    os.system('cls')
    # LuckyNumbers logo in AXCII
    print(f"{Fore.GREEN}\n ___      __   __  _______  ___   _  __   __    __    _  __   __  __   __  _______  _______  ______    _______ \n|   |    |  | |  ||       ||   | | ||  | |  |  |  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |  |       |\n|   |    |  | |  ||       ||   |_| ||  |_|  |  |   |_| ||  | |  ||       || |_|   ||    ___||   | ||  |  _____|\n|   |    |  |_|  ||       ||      _||       |  |       ||  |_|  ||       ||       ||   |___ |   |_||_ | |_____ \n|   |___ |       ||      _||     |_ |_     _|  |  _    ||       ||       ||  _   | |    ___||    __  ||_____  |\n|       ||       ||     |_ |    _  |  |   |    | | |   ||       || ||_|| || |_|   ||   |___ |   |  | | _____| |\n|_______||_______||_______||___| |_|  |___|    |_|  |__||_______||_|   |_||_______||_______||___|  |_||_______|")
    # authors of the game
    print(f"\n-------------------------------------{Back.WHITE}{Fore.BLACK}Jogo de: Filipe Nunes e Tiago Isidro{Back.RESET}{Fore.RESET}-------------------------------------")
    input("\nPressione uma tecla para avançar...")

# window configuration
def showMenu():
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
    print("\nIntroduza uma opção: ")
    op = int(input())

    # check if user input is an acceptable answer
    while op <= 0 or op >= 5:
        os.system('cls')
        print("Oops... Opção inválida!")
        time.sleep(1)
        input("\nPressione uma tecla para voltar...")
        showMenu()
       
    # runs program based on the user's input
    if op == 1:
        runGame()
        showMenu()
    elif op == 2:
        os.system('exit')
    elif op == 3:
        showDescription()
        showMenu()
    elif op == 4:
        os.system('cls')
        print("Sessão Terminada!")
        os.system('exit')


# calling function to start LuckyNumbers 
showpage()
showMenu()