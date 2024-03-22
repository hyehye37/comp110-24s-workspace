"""Making a functional battleship."""

__author__ = "730395168"
import random


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(size_guess: int, row_or_column: str) -> int:
    """Returns grid size and user's row or column guesses."""
    assert row_or_column == "row" or row_or_column == "column" 
    input_guess: int = int(input(f"Guess a {row_or_column}: "))
    while input_guess > size_guess or input_guess < 1:
        input_guess = int(input(f"The grid is only {size_guess} by {size_guess}. Try again: "))
    return input_guess


def print_grid(size_guess: int, guess_row: int, guess_column: int, correctness: bool) -> None:
    """Given the above variables, print the game board."""
    if correctness is True:
        result = RED_BOX
    else:
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
    """Given the secret boat location and the user guess, return if the user was correct or not."""
    if (secret_column == guess_column and secret_row == guess_row):
        return True
    else:
        return False


def main(size_guess: int, secret_row: int, secret_column: int) -> None:
    """Putting everything together."""
    turn_num: int = 1
    win: bool = False
    while (turn_num <= 5 and win is False): 
        print(f"=== Turn {turn_num}/5 ===")
    
        guess_row: int = input_guess(size_guess, "row")

        guess_column: int = input_guess(size_guess, "column")
        
        verify_guess: bool = correct_guess(secret_row, secret_column, guess_row, guess_column)
        
        print_grid(size_guess, guess_row, guess_column, win)

        if verify_guess is True:
            print("Hit!")
            print(f"You won in {turn_num}/5 turns!")
            win = True 
            turn_num = 6
        else:
            print("Miss!")

        if turn_num == 5:
            print("X/5 - Better luck next time!")
        turn_num += 1   


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))