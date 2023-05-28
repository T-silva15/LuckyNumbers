import os
import random
import time
import colorama

# colored text
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

# function to show the board of a given player
def showBoard(board, stack):
    rows = 4
    cols = 4
    print(f"{Fore.WHITE}")
    print("+" + "-" * 13 + "+")  # Print the top border

    for i in range(rows):
        print("|", end=" ")  # Print the left border
        for j in range(cols):
            index = i * cols + j
            index1 = board[index]
            print(f"{stack[index1]:2}", end=" ")
        print("|")  # Print the right border

        if i < rows - 1:
            print("|" + "-" * 13 + "|")  # Print the row divider
    
    print("+" + "-" * 13 + "+")  # Print the bottom border

# function to decide which player starts
def coinflip(player1, player2):
    os.system('cls')
    print(f"{Fore.BLUE}Quem começará o jogo?")
    time.sleep(1)
    # create random number between 0 and 1
    coin = random.randint(0,1)
    # if the number is 0 player starts (return 0), if not the first one to play is the bot (return 1)
    if coin == 0:
        print(f"{Fore.BLUE}O jogador", player1, f"{Fore.BLUE}é o primeiro a jogar!\n")
    else:
        print(f"{Fore.BLUE}O jogador", player2, f"{Fore.BLUE}é o primeiro a jogar!\n")
    return coin

# draw clover
def drawClover(indClover, pastIndex):
    # loops until an accetpable clover is drawn
    while True:
            # draws random clover from the sack
            indClover = random.randint(1,40)
            # if clover hasn't been drawn before adds it to the list of drawn clovers and breaks out of the loop
            if indClover not in pastIndex:
                pastIndex.append(indClover)
                break
    return indClover

