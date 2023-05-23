import os
import random
import time

# function to show the board of a given player
def showBoard(board):
    rows = 4
    cols = 4

    print("+" + "-" * 13 + "+")  # Print the top border

    for i in range(rows):
        print("|", end=" ")  # Print the left border
        for j in range(cols):
            index = i * cols + j
            print(f"{board[index]:2}", end=" ")
        print("|")  # Print the right border

        if i < rows - 1:
            print("|" + "-" * 13 + "|")  # Print the row divider
    
    print("+" + "-" * 13 + "+")  # Print the bottom border

# function to decide which player starts
def coinflip(player1):
    
    print("Quem começará o jogo?")
    time.sleep(1)
    # create random number between 0 and 1
    coin = random.randint(0,1)
    # if the number is 0 player starts (return 0), if not the first one to play is the bot (return 1)
    if coin == 0:
        print("O jogador", player1, "é o primeiro a jogar!\n")
        return 0
    else:
        print("O BOT é o primeiro a jogar!\n")
        return 1
        
# function that gives the player a random clover from the stack
def gameTurn(board, stack, table):
    dec = 0
    # Asks user for option (loops until acceptable answer)
    while dec < 1 or dec > 2:
        os.system('cls')
        print("1. Tirar um trevo do saco")
        print("2. Escolher um trevo da mesa")
        dec = int(input("Escolha a sua opção: "))
    # Draw a clover from stack and place it
    if dec == 1:
        # loops until an accetpable clover is drawn
        while True:
            pastIndex = []
            indClover = random.randint(0,39)
            # if clover hasn't been drawn before adds it to the list of drawn clovers and breaks out of the loop
            if indClover not in pastIndex:
                pastIndex.append(indClover)
                break
        dec = 0
        while dec < 1 or dec > 2:
            os.system('cls')
            # tells the user the clover that was drawn
            print("O trevo retirado foi um", stack[indClover],"!\n")
            print("1. Colocar o trevo no tabuleiro")
            print("2. Colocar o trevo na mesa ")
            dec = int(input("Escolha a sua opção: "))
            
        if dec == 1:
            os.system('cls')
            showBoard(board)
            input("Pressione uma tecla para continuar...")
            os.system('cls')
            print("+-----------------+")
            print("|  1   2   3   4  |")    
            print("|-----------------|")
            print("|  5   6   7   8  |")    
            print("|-----------------|")
            print("|  9  10  11   12 |")    
            print("|-----------------|")
            print("|  13  14  15  16 |")    
            print("|-----------------|")
            pos = int(input("Indique a posição no tabuleiro que pretende colocar o trevo(1-16): "))
            board[pos-1] = stack[indClover]
        else:
            os.system('cls')
            print("Trevo adicionado à stack!")
            table.append(stack[indClover])
    # draw clover from table and place it
    else:
        os.system('cls')
        print("A mesa possui os seguintes trevos: ", stack)
        print("Qual dos trevos pretende colocar na mesa")
    
    
# functions that runs main game
def runGame(player1, player2, board1, board2):    
    # Board creation 
    stack = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20]
    table = []  

# decide who starts
    os.system('cls')
    dec = coinflip(player1)
    input("Pressione uma tecla para continuar...")
    # player starts
    if dec == 0:
        # Loop that ends when any of the boards is full
        while True:
            # Displaying both boards
            os.system('cls') 
            print("Tabuleiro do", player1, ": \n")
            showBoard(board1)
            input("Pressione uma tecla para continuar...")
            os.system('cls')
            print("Tabuleiro do Bot: \n")
            showBoard(board2)
            input("Pressione uma tecla para continuar...")
            
            # Check if all entries are different from zero
            if all(value != 0 for value in board1):
                print("O Jogador é o Vencedor!")
                break
            elif all(value != 0 for value in board2):
                print("O Bot é o Vencedor!")
                break
            # Incrementing a list temporarily to avoid infinite loops
            board2 = [value + 1 for value in board2]  
    # bot starts        
    else:
        # Loop that ends when any of the boards is full
        while True:
            # Displaying both boards
            os.system('cls') 
            print("Tabuleiro do Bot: \n")
            showBoard(board2)
            input("Pressione uma tecla para continuar...")
            os.system('cls')
            print("Tabuleiro do", player1, ": \n")
            showBoard(board1)
            input("Pressione uma tecla para continuar...")
            
            # Check if all entries are different from zero
            if all(value != 0 for value in board1) or all(value != 0 for value in board2):
                break
            # Incrementing a list temporarily to avoid infinite loops
            board2 = [value + 1 for value in board2]  
