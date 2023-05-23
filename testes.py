import random
from main import showBoard




stack = [0,0,0,0,0]
indClover = 1
dec = 0

while dec < 1 or dec > 2:
    # tells the user the clover that was drawn
    print("O trevo retirado foi um", stack[indClover],"!\n")
    print("1. Colocar o trevo no tabuleiro")
    print("2. Colocar o trevo na mesa ")
    dec = int(input("Escolha a sua opção: "))
