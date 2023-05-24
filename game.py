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
    os.system('cls')
    print("Quem começará o jogo?")
    time.sleep(1)
    # create random number between 0 and 1
    coin = random.randint(0,1)
    # if the number is 0 player starts (return 0), if not the first one to play is the bot (return 1)
    if coin == 0:
        print("O jogador", player1, "é o primeiro a jogar!\n")
    else:
        print("O BOT é o primeiro a jogar!\n")
    return coin

# function that runs if a player decides to draw a clover from the sack and place it on the board/table 
def boardPlay(board, stack, table, clover):
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
    pos = (int(input("Indique a posição no tabuleiro que pretende colocar o trevo(1-16): ")) - 1)
    # check if position is occupied / if it is, switch clovers and send old clover to table
    if board[pos] != 0:
        if checkPlacement(board, pos, clover, stack) == True:
            table.append(board[pos])        # send clover to table
            board[pos] = stack[clover]      # put clover on square chosen
        else:
            os.system('cls')
            print("O trevo não pode ser colocado nesse quadrado!")
            print("A reiniciar jogada...")
            time.sleep(5)
            boardPlay(board, stack, table, clover)
    else: 
        if checkPlacement(board, pos, clover, stack) == True:
            board[pos] = stack[clover]       # put clover on square chosen
        else:
            os.system('cls')
            print("O trevo não pode ser colocado nesse quadrado!")
            print("A reiniciar jogada...")
            time.sleep(5)
            boardPlay(board, stack, table, clover)

# function that gives the player a random clover from the stack
def gameTurn(player, board, stack, table):
    dec = 0
    # Asks user for option (loops until acceptable answer)
    while dec < 1 or dec > 2:
        os.system('cls')
        print("Turno do", player, "!")
        print("1. Tirar um trevo do saco")
        print("2. Escolher um trevo da mesa")
        dec = int(input("Escolha a sua opção: "))
    # Draw a clover from stack and place it
    if dec == 1:
        # loops until an accetpable clover is drawn
        while True:
            pastIndex = []
            # draws random clover from the sack
            indClover = random.randint(0,39)
            # if clover hasn't been drawn before adds it to the list of drawn clovers and breaks out of the loop
            if indClover not in pastIndex:
                pastIndex.append(indClover)
                break
        dec = 0
        while dec < 1 or dec > 2:
            os.system('cls')
            # tells the user what clover was drawn
            print("O trevo retirado foi um", stack[indClover],"!\n")
            # prompts the options
            print("1. Colocar o trevo no tabuleiro")
            print("2. Colocar o trevo na mesa ")
            dec = int(input("Escolha a sua opção: "))
            # places on board/play
        if dec == 1:
            boardPlay(board, stack, table, indClover)
        else:
            os.system('cls')
            print("Trevo adicionado à stack!")
            table.append(stack[indClover])
    # draw clover from table and place it
    else:
        # checks if table has any clovers, if it does not, forces player to draw from sack
        if len(table) != 0:
            os.system('cls')
            print("A mesa possui os seguintes trevos: ", stack)
            print("Qual dos trevos pretende colocar na mesa")
        else:
            os.system('cls')
            print("A mesa não possui nenhum trevo!")
            print("O trevo será retirado do saco!")
            input("Pressione uma tecla para continuar...")
            boardPlay(board, stack, table, indClover)

