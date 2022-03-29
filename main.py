from art import logo
import random
import os


def game(difficulty):
    # Computer random number between 1 to 100
    computer_guess = random.randint(1, 100)
    if(difficulty == "easy"):
        attempts = 10
    else:
        attempts = 5
    is_guess_over = False
    while(not is_guess_over):
        if(attempts == 0):
            print("You've run out of guesses, you lose")
            break
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if(user_guess > computer_guess):
            print("Too high")
            print("Guess again")
            attempts -= 1
        elif(user_guess < computer_guess):
            print("Too low")
            print("Guess again")
            attempts -= 1
        else:
            print(f"You got it! The answer was {computer_guess}")
            is_guess_over = True


def choose_difficulty():
    user_choice_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if(user_choice_mode.lower() == "easy"):
        return "easy"
    elif(user_choice_mode.lower() == "hard"):
        return "hard"
    else:
        print("Please type 'easy' or 'hard' ")


def guess_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = choose_difficulty()
    game(difficulty)

is_game_end = False
while(not is_game_end):
    play_game = input(
        "Do you want to play a guess number game? Type 'y' or 'n': ")
    if(play_game.lower() == "y"):
        os.system("cls")
        guess_game()
    else:
        is_game_end = True

