import os
from desc import showDescription
from game import *
import time

# colored text
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

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
    print("| / / / / / / / / / / / / / / / / / / / / / / / / / / / / |")
    print("Introduza a sua opção: ")
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


# calling function to show game menu
showMenu()