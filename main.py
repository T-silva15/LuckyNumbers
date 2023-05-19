import os  
from desc import showDescription
from game import *

# window configuration
def showMenu():
    # menu creation
    os.system('cls')
    print("| / / / / / / / / / / Lucky Numbers / / / / / / / / / / |")
    print("| / / / / / / / / / /      MENU     / / / / / / / / / / |")
    print("|                                                       |")
    print("| 1. Iniciar uma partida                                |")
    print("| 2. Carregar uma partida a partir de um ficheiro       |")     
    print("| 3. Descrição do jogo                                  |") 
    print("| 4. Sair                                               |")
    print("|                                                       |")
    print("| / / / / / / / / / / / / / / / / / / / / / / / / / / / |")
    print("| / / / / / / / / / / / / / / / / / / / / / / / / / / / |")
    print("Introduza a sua opção: ")
    op = int(input())
    
    # check if user input is an acceptable answer
    while op <= 0 or op >= 5:
        os.system('cls')
        print("Opção Inválida! Escolha novamente: ")
        op = int(input()) 
    
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