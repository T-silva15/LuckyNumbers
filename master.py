import os
import sys  
import random
from desc import showDescription

# window configuration
def showMenu():
    print("/ / / / / / / / Lucky Numbers / / / / / / / /")
    print("/ / / / / / / /     MENU      / / / / / / / /")
    print("1. Iniciar uma partida")
    print("2. Carregar uma partida a partir de um ficheiro")
    print("3. Descrição do jogo")
    print("4. Sair")
    print("Introduza a sua opção: \n")
    op = int(input())

    while op <= 0 or op >= 5:
        os.system('cls')
        print("Opção Inválida! Escolha novamente: ")
        op = int(input()) 
    
    if op == 1:
        os.system('exit')
    elif op == 2:
        os.system('exit')
    elif op == 3:
        showDescription()
        showMenu()
    elif op == 4:
        os.system('exit')
        
showMenu()