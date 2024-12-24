# Part 4
# Q1. You are developing a simple game where the player needs to select
# a cell in a 3x3 matrix and reveal its content.
# Initially, all cells in the matrix are hidden and have a value of 1.
# When the player chooses a cell, the value in that cell is revealed and
# replaced with an 'X' to indicate that it has been selected.
# The game continues until all cells have been selected.
# As the developer, you need to implement the game logic in Python.
# Write a function play_game() that takes no parameters and returns nothing.
# The function should create a 3x3 matrix of integers, initialize all cells
# with a value of 1, and then repeatedly prompt the
# player to choose a cell until all cells have been selected.
# Your 3x3 matrix should initially should look as shown below:
# matrix = [[1, 1, 1],
# [1, 1, 1],
# [1, 1, 1] ]
# When the player chooses a cell, the function should print the updated
# matrix with the selected cell marked with an 'X'.
# If the player chooses a cell that has already been selected,
# the function should print an error message and prompt the player to choose again.
# Once all cells have been selected, the function should print a message
# indicating that the game is over and
# the total number of moves made by the player.
# Hint: Create a 3x3 matrix of integers,
# prompt the player to choose a cell and reveal its content, and
# keep track of the number of moves until all cells have been selected.

matrix = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
moves = 0
while True:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f'{matrix[i][j]} | ', end='')
        print()

    allX = all(value == 'X' for row in matrix for value in row)
    if allX:
        print('Game Over')
        print(f'No. of Moves = {moves}')
        break

    row = input('Enter row 1, 2 or 3: ')
    column = input('Enter column 1, 2 or 3: ')
    if row.isdigit() and column.isdigit():
        row = int(row)
        column = int(column)
        if (0 < row <= 3) and (0 < column <= 3):
            if matrix[row-1][column-1] == 'X':
                print(f'Row[{row}] and Column[{column}] already selected')
                moves += 1
            else:
                matrix[row-1][column-1] = 'X'
                moves += 1
        else:
            print('Invalid! index selected\n')
            moves += 1
    else:
        print('Not a valid input')
    print(f'No. of moves = {moves}')

# dean4@DESKTOP-UEPI2CG MINGW64 /d/BIC/Python/Week 5/Part 4
# $ python Q1.py
# 1 | 1 | 1 |
# 1 | 1 | 1 |
# 1 | 1 | 1 |
# Enter row 1, 2 or 3: 1
# Enter column 1, 2 or 3: 1
# No. of moves = 1
# X | 1 | 1 | 
# 1 | 1 | 1 | 
# 1 | 1 | 1 | 
# Enter row 1, 2 or 3: 1
# Enter column 1, 2 or 3: 1
# Row[1] and Column[1] already selected
# No. of moves = 2
# X | 1 | 1 | 
# 1 | 1 | 1 | 
# 1 | 1 | 1 | 
# Enter row 1, 2 or 3: 1
# Enter column 1, 2 or 3: 2
# No. of moves = 3
# X | X | 1 | 
# 1 | 1 | 1 | 
# 1 | 1 | 1 | 
# Enter row 1, 2 or 3: 1
# Enter column 1, 2 or 3: 3
# No. of moves = 4
# X | X | X | 
# 1 | 1 | 1 | 
# 1 | 1 | 1 | 
# Enter row 1, 2 or 3: 2
# Enter column 1, 2 or 3: 1
# No. of moves = 5
# X | X | X |
# X | 1 | 1 |
# 1 | 1 | 1 |
# Enter row 1, 2 or 3: 2
# Enter column 1, 2 or 3: 2
# No. of moves = 6
# X | X | X |
# X | X | 1 |
# 1 | 1 | 1 |
# Enter row 1, 2 or 3: 2
# Enter column 1, 2 or 3: 3
# No. of moves = 7
# X | X | X |
# X | X | X |
# 1 | 1 | 1 |
# Enter row 1, 2 or 3: 3
# Enter column 1, 2 or 3: 1
# No. of moves = 8
# X | X | X |
# X | X | X |
# X | 1 | 1 |
# Enter row 1, 2 or 3: 3
# Enter column 1, 2 or 3: 2
# No. of moves = 9
# X | X | X |
# X | X | X |
# X | X | 1 |
# Enter row 1, 2 or 3: 3
# Enter column 1, 2 or 3: 3
# No. of moves = 10
# X | X | X |
# X | X | X |
# X | X | X |
# Game Over
# No. of Moves = 10