import random


def generate_secret():
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join([str(digit) for digit in digits[:4]])


def start():
    while True:
        guess = input("Guess: ")
        if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
            return guess
        print("Invalid guess. Please enter a 4-digit number with unique digits.")


def calculate_cows_and_bulls(secret, guess):
    bulls = sum([1 for i in range(4) if guess[i] == secret[i]])
    cows = sum([1 for i in range(4) if guess[i] in secret] - bulls)
    return cows, bulls


def win(cows, bulls):
    print(f"{cows} cows, {bulls} bulls")
    if bulls == 4:
        print("Congratulations! You guessed the correct number")
        return True
    return False


def main():
    print("I have generated a 4-digit number with unique digits. Try to guess it!")
    secret = generate_secret()
    while True:
        guess = start()
        cows, bulls = calculate_cows_and_bulls(secret, guess)
        if win(cows, bulls):
            break


if __name__ == "__main__":
    main()
