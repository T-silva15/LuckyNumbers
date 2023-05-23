import random

# Function to print the game board
def print_board(board):
    print("Current Board:")
    for row in board:
        print(" ".join(str(cell) for cell in row))

# Function to check if the number placement is valid
def is_valid(board, row, col, number):
    # Check if the number is already present in the row or column
    for i in range(4):
        if board[row][i] == number or board[i][col] == number:
            return False
    
    # Check if the number is placed in the correct order
    if row > 0 and board[row-1][col] >= number:
        return False
    
    return True

# Get player's name
name = input("Enter your name: ")

# Initialize the game board
board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Generate and place random clovers on the board
clovers = random.sample(range(1, 21), 16)
for i in range(4):
    for j in range(4):
        if i == 0 and j == 0:
            continue
        board[i][j] = clovers.pop()

# Game loop
while True:
    print_board(board)
    
    # Get input for number placement
    row = int(input("Enter the row (0-3): "))
    col = int(input("Enter the column (0-3): "))
    number = int(input("Enter the number (1-20): "))
    
    # Check if the placement is valid
    if is_valid(board, row, col, number):
        board[row][col] = number
    else:
        print("Invalid placement! You cannot put the number there.")
    
    # Check if the game is over
    if all(all(cell != 0 for cell in row) for row in board):
        break

# Print the final board
print_board(board)

# Declare the winner
print(name + " is the winner!")