# function that checks if player can place clover in specific position
def checkPlacement(board, pos, clover, stack):
    # clover in first row
    if pos >= 0 and pos <= 3:
        # stores previous clover in position
        prevClover = board[pos]
        board[pos] = clover
        below = 3          # 3 clover below
        left = 0           # clover counter
        # counts how many clovers are on the left of the position
        loopPosition = pos
        for i in range (4):
            if loopPosition == 0:
                break
            # increment counter
            left += 1
            # decrement position
            loopPosition -= 1 
        # calculates how many numbers are on the right of the position
        right = 4 - left - 1
        # checks if number is higher that the numbers to its left
        for j in range(pos, pos - left - 1, -1):
            if stack[board[j]] > stack[board[pos]]:
                board[pos] = prevClover
                return False
        # checks if number is lower that the numbers to its right (excluding 0)
        for h in range(pos, pos + right + 1, 1):
            if stack[board[h]] < stack[board[pos]] and stack[board[h]] != 0:
                board[pos] = prevClover
                return False
        # checks if number is higher that the numbers below it (excluding 0)    
        for l in range(pos, pos + below * 4 + 4, 4):
            if stack[board[l]] < stack[board[pos]] and stack[board[l]] != 0:
                board[pos] = prevClover
                return False
        return True
    # clover in second row
    elif pos >= 4 and pos <= 7:
         # stores previous clover in position
        prevClover = board[pos]
        board[pos] = clover
        below = 2           # 2 clover below          
        above = 1           # 1 clover above
        left = 0            # clover counter
        pos1 = pos % 4      # calculate absolute position in row
        # counts how many clovers are on the left of the position
        loopPosition = pos1
        for i in range (4):
            if loopPosition == 0:
                break
            # increment counter
            left += 1
            # decrement position
            loopPosition -= 1 
        # calculates how many numbers are on the right of the position
        right = 4 - left - 1
        # checks if number is higher that the numbers to its left
        for j in range(pos, pos - left - 1, -1):
            if stack[board[j]] > stack[board[pos]]:
                board[pos] = prevClover
                return False
        # checks if number is lower that the numbers to its right
        for h in range(pos, pos + right + 1, 1):
            if stack[board[h]] < stack[board[pos]] and stack[board[h]] != 0:
                board[pos] = prevClover
                return False
        # checks if number is higher that the numbers below it     
        for l in range(pos, pos + below * 4 + 4, 4):
            if stack[board[l]] < stack[board[pos]] and stack[board[l]] != 0:
                board[pos] = prevClover
                return False
        # checks if number is lower that the numbers above it
        for p in range(pos, pos - above * 4 - 4, -4):
            if stack[board[p]] > stack[board[pos]]:
                board[pos] = prevClover
                return False
        return True
    # clover in third row
    elif pos >= 8 and pos <= 11:
        # stores previous clover in position
        prevClover = board[pos]
        board[pos] = clover
        below = 1           # 1 clover below          
        above = 2           # 2 clover above
        left = 0            # clover counter
        pos1 = pos % 4      # calculate absolute position in row
        # counts how many clovers are on the left of the position
        loopPosition = pos1
        for i in range (4):
            if loopPosition == 0:
                break
            # increment counter
            left += 1
            # decrement position
            loopPosition -= 1  
        # calculates how many numbers are on the right of the position
        right = 4 - left - 1
        # checks if number is higher that the numbers to its left
        for j in range(pos, pos - left - 1, -1):
            if stack[board[j]] > stack[board[pos]]:
                board[pos] = prevClover
                return False
        # checks if number is lower that the numbers to its right
        for h in range(pos, pos + right + 1, 1):
            if stack[board[h]] < stack[board[pos]] and stack[board[h]] != 0:
                board[pos] = prevClover
                return False
        # checks if number is higher that the numbers below it     
        for l in range(pos, pos + below * 4 + 4, 4):
            if stack[board[l]] < stack[board[pos]] and stack[board[l]] != 0:
                board[pos] = prevClover
                return False
        # checks if number is lower that the numbers above it
        for p in range(pos, pos - above * 4 - 4, -4):
            if stack[board[p]] > stack[board[pos]]:
                board[pos] = prevClover
                return False
        return True
    # clover in fourth row
    else:
        # stores previous clover in position
        prevClover = board[pos]
        board[pos] = clover
        # clover in second row         
        above = 3           # 3 clover above
        left = 0            # clover counter
        pos1 = pos % 4      # calculate absolute position in row
        # counts how many clovers are on the left of the position
        loopPosition = pos1
        for i in range (4):
            if loopPosition == 0:
                break
            # increment counter
            left += 1
            # decrement position
            loopPosition -= 1 
        # calculates how many numbers are on the right of the position
        right = 4 - left - 1
        # checks if number is higher that the numbers to its left
        for j in range(pos, pos - left - 1, -1):
            if stack[board[j]] > stack[board[pos]]:
                board[pos] = prevClover
                return False
        # checks if number is lower that the numbers to its right
        for h in range(pos, pos + right + 1, 1):
            if stack[board[h]] < stack[board[pos]] and stack[board[h]] != 0:
                board[pos] = prevClover
                return False
        # checks if number is lower that the numbers above it
        for p in range(pos, pos - above * 4 - 4, -4):
            if stack[board[p]] > stack[board[pos]]:
                board[pos] = prevClover
                return False
        return True

# funtion that runs when the bot wants to place a clover on the board
def botBoardPlay(board, stack, table, clover):
    os.system('cls')
    showBoard(board, stack)
    input(f"{Fore.GREEN}Pressione uma tecla para continuar...")
    os.system('cls')
    print(f"{Fore.WHITE}O bot está a escolher uma posição...")
    input(f"{Fore.GREEN}Pressione uma tecla para continuar...")
    # loops until bot chooses a valid placement
    while True:
        pos = random.randint(0,15)
        if checkPlacement(board, pos, clover, stack) == True:
            break
    os.system('cls')
    print(f"{Fore.WHITE}O bot colocou o trevo na posição", pos + 1)
    input(f"{Fore.GREEN}Pressione uma tecla para continuar...")
    # put clover on board
    board[pos] = clover         

# function that runs when a bot is supposed to play a turn
def botTurn(bot, board, stack, table, pastIndex):
    dec = 0
    indClover = 0
    os.system('cls')
    print(f"{Fore.WHITE}Turno do bot!")
    print(f"{Fore.RED}1. ",f"{Fore.WHITE}Tirar um trevo do saco")
    print(f"{Fore.RED}2. ",f"{Fore.WHITE}Escolher um trevo da mesa")
    print(f"{Fore.WHITE}\nO bot está a escolher uma opção...")
    input(f"{Fore.GREEN}Pressione uma tecla para continuar...")
    if len(table) != 0:
        dec = random.randint(1,2)
    else:
        dec = 1
    if dec == 1:
        os.system('cls')
        # draws clover
        indClover = drawClover(indClover, pastIndex)
        print(f"{Fore.WHITE}O bot decidiu retirar um trevo do saco!")
        print(f"{Fore.WHITE}O trevo retirado foi um", stack[indClover],"!\n")
        # prompts the options
        print(f"{Fore.RED}1. ",f"{Fore.WHITE}Colocar o trevo no tabuleiro")
        print(f"{Fore.RED}2. ",f"{Fore.WHITE}Colocar o trevo na mesa ")
        print(f"{Fore.WHITE}\nO bot está a escolher uma opção...")
        input(f"{Fore.GREEN}Pressione uma tecla para continuar...")
        clPlace = random.randint(1,2)
        if clPlace == 1:
            os.system('cls')
            print(f"{Fore.WHITE}O bot decidiu colocar o trevo no tabuleiro!")
            input(f"{Fore.GREEN}Pressione uma tecla para continuar...")
            botBoardPlay(board, stack, table, indClover)
        else:
            os.system('cls')
            print(f"{Fore.GREEN}O bot adicionou o trevo à mesa!")
            input(f"{Fore.GREEN}Pressione uma tecla para continuar...")
            # appends stack index to table
            table.append(indClover)
    else:        
        os.system('cls')
        print(f"{Fore.WHITE}O bot decidiu retirar um trevo da mesa!")
        # Prints table using the stack indexes
        print(f"{Fore.WHITE}A mesa possui os seguintes trevos: ")
        # prints table to user
        for i in range(len(table)):         
            print(stack[table[i]], end= ' ')          
        print(f"{Fore.WHITE}\nO bot está a escolher uma opção...")
        input(f"{Fore.GREEN}Pressione uma tecla para continuar...")
        num = random(0, len(table))
        os.system('cls')
        print(f"{Fore.WHITE}\nO bot escolheu o trevo", stack[table[num]],"!")
        input(f"{Fore.GREEN}Pressione uma tecla para continuar...")
        indClover = table[num]          # "pick up" clover from table
        table.remove(indClover)         # removes clover that was picked up rom table
        botBoardPlay(board, stack, table, indClover)   # calls function for bot to place clover on board

# function that runs if a player decides to draw a clover from the sack and place it on the board 
def boardPlay(board, stack, table, clover):
    os.system('cls')
    showBoard(board, stack)
    input(f"{Fore.WHITE}Pressione uma tecla para continuar...")
    while True:         # loops until user inputs a valid board position
        os.system('cls')
        print(f"{Fore.BLUE}+-----------------+")
        print(f"{Fore.BLUE}|  1   2   3   4  |")    
        print(f"{Fore.BLUE}|-----------------|")
        print(f"{Fore.BLUE}|  5   6   7   8  |")    
        print(f"{Fore.BLUE}|-----------------|")
        print(f"{Fore.BLUE}|  9  10  11   12 |")    
        print(f"{Fore.BLUE}|-----------------|")
        print(f"{Fore.BLUE}|  13  14  15  16 |")    
        print(f"{Fore.BLUE}+-----------------+")
        pos = (input(f"{Fore.GREEN}Indique a posição no tabuleiro que pretende colocar o trevo(1-16): "))
        if pos in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']:
            pos = int(pos) - 1
            break
    # check if position is occupied / if it is, switch clovers and send old clover to table
    if board[pos] != 0:
        if checkPlacement(board, pos, clover, stack) == True:
            table.append(board[pos])        # send clover to table
            board[pos] = clover      # put clover on square chosen
        else:
            os.system('cls')
            print(f"{Fore.RED}O trevo não pode ser colocado nesse quadrado!")
            print(f"{Fore.RED}A reiniciar jogada...")
            time.sleep(5)
            boardPlay(board, stack, table, clover)
    else: 
        if checkPlacement(board, pos, clover, stack) == True:
            board[pos] = clover       # put clover on square chosen
        else:
            os.system('cls')
            print(f"{Fore.RED}O trevo não pode ser colocado nesse quadrado!")
            print(f"{Fore.RED}A reiniciar jogada...")
            time.sleep(5)
            boardPlay(board, stack, table, clover)

