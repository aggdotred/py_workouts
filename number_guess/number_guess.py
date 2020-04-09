import random

secret_number = random.randint(0, 100)


def get_guess():
    guess = input("What's your guess? ")
    return int(guess)


def check_guess(guess_int):
    if guess_int == secret_number:
        print("You win!")
    elif guess_int > secret_number:
        print("Too high!")
        new_guess = get_guess()
        check_guess(new_guess)
    else:
        print("Too low!")
        new_guess = get_guess()
        check_guess(new_guess)


guess = get_guess()
check_guess(guess)
