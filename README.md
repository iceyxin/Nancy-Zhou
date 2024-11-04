# Nancy-Zhou

Welcome to my 2048 game project! This README will walk you through the steps needed to implement and run a basic command-line version of 2048 in Python.

**Project Overview**
This project involves building a simplified version of the popular 2048 game, where:
Use a 4x4 grid (matrix) to represent the game board.
The game starts with two randomly placed cells each containing the number 2; all other cells are empty.
At the beginning of each turn, a new "2" is added in an empty cell at random.

**Game Mechanics**
User Controls:
use W, S, A, D, Q keys to move up, down, left, right, and Quit respectively.

**Game Rules:**
When press a key, numbers in the grid shift in the chosen direction: 
If two adjacent numbers in a row (for horizontal moves) or column (for vertical moves) are the same, they combine into their sum. 
After combining, the resulting number fills one cell, while the other becomes empty. 
If no numbers can combine, all numbers still shift in the chosen direction, filling the empty spaces. 
If reach 2048 in any cell, I win! If there are no moves left, the game ends, allowing me to restart or quit.

**Exception Handling:**
Used exception handling to capture any invalid inputs and unexpected actions during gameplay.

**Project Structure**
The project includes two Python files:
main.py: This is the main file where  run the game, manage user input, handle game state, and display updates. It imports functions from game_functions.py.
game_functions.py: This file contains all the necessary functions, including:

Initializing the board with two random "2"s
Handling movement logic and combining cells
Checking for win/loss conditions
Additional helper functions as needed