# function responsible for every action in a player's turn (drawing clover and placing it on board/table) 
def gameTurn(player, board, stack, table, pastIndex): 
    dec = 0
    indClover = 0
    # Asks user for option (loops until acceptable answer)
    while True:
        os.system('cls')
        print(f"{Fore.WHITE}Turno do", player,"!")
        print(f"{Fore.RED}1. ",f"{Fore.WHITE}Tirar um trevo do saco")
        print(f"{Fore.RED}2. ",f"{Fore.WHITE}Escolher um trevo da mesa")
        dec1 = input(f"{Fore.GREEN}Escolha a sua opção: ")
        if dec1 in ['1','2']:
            dec = int(dec1)
            break
    # Draw a clover from stack and place it
    if dec == 1:
        # draws clover
        indClover = drawClover(indClover, pastIndex)
        dec = 0
        while True:         # loops until user inputs an valid answer
            os.system('cls')
            # tells the user what clover was drawn
            print(f"{Fore.WHITE}O trevo retirado foi um", stack[indClover],"!\n")
            # prompts the options
            print(f"{Fore.RED}1. ",f"{Fore.WHITE}Colocar o trevo no tabuleiro")
            print(f"{Fore.RED}2. ",f"{Fore.WHITE}Colocar o trevo na mesa ")
            dec1 = input(f"{Fore.GREEN}Escolha a sua opção: ")
            if dec1 in ['1','2']:
                dec = int(dec1)
                break
            # places on board/play
        if dec == 1:
            boardPlay(board, stack, table, indClover)
        else:
            os.system('cls')
            print(f"{Fore.GREEN}Trevo adicionado à mesa!")
            input(f"{Fore.GREEN}Pressione uma tecla para continuar...")
            # appends stack index to table
            table.append(indClover)
    # draw clover from table and place it
    else:
        # checks if table has any clovers, if it does not, forces player to draw from sack
        if len(table) != 0:
            num = 1
            while True:         # loops question until user inputs valid number
                os.system('cls')
                # Prints table using the stack indexes
                print(f"{Fore.WHITE}A mesa possui os seguintes trevos: ")
                for i in range(len(table)):         
                    print(stack[table[i]], end= ' ')          # prints table to user
                num1 = input(f"{Fore.GREEN}\nInsira o trevo que pretende colocar no tabuleiro(1,2,3...): ")
                if num1 in [str(i + 1 for i in range(len(table)))]:
                    num = int(num1) - 1
                    break       # breaks when user inputs a valid number
            indClover = table[num]          # "pick up" clover from table
            table.remove(indClover)         # removes clover that was picked up rom table
            boardPlay(board, stack, table, indClover)   # calls function to place clover on board
        else:
            os.system('cls')
            print(f"{Fore.RED}A mesa não possui nenhum trevo!")
            print(f"{Fore.RED}O trevo será retirado do saco!")
            input(f"{Fore.RED}Pressione uma tecla para continuar...")
            # draws clover
            indClover = drawClover(indClover, pastIndex)
            dec = 0
            while True:
                os.system('cls')
                # tells the user what clover was drawn
                print(f"{Fore.WHITE}O trevo retirado foi um", stack[indClover],"!\n")
                # prompts the options
                print(f"{Fore.RED}1. ",f"{Fore.WHITE}Colocar o trevo no tabuleiro")
                print(f"{Fore.RED}2. ",f"{Fore.WHITE}Colocar o trevo na mesa ")
                dec1 = input(f"{Fore.GREEN}Escolha a sua opção: ")
                if dec1 in ['1','2']:
                    dec = int(dec1)
                    break
                # places on board/play
            if dec == 1:
                boardPlay(board, stack, table, indClover)
            else:
                os.system('cls')
                print(f"{Fore.GREEN}Trevo adicionado à mesa!")
                input(f"{Fore.GREEN}Pressione uma tecla para continuar...")
                table.append(indClover)

# function that runs when player 1 is the first to play (PvP)
def PvPp1Start(player1, board1, player2, board2, stack, table, pastIndex):
    # Loop that ends when any of the boards is full
        while True:
            # Player 1 turn
            os.system('cls')
            print(f"{Fore.BLUE}Turno do ", player1)
            savePrompt(1, 'PvP', player1, board1, player2, board2, table, pastIndex)
            gameTurn(player1, board1, stack, table, pastIndex)
            # Player 2 turn
            os.system('cls')
            print(f"{Fore.BLUE}Turno do ", player2)
            savePrompt(2, 'PvP', player1, board1, player2, board2, table, pastIndex)
            gameTurn(player2, board2, stack, table,pastIndex)
            # Check if all entries are different from zero, if they are, player1 has won!
            if all(value != 0 for value in board1):
                print(f"{Fore.RED}O Jogador", player1, "é o Vencedor!")
                break
            # Check if all entries are different from zero, if they are, player2 has won!
            elif all(value != 0 for value in board2):
                print(f"{Fore.RED}O jogador", player2,"é o Vencedor!")
                break

