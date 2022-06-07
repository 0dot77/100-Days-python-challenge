from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def guess_the_game(life):
    # Allow the player to submit a guess for a number between 1 and 100.
    print(f"You have {life} attempts remaining to guess the number.")
    user_input = int(input(f"Make a guess: "))
    return user_input


def set_difficulty():
    start = input(
        "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': "
    ).lower()
    if start == "easy":
        # 수를 그냥 반환하는 것보다 상수로 변환할 수 있는 것들은 상수로 바꿔주자
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    random_number = random.randint(0, 100)
    is_game_over = False
    life = set_difficulty()
    while not is_game_over:
        guess = guess_the_game(life)

        if guess == random_number or life == 1:
            if guess == random_number:
                print(f"You got it! The answer was {guess}")
            else:
                print(f"You lose! The answer was {guess}")
            is_game_over = True
        elif guess > random_number:
            life -= 1
            print("Too high")
            print("Guess again")
        elif guess < random_number:
            life -= 1
            print("Too low")
            print("Guess again")


game()
