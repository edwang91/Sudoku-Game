from random import randint, shuffle


# 0 in board means empty space to be filled in
# Sudoku board generator

# FUnction definitions----------------------------------------------------------------------------------

# is_solution() will check if any remaining 0s are left in the board
# Parameters: the current state of the board
# Return: true if it is the solution, otherwise false


def is_solution(board):
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                return False

    return True


# Preset function returns all the preset values of original board
# Parameters: the original unfilled board
# Returns list of pre-set box positions in the form [x, y]

def pre_set(board):
    preset_list = []

    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                preset_list.append([row, col])

    return preset_list


# Function checks if a given value is unique in the column
# Parameters: Current state of the board, current column position, and current value attempted to be inserted
# Returns True if no other value in the corresponding column matches, otherwise False
def unique_col(curr_board, column, value):
    for row in range(9):
        if value == curr_board[row][column]:
            return False

    return True


# Function checks if a given value is unique in the box
# Parameters: the current state of the board, current position, and current value attempted to be inserted
# Returns True if no other value in the 3 by 3 box matches otherwise returns False
def unique_box(curr_board, row, column, value):
    for y in range(int(row / 3) * 3, int((row / 3) + 1) * 3):
        for x in range(int(column / 3) * 3, int((column / 3) + 1) * 3):
            if value == curr_board[y][x]:
                return False

    return True


# Function updates the coordinates
# Parameters: current position and list of pre-set positions
# Returns the next empty position
# Note: coordinates returned may go out of bounds
def update_coords(curr_coord, pre_set_coord):
    row = curr_coord[0]
    col = curr_coord[1]

    if col == 8:
        row += 1
        col = 0

    else:
        col += 1

    while pre_set_coord.count([row, col]) != 0:
        if col == 8:
            row += 1
            col = 0

        else:
            col += 1

    return [row, col]


# back_track() function is recursive function and main driver for solving the puzzle
# Function will start from 1, and check if it is unique from all other values in the same
# row, column, and 3x3 box.
# If it is unique, then update the current_board and move to next non-zero box and repeat.
# If it is not unique, try the next number.

# If none of the values 1-9 meet the unique conditions, return to previous coordinate and try another unique value.
# Parameters: current state of board, current box we are on
# Return: updated_board(?)

def back_track(curr_board, curr_coord, preset_coord):
    row = curr_coord[0]
    col = curr_coord[1]

    new_coord = update_coords(curr_coord, preset_coord)

    # Checking if chosen value is unique
    for val in range(1, 10):
        if curr_board[row].count(val) == 0 and unique_col(curr_board, col, val) and unique_box(curr_board, row, col,
                                                                                               val):
            curr_board[row][col] = val
            if new_coord[0] > 8 or new_coord[1] > 8:  # case for being at the last box and we find the right value
                return curr_board

            new_board = back_track(curr_board, new_coord, preset_coord)

            if is_solution(new_board):
                return new_board

    # If the for loop completes without returning, then no values were unique -> back track to the previous
    # coordinate and try another value at that coordinate
    curr_board[row][col] = 0
    return curr_board


# Sudoku solver function

def sud_solver(board, preset_boxes):
    solution = []

    # Start the back_track algorithm by starting with the first 0-value coordinate
    for i in range(9):
        for j in range(9):
            if sud_board[i][j] == 0:
                solution = back_track(sud_board, [i, j], preset_list)

    return solution


# Function that generates sudoku board
def sud_generator(board):
    count = 81
    list_emptied = []

    while count > 17:
        rand_row = randint(0, 8)
        rand_col = randint(0, 8)
        if list_emptied.count([rand_row, rand_col]) == 0:
            board[rand_row][rand_col] = 0
            list_emptied.append([rand_row, rand_col])
            count -= 1

    return board


# Main ----------------------------------------------------------------------------------

sud_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 8, 0, 0, 0, 0]]

# Generate fully filled out sudoku board
preset_list = pre_set(sud_board)
solution = sud_solver(sud_board, preset_list)

print("\n\n")

for row in solution:
    print(row)

# Fully filled board generated. Now start removing random elements until only 17 boxes remain
gen_board = sud_generator(solution)

print("\n\nGenerated sudoku board:\n\n")

for row in gen_board:
    print(row)

