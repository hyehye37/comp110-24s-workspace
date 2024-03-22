"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730395168"
player1_strategy_input: str = input("Pick a secret boat location between 1 and 4: ")
player1_strategy_number: int = int(player1_strategy_input)
if player1_strategy_number > 4:
    print("Error" + "! " + str(player1_strategy_number) + " too" + " high" + " !")
    exit()
if player1_strategy_number < 1:
    print("Error" + "! " + str(player1_strategy_number) + " too" + " low" + " !")
    exit()

player2_strategy_input: str = input("Guess a number between 1 and 4: ")  
player2_strategy_number: int = int(player2_strategy_input) 
if player2_strategy_number < 1:
    print("Error" + "! " + str(player2_strategy_number) + " too" + " low" + " !")
    exit()
if player2_strategy_number > 4:
    print("Error" + "! " + str(player2_strategy_number) + " too" + " high" + " !")
    exit()
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
# if Player1_strategy_number == Player2_strategy_numnber:
result_correct: str = RED_BOX
# if Player1_strategy_number != Player2_strategy_numnber:
result_incorrect: str = WHITE_BOX
if player1_strategy_number != player2_strategy_number:
    if player2_strategy_number == 2:
        print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
        print("Incorrect! You missed the ship.")
    if player2_strategy_number == 3:
        print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
        print("Incorrect! You missed the ship.")
    if player2_strategy_number == 4:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)
        print("Incorrect! You missed the ship.")
    if player2_strategy_number == 1:
        print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
        print("Incorrect! You missed the ship.")
if player1_strategy_number == player2_strategy_number:
    if player2_strategy_number == 1:
        print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
        print("Correct! You hit the ship.")
    if player2_strategy_number == 2:
        print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
        print("Correct! You hit the ship.")
    if player2_strategy_number == 3:
        print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
        print("Correct! You hit the ship.")
    if player2_strategy_number == 4:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
        print("Correct! You hit the ship.")