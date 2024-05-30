"""EX02 - One Shot Battleship."""

__author__ = "730649181"

grid_size = 4
secret_row = 3
secret_column = 2

# box emojis
BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"


# Function 1
def row_input(grid_size: int) -> int:  # value returns to int
    row_guess = int(input("Guess a row: "))
    while row_guess < 1 or row_guess > grid_size:  # one has to be true
        row_guess = int(
            input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
        )
    return row_guess


# Function 2
def column_input(grid_size: int) -> int:  # value returns to int
    column_guess = int(input("Guess a column: "))
    while column_guess < 1 or column_guess > grid_size:  # one has to be true
        column_guess = int(
            input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
        )
    return column_guess


# Function 3- print grid with while loops and if-else
def print_grid(
    grid_size: int, row_guess: int, column_guess: int, result_box: int
) -> int:  # value returns to int
    row_counter = 1  # starts at 1
    while row_counter <= grid_size:
        row_str = ""
        column_counter = 1  # starts at 1
        while column_counter <= grid_size:
            if (
                row_counter == row_guess and column_counter == column_guess
            ):  # checks if grid matches user's guess
                row_str += result_box
            else:
                row_str += BLUE_BOX
            column_counter += 1  # avoids infinite loop
        print(row_str)
        row_counter += 1  # avoids infinite loop


# Row and column input!!!
row_guess = row_input(grid_size)
column_guess = column_input(grid_size)

# Result box
if row_guess == secret_row and column_guess == secret_column:  # both have to be true
    result_box = RED_BOX  # user guessed correctly
else:
    result_box = WHITE_BOX  # user guessed incorrectly

# Print grid with the user's guess (passing these four arguments)
print_grid(grid_size, row_guess, column_guess, result_box)

# Giving a hint to the user
if row_guess == secret_row and column_guess == secret_column:  # both have to be true
    print("Hit!")
elif row_guess == secret_row:
    print("Close! Correct row, wrong column.")
elif column_guess == secret_column:
    print("Close! Correct column, wrong row.")
else:  # False (opposite of all those above)
    print("Miss!")
