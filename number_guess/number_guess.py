import random

secret_number = random.randint(0, 100)


def get_guess():
    try:
        guess = int(input("What's your guess? "))
        check_guess(guess)
    except:
        print("Please enter a whole number not a string.")
        get_guess()


def check_guess(guess_int):
    if guess_int == secret_number:
        print("You win!")
        return
    elif guess_int > secret_number:
        print("Too high!")
        new_guess = get_guess()
    else:
        print("Too low!")
        new_guess = get_guess()


get_guess()
