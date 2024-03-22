"""EX02 - One Shot Battleship - A cute step toward Battleship."""

__author__ = "730395168"


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

GRID_SIZE: int = 4
SECRET_ROW: int = 3
SECRET_COLUMN: int = 2
result: str = ""
 
guess_row: int = int(input("Guess a row: "))
while guess_row > GRID_SIZE or guess_row < 1:
    guess_row = int(input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: ")) 

guess_column: int = int(input("Guess a column: "))
while guess_column > GRID_SIZE or guess_column < 1:
    guess_column = int(input(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: ")) 

if (guess_column == SECRET_COLUMN and guess_row == SECRET_ROW):
    result = RED_BOX
else:
    result = WHITE_BOX

counter_row: int = 1
while counter_row <= GRID_SIZE:
    emoji: str = ""
    column_counter: int = 1
    if guess_row == counter_row:
        while column_counter <= GRID_SIZE:
            if guess_column == column_counter:
                emoji += result
            else:
                emoji += BLUE_BOX
            column_counter += 1
    else:
        while column_counter <= GRID_SIZE:
            emoji += BLUE_BOX
            column_counter += 1
    print(emoji)
    counter_row += 1

if (guess_column == SECRET_COLUMN and guess_row == SECRET_ROW):
    result = RED_BOX
    print("Hit!")
elif guess_column == SECRET_COLUMN and guess_row != SECRET_ROW:
    print("Close! Correct column, wrong row.")
elif guess_row == SECRET_ROW and guess_column != SECRET_COLUMN:
    print("Close! Correct row, wrong column.")
else:
    result = WHITE_BOX
    print("Miss!")







def print_grid (size_guess: int, guess_row: int, guess_column: int, correctness: bool) -> None:
    """Given the above variables, print the game board"""
    if correctness == True:
        result = RED_BOX
    else:
        correctness == False
        result = WHITE_BOX

    counter_row: int = 1
    while counter_row <= size_guess:
        emoji: str = ""
        column_counter: int = 1
        if guess_row == counter_row:
            while column_counter <= size_guess:
                if guess_column == column_counter:
                    emoji += result
                else:
                    emoji += BLUE_BOX
                column_counter += 1
        else:
            while column_counter <= size_guess:
                emoji += BLUE_BOX
                column_counter += 1
        print(emoji)
        counter_row += 1

def correct_guess(secret_row: int, secret_column: int, guess_row: int, guess_column: int) -> bool:
    """Given the secret boat location and the user guess, return if the user was correct or not"""
    if (secret_column == guess_column and secret_row == guess_row):
        print(True)
    else:
        print(False)