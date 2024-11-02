import random

# Create a 4x4 grid (matrix) to represent the game board.
def initial_board():
    board = [[0] *4 for _ in range(4)] # Empty cells are represented by 0
    initial_cell(board)
    initial_cell(board)
    return board
# add 2 at a random empty position on the game board
def initial_cell(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0] # find empty cell
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2
# display board
def display_board(board):
    for row in board:
        print("\t".join(str(cell) if cell != 0 else '.' for cell in row))
    print("\n")
    
# Game Board Initialization and Visualization   
# Slides and merges a row to the left.
def slide_left(row):
    new_row = [num for num in row if num != 0]  # remove all zeros
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:  # merge equal tiles
            new_row[i] *= 2
            new_row[i + 1] = 0  # mark the merged tile for removal
    new_row = [num for num in new_row if num != 0]  # remove zeros again after merging
    return new_row + [0] * (len(row) - len(new_row))  # pad the row with zeros on the right

def move_left(board):
    moved = False
    for i in range(4):
        original_row = board[i]
        new_row = slide_left(original_row)
        if new_row != original_row:
            moved = True
        board[i] = new_row
    return moved
    
# Slides and merges a row to the right.
def slide_right(row):
    new_row = [num for num in row if num != 0]  # remove all zeros
    for i in range(len(new_row) - 1, 0, -1):  # iterate from the end to the start
        if new_row[i] == new_row[i - 1]:  # merge equal tiles
            new_row[i] *= 2
            new_row[i - 1] = 0  # mark the merged tile for removal
    new_row = [num for num in new_row if num != 0]  # remove zeros after merging
    return [0] * (len(row) - len(new_row)) + new_row  # pad the row with zeros on the left

def move_right(board):
    moved = False
    for i in range(4):
        original_row = board[i]
        new_row = slide_right(original_row)
        if new_row != original_row:
            moved = True
        board[i] = new_row
    return moved

# merges a row to the up and down.
def transpose(board):
    return [list(row) for row in zip(*board)]

def move_up(board):
    board = transpose(board)  # transpose to use row logic on columns
    moved = move_left(board)  # use left logic on transposed board
    board = transpose(board)  # transpose back to original orientation
    return moved

def move_down(board):
    board = transpose(board)  # transpose to use row logic on columns
    moved = move_right(board)  # use right logic on transposed board
    board = transpose(board)  # transpose back to original orientation
    return moved
    
# win condition
def check_win(board):
    for row in board:
        if 2048 in row:
            return True
    return False
# lose     
def check_loss(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if i < 3 and board[i][j] == board[i + 1][j]:
                return False
            if j < 3 and board[i][j] == board[i][j + 1]:
                return False
    return True