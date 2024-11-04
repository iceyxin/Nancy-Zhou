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
# Slide and merge row to the left
def slide_left(row):
    new_row = [num for num in row if num != 0]  # Remove zeros
    merged_row = []
    skip = False

    for i in range(len(new_row)):
        if skip:
            skip = False
            continue
        if i + 1 < len(new_row) and new_row[i] == new_row[i + 1]:  # Merge only if the next tile is the same
            merged_row.append(new_row[i] * 2)
            skip = True  # Skip the next tile after merging
        else:
            merged_row.append(new_row[i])

    merged_row += [0] * (4 - len(merged_row))  # Pad with zeros on the right
    return merged_row

# Move entire board left
def move_left(board):
    moved = False
    for i in range(4):
        original_row = board[i]
        new_row = slide_left(original_row)
        if new_row != original_row:
            moved = True
        board[i] = new_row
    return moved

# Rotate the board clockwise
def rotate_board_clockwise_in_place(board):
    # Transpose the matrix
    for i in range(4):
        for j in range(i + 1, 4):
            board[i][j], board[j][i] = board[j][i], board[i][j]
    # Reverse each row
    for i in range(4):
        board[i].reverse()

def rotate_board_counterclockwise_in_place(board):
    # Transpose the matrix
    for i in range(4):
        for j in range(i + 1, 4):
            board[i][j], board[j][i] = board[j][i], board[i][j]
    # Reverse each column
    for j in range(4):
        for i in range(2):
            board[i][j], board[3 - i][j] = board[3 - i][j], board[i][j]

# Movement functions based on rotation
def move_right(board):
    # Reverse each row in place
    for i in range(len(board)):
        board[i] = board[i][::-1]  # Reverse each row for right movement
    # Apply left movement logic to the reversed board
    moved = move_left(board)
    # Reverse each row back to its original orientation
    for i in range(len(board)):
        board[i] = board[i][::-1]
    return moved

def move_down(board):
    rotate_board_clockwise_in_place(board)  # Rotate 90 degrees clockwise
    moved = move_left(board)  # Move left on the rotated board
    rotate_board_counterclockwise_in_place(board)  # Rotate back counterclockwise
    return moved

def move_up(board):
    rotate_board_counterclockwise_in_place(board)  # Rotate 90 degrees counterclockwise
    moved = move_left(board)  # Move left on the rotated board
    rotate_board_clockwise_in_place(board)  # Rotate back clockwise
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