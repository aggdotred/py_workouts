import random
answer = random.randint(0, 100)

for i in range(0, 3):
    i += 1
    try:
        user_guess = int(input("What's your guess? "))
    except:
        print("Please enter a whole number not a string.")
        break

    if user_guess == answer:
        print(f"Right!  The answer is {user_guess}")
        break

    elif user_guess < answer:
        print(f"Your guess of {user_guess} is too low!")

    elif user_guess > answer:
        print(f"Your guess of {user_guess} is too high!")