# function that checks if player can place clover in specific position
def checkPlacement(board, pos, clover, stack):
    
    if pos >= 0 and pos <= 3:
        # stores previous clover in position
        prevClover = board[pos]
        board[pos] = stack[clover]
        # clover in first row
        lwrNumbers = 3          # 3 clover below
        # clover counter
        lftNumbers = 0
        # counts how many clovers are on the left of the position
        for i in range (4):
            # increment counter
            lftNumbers += 1
            # decrement position
            pos -= 1 
            if pos == 0:
                break
        # calculates how many numbers are on the right of the position
        rgtNumbers = pos - 1 - lftNumbers
        # checks if number is higher that the numbers to its left
        for j in range(pos, pos - lftNumbers, -1):
            if board[j] > board[pos]:
                return False
        # checks if number is lower that the numbers to its right
        for h in range(pos, pos + rgtNumbers, 1):
            if board[h] < board[pos]:
                return False
        # checks if number is higher that the numbers below it     
        for l in range(pos, pos + lwrNumbers * 4, 4):
            if board[l] < board[pos]:
                return False
        return True
    elif pos >= 4 and pos < 7:
        # stores previous clover in position
        prevClover = board[pos]
        board[pos] = stack[clover]
        # clover in second row
        lwrNumbers = 2          # 2 clovers above
        hgrNumbers = 1          # 1 clover below
        # clover counter
        lftNumbers = 0
        # counts how many clovers are on the left of the position
        for i in range (4):
            # increment counter
            lftNumbers += 1
            # decrement position
            pos -= 1 
            if pos == 0:
                break
        # calculates how many numbers are on the right of the position
        rgtNumbers = pos - 1 -lftNumbers
       # checks if number is higher that the numbers to its left
        for j in range(pos, pos - lftNumbers, -1):
            if board[j] > board[pos]:
                return False
        # checks if number is lower that the numbers to its right
        for h in range(pos, pos + rgtNumbers, 1):
            if board[h] < board[pos]:
                return False
        # checks if number is higher that the numbers below it     
        for l in range(pos, pos + lwrNumbers * 4, 4):
            if board[l] < board[pos]:
                return False
        # checks if number is lower that the numbers above it
        for p in range(pos, pos - hgrNumbers * 4, 4):
            if board[p] > board[pos]:
                return False
        return True
    elif pos >= 8 and pos < 11:
        # stores previous clover in position
        prevClover = board[pos]
        board[pos] = stack[clover]
        # clover in third row
        lwrNumbers = 1          # 1 clover above
        hgrNumbers = 2          # 2 clovers below
        # clover counter
        lftNumbers = 0
        # counts how many clovers are on the left of the position
        for i in range (4):
            # increment counter
            lftNumbers += 1
            # decrement position
            pos -= 1 
            if pos == 0:
                break
        # calculates how many numbers are on the right of the position
        rgtNumbers = pos - 1 -lftNumbers
       # checks if number is higher that the numbers to its left
        for j in range(pos, pos - lftNumbers, -1):
            if board[j] > board[pos]:
                return False
        # checks if number is lower that the numbers to its right
        for h in range(pos, pos + rgtNumbers, 1):
            if board[h] < board[pos]:
                return False
        # checks if number is higher that the numbers below it     
        for l in range(pos, pos + lwrNumbers * 4, 4):
            if board[l] < board[pos]:
                return False
        # checks if number is lower that the numbers above it
        for p in range(pos, pos - hgrNumbers * 4, 4):
            if board[p] > board[pos]:
                return False
        return True
    else:
        # stores previous clover in position
        prevClover = board[pos]
        board[pos] = stack[clover]
        # clover in fourth row
        hgrNumbers = 3          # 3 clovers above
        # clover counter
        lftNumbers = 0
        # counts how many clovers are on the left of the position
        for i in range (4):
            # increment counter
            lftNumbers += 1
            # decrement position
            pos -= 1 
            if pos == 0:
                break
        # calculates how many numbers are on the right of the position
        rgtNumbers = pos - 1 - lftNumbers
        # checks if number is higher that the numbers to its left
        for j in range(pos, pos - lftNumbers, -1):
            if board[j] > board[pos]:
                return False
        # checks if number is lower that the numbers to its right
        for h in range(pos, pos + rgtNumbers, 1):
            if board[h] < board[pos]:
                return False
        # checks if number is lower that the numbers above it
        for p in range(pos, pos - hgrNumbers * 4, 4):
            if board[p] > board[pos]:
                return False
        return True
    
# functions that runs main game
def runGame(player1, player2, board1, board2):    
    # Board creation 
    stack = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20]
    table = []  

    # decide who starts
    dec = coinflip(player1)
    input("Pressione uma tecla para continuar...")
    # player starts
    if dec == 0:
        # Loop that ends when any of the boards is full
        while True:
            gameTurn(player1, board1, stack, table)
            gameTurn(player2, board2, stack, table)
            # Check if all entries are different from zero, if they are, player has won!
            if all(value != 0 for value in board1):
                print("O Jogador", player1, "é o Vencedor!")
                break
            # Check if all entries are different from zero, if they are, bot has won!
            elif all(value != 0 for value in board2):
                print("O BOT é o Vencedor!")
                break 
    # bot starts        
    else:
        # Loop that ends when any of the boards is full
        while True:
            # Displaying both boards
            gameTurn(player2, board2, stack, table)
            gameTurn(player1, board1, stack, table)
            # Check if all entries are different from zero, if they are, player has won!
            if all(value != 0 for value in board1):
                print("O Jogador", player1, "é o Vencedor!")
                break
            # Check if all entries are different from zero, if they are, bot has won!
            elif all(value != 0 for value in board2):
                print("O BOT é o Vencedor!")
                break 