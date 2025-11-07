import random

number__to_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess > number__to_guess:
            print("Too high!")
        elif guess < number__to_guess:
            print("Too low!")
        else:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number")
