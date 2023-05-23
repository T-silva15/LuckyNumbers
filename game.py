import os
import random
import time
from player import *

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
def coinflip():
    print("Quem começará o jogo?")
    time.sleep(1)
    # create random number between 0 and 1
    coin = random.randint(0,1)
    # if the number is 0 player starts (return 0), if not the first one to play is the bot (return 1)
    if coin == 0:
        print("O jogador", Player, "é o primeiro a jogar!\n")
        return 0
    else:
        print("O bot é o primeiro a jogar!\n")
        return 1
        
# function that gives the player a random clover from the stack
def giveClover(stack):
    # loops until an accetpable clover is drawn (clover )
    while True:
        pastIndex = []
        indClover = random.randint(0,39)
        # if clover hasn't been drawn before adds it to the list of drawn clovers and breaks out of the loop
        if indClover not in pastIndex:
            pastIndex.append(indClover)
            break
    # tells the user the clover that was drawn
    print("O trevo que saiu foi ", stack[indClover])

# asks player name
def playername():
    # ask player name
    os.system('cls')
    player_name = input("Digite o nome do jogador: ")
    player = Player(player_name)
    board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
# functions that runs main game
def runGame(player1, player2):
    # Board creation 
    stack = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20]
    table = []  

    #--------------------playername()
# decide who starts
    os.system('cls')
    dec = coinflip()
    input("Pressione uma tecla para continuar...")
    # player starts
    if dec == 0:
        # Loop that ends when any of the boards is full
        while True:
            # Displaying both boards
            os.system('cls') 
            print("Tabuleiro do ", player1.name, ": \n")
            showBoard(player1.board)
            input("Pressione uma tecla para continuar...")
            os.system('cls')
            print("Tabuleiro do Bot: \n")
            showBoard(player2.board)
            input("Pressione uma tecla para continuar...")
            
            # Check if all entries are different from zero
            if all(value != 0 for value in player1.board):
                print("O Jogador é o Vencedor!")
                break
            elif all(value != 0 for value in player2.board):
                print("O Bot é o Vencedor!")
                break
            # Incrementing a list temporarily to avoid infinite loops
            player2.board = [value + 1 for value in player2.board]  
    # bot starts        
    else:
        # Loop that ends when any of the boards is full
        while True:
            # Displaying both boards
            os.system('cls') 
            print("Tabuleiro do Bot: \n")
            showBoard(player2.board)
            input("Pressione uma tecla para continuar...")
            os.system('cls')
            print("Tabuleiro do Jogador: \n")
            showBoard(player1.board)
            input("Pressione uma tecla para continuar...")
            
            # Check if all entries are different from zero
            if all(value != 0 for value in player1.board) or all(value != 0 for value in player2.board):
                break
            # Incrementing a list temporarily to avoid infinite loops
            player2.board = [value + 1 for value in player2.board]  
