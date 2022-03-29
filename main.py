from art import logo
import random
import os

def easy_mode_game():
    # Computer random number between 1 to 100
    computer_guess = random.randint(1, 100)
    easy_mode_attempts = 10
    is_guess_over = False
    while(not is_guess_over):
        if(easy_mode_attempts == 0):
            print("You've run out of guesses, you lose")
            break
        print(f"You have {easy_mode_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if(user_guess > computer_guess):
            print("Too high")
            print("Guess again")
            easy_mode_attempts -= 1
        elif(user_guess < computer_guess):
            print("Too low")
            print("Guess again")
            easy_mode_attempts -= 1
        else:
            print(f"You got it! The answer was {computer_guess}")
            is_guess_over = True


def hard_mode_game():
    # Computer random number between 1 to 100
    computer_guess = random.randint(1, 100)
    hard_mode_attempts = 5
    is_guess_over = False
    while(not is_guess_over):
        if(hard_mode_attempts == 0):
            print("You've run out of guesses, you lose")
            break
        print(f"You have {hard_mode_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if(user_guess > computer_guess):
            print("Too high")
            print("Guess again")
            hard_mode_attempts -= 1
        elif(user_guess < computer_guess):
            print("Too low")
            print("Guess again")
            hard_mode_attempts -= 1
        else:
            print(f"You got it! The answer was {computer_guess}")
            is_guess_over = True


def guess_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    user_choice_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if(user_choice_mode.lower() == "easy"):
        easy_mode_game()
    elif(user_choice_mode.lower() == "hard"):
        hard_mode_game()
    else:
        print("Please type 'easy' or 'hard' ")

is_game_end = False
while(not is_game_end):
    play_game = input("Do you want to play a guess number game? Type 'y' or 'n': ")
    if(play_game.lower() == "y"):
        os.system("cls")
        guess_game()
    else:
        is_game_end = True
