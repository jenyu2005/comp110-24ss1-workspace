"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730649181"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
emoji_box: str = ""


secret_location = int(input("Pick a secret boat location between 1 and 4: "))
if secret_location < 1:
    print(f"Error! {secret_location} too low!")
    exit()
elif secret_location > 4:
    print(f"Error! {secret_location} too high!")
    exit()

second_user_guess = int(input("Guess a number between 1 and 4:"))
if second_user_guess < 1:
    print(f"Error! {second_user_guess} too low!")
    exit()
elif second_user_guess > 4:
    print(f"Error! {second_user_guess} too high!")
    exit()


if second_user_guess == 1:
    if second_user_guess == secret_location:
        print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
        print("Correct! You hit the ship.")
    else:
        print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
        print("Incorrect! You missed the ship.")
elif second_user_guess == 2:
    if second_user_guess == secret_location:
        print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
        print("Correct! You hit the ship.")
    else:
        print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
        print("Incorrect! You missed the ship.")
elif second_user_guess == 3:
    if second_user_guess == secret_location:
        print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
        print("Correct! You hit the ship.")
    else:
        print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
        print("Incorrect! You missed the ship.")
elif second_user_guess == 4:
    if second_user_guess == secret_location:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
        print("Correct! You hit the ship.")
    else:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)
        print("Incorrect! You missed the ship.")