# function that runs when player 2 is the first to play (PvP)
def PvPp2Start(player1, board1, player2, board2, stack, table, pastIndex):
    # Loop that ends when any of the boards is full
        while True:
            # Player 2 turn
            os.system('cls')
            print(f"{Fore.BLUE}Turno do ", player2)
            savePrompt(2, 'PvP', player1, board1, player2, board2, table, pastIndex)
            gameTurn(player2, board2, stack, table, pastIndex)
            # Player 1 turn
            os.system('cls')
            print(f"{Fore.BLUE}Turno do ", player1)
            savePrompt(1, 'PvP', player1, board1, player2, board2, table, pastIndex)
            gameTurn(player1, board1, stack, table, pastIndex)
            # Check if all entries are different from zero, if they are, player1 has won!
            if all(value != 0 for value in board1):
                print(f"{Fore.RED}O Jogador", player1, "é o Vencedor!")
                break
            # Check if all entries are different from zero, if they are, player2 has won!
            elif all(value != 0 for value in board2):
                print(f"{Fore.RED}O jogador", player2,"é o Vencedor!")
                break
 
# function that runs when player 1 is the first to play (PvE)
def PvEp1Start(player1, board1, player2, board2, stack, table, pastIndex):
    # Loop that ends when any of the boards is full
        while True:
            os.system('cls')
            # Turn order player - bot
            print(f"{Fore.BLUE}Turno do ", player1)
            savePrompt(1, 'PvE', player1, board1, player2, board2, table, pastIndex)
            gameTurn(player1, board1, stack, table, pastIndex)
            botTurn(player2, board2, stack, table, pastIndex)
            # Check if all entries are different from zero, if they are, player1 has won!
            if all(value != 0 for value in board1):
                print(f"{Fore.RED}O Jogador", player1, "é o Vencedor!")
                break
            # Check if all entries are different from zero, if they are, player2 has won!
            elif all(value != 0 for value in board2):
                print(f"{Fore.RED}O bot é o Vencedor!")
                break  

# function that runs when player 2 is the first to play (PvE)
def PvEbotStart(player1, board1, player2, board2, stack, table, pastIndex):
    # Loop that ends when any of the boards is full
        while True:
            # Turn order bot - player 
            botTurn(player2, board2, stack, table, pastIndex)
            os.system('cls')
            print(f"{Fore.BLUE}Turno do ", player1)
            savePrompt(2, 'PvE', player1, board1, player2, board2, table, pastIndex)
            gameTurn(player1, board1, stack, table, pastIndex)
            # Check if all entries are different from zero, if they are, player1 has won!
            if all(value != 0 for value in board1):
                print(f"{Fore.RED}O Jogador", player1, "é o Vencedor!")
                break
            # Check if all entries are different from zero, if they are, player2 has won!
            elif all(value != 0 for value in board2):
                print(f"{Fore.RED}O bot é o Vencedor!")
                break
 
# funtion that asks player if he wants to save the game       
def savePrompt(pIdentifier, gIdentifer, player1, board1, player2, board2, table, pastIndex):
    # loops question until player inputs valid answer
    while True:
        save = input(f"{Fore.BLUE}Pretende salvar o jogo? (S/N): ")
        if save in ['S', 's']:
            saveGame(pIdentifier, gIdentifer, player1, board1, player2, board2, table, pastIndex)
            break
        elif save in ['N', 'n']:
            break                 
 
