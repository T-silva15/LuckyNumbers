import random

# Function to print the game board
def print_board(board):
    print("Current Board:")
    print("  ", end="")
    print(" ".join(str(i) for i in range(len(board[0]))))
    print(" ─" + "─" * (2 * len(board[0]) - 1))
    for i, row in enumerate(board):
        print(f"{i}|", end="")
        for j, cell in enumerate(row):
            if cell == 0:
                print(" ", end=" ")
            else:
                print(cell, end="")
            if j != len(row) - 1:
                print("│", end="")
        print("|")
        if i != len(board) - 1:
            print(" ─" + "─" * (2 * len(board[0]) - 1))
    print(" ─" + "─" * (2 * len(board[0]) - 1))

# Function to check if the number placement is valid
def is_valid(board, row, col, number):
    # Check if the number is already present in the row or column
    for i in range(len(board)):
        if board[row][i] == number or board[i][col] == number:
            return False

    # Check if the number is placed in the correct order
    if row > 0 and board[row - 1][col] >= number:
        return False

    return True

# Get player's name
name = input("Enter your name: ")

# Initialize the game board
size = 4
board = [[0] * size for _ in range(size)]

# Generate and shuffle a list of clovers (numbers 1 to 20)
clovers = random.sample(range(1, size * size + 1), size * size)
random.shuffle(clovers)

# Game loop
for i in range(size):
    for j in range(size):
        if i == 0 and j == 0:
            continue
        print_board(board)
        print("It's your turn, " + name + "!")
        assigned_number = clovers.pop()
        print("The number assigned to you is: " + str(assigned_number))
        row = int(input("Enter the row (0-3): "))
        col = int(input("Enter the column (0-3): "))
        if is_valid(board, row, col, assigned_number):
            board[row][col] = assigned_number
        else:
            print("Invalid placement! You cannot put the number there.")
        if all(all(cell != 0 for cell in row) for row in board):
            break

# Print the final board
print_board(board)

# Declare the winner
print(name + " is the winner!")