# function that saves the game in a file 
def saveGame(pIdentifier, gIdentifer, player1, board1, player2, board2, table, pastIndex):
    # creates unique file, making sure it doesn't overwrite any previous save
    timestamp = time.strftime("%Y%m%d%H%M%S")       # create unique signature
    short_timestamp = timestamp[-3:]  # make the signature smaller,
    # create file
    filename = f"save\save{short_timestamp}.txt"
    # store variables in file
    with open(filename, 'w') as save: 
        save.write(str(pIdentifier) + '\n')         # player identifier
        save.write(str(gIdentifer) + '\n')         # game type identifier
        save.write(str(player1) + '\n')         # player 1 name
        save.write(str(board1) + '\n')          # player 1 board
        save.write(str(player2) + '\n')         # player 2 name
        save.write(str(board2) + '\n')          # player 2 board
        # if list is empty, simply write 0
        if table == []:
            save.write(str(0) + '\n')
        else:
            save.write(str(table) + '\n')       # table
        # if list is empty, simply write 0
        if pastIndex == []:
            save.write(str(0) + '\n')
        else:
            save.write(str(pastIndex) + '\n')       # clovers previously drawn
            
    print(f"{Fore.GREEN}Ficheiro salvo com sucesso!")
    input(f"{Fore.GREEN}Pressione uma tecla para continuar...")
             
# function to load game from a savefile             
def loadGame():
    while True:
        # save file name input
        os.system('cls')
        savename = input(f"{Fore.BLUE}Introduza o nome do ficheiro: ")
        filename = "save/" + savename + ".txt"
        # checks if save file with that name exists
        if os.path.exists(filename) == True:
            break
        else:
            print(f"{Fore.RED}Ficheiro não encontrado!")
            input(f"{Fore.RED}Tente novamente, pressione qualquer tecla para continuar...")
    
    with open(filename, 'r') as save:
        lines = save.readlines()

    pIdentifier = lines[0].strip()      # player turn indicator
    gIdentifier = lines[1].strip()      # game type indicator
    player1 = lines[2].strip()          # player 1 name
    
    board1 = lines[3].strip()           # player 1 board
    # converts list from string to integers
    board1 = board1.strip('[]').split(',')
    board1 = [int(num) for num in board1]
    
    player2 = lines[4].strip()          # player 2 name
    
    board2 = lines[5].strip()           # player 2 board
    # converts list from string to integers
    board2 = board2.strip('[]').split(',')
    board2 = [int(num) for num in board2]
    
    table = lines[6].strip()            # table
    # checks if list is empty
    if table == '0':
        table = []
    else:
        # converts list from string to integers
        table = table.strip('[]').split(',')
        table = [int(num) for num in table]
    
    pastIndex = lines[7].strip()        # clovers previously drawn
    # checks if list is empty
    if pastIndex == '0':
        pastIndex = []
    else:
        # converts list from string to integers
        pastIndex = pastIndex.strip('[]').split(',')
        pastIndex = [int(num) for num in pastIndex]
                
    stack = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20]
    
    # player vs. player
    if gIdentifier == 'PvP':
        # player 1 moves first
        if pIdentifier == '1':
            PvPp1Start(player1, board1, player2, board2, stack, table, pastIndex)
        # player 2 moves first
        else:
            PvPp2Start(player1, board1, player2, board2, stack, table, pastIndex)
    # player vs. bot
    else:
        PvEp1Start(player1, board1, player2, board2, stack, table, pastIndex)

# functions that runs two player game
def twoPlayerGame(player1, player2, board1, board2):
    # Board creation 
    stack = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20]
    table = []
    pastIndex = []  
    
    os.system('cls')
    # initialize players
    player1 = input(f"{Fore.GREEN}Digite o nome do primeiro jogador: ")
    player2 = input(f"{Fore.GREEN}\nDigite o nome do segundo jogador: ")
    # decide who starts
    dec = coinflip(player1, player2)
    input(f"{Fore.GREEN}Pressione uma tecla para continuar...")
    
    if dec == 0:
        PvPp1Start(player1, board1, player2, board2, stack, table, pastIndex)  # player 1 starts      
    else:
        PvPp2Start(player1, board1, player2, board2, stack, table, pastIndex)  # player 2 starts

# function that runs game against bot
def botGame(player1, board1, board2):
    # Board creation 
    stack = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20]
    table = [] 
    pastIndex = []
    
    os.system('cls')
    # initialize players
    player1 = input(f"{Fore.GREEN}Digite o nome do primeiro jogador: ")
    player2 = "BOT"
    # decide who starts
    dec = coinflip(player1, player2)
    input(f"{Fore.GREEN}Pressione uma tecla para continuar...")
    if dec == 0:
        PvEp1Start(player1, board1, player2, board2, stack, table, pastIndex)   # player starts   
    else:
        PvEbotStart(player1, board1, player2, board2, stack, table, pastIndex)  # bot starts
