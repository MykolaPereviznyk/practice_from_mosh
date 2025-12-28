import random


def get_starting_balance():
    while True:
        try:
            balance = int(input("Enter your starting balance: $"))
            if balance <= 0:
                print("Balance must be a positive number.")
            else:
                return balance
        except ValueError:
            print("Please enter a valid number.")


def get_bet_amount(balance):
    while True:
        try:
            bet = int(input("Enter your bet amount: $"))
            if 1 <= bet <= balance:
                return bet
            else:
                print(
                    f"Invalid bet amount. You can bet between $1 and ${balance}.")
        except ValueError:
            print("Please enter a valid number for the bet amount.")


def spin_reels():
    symbols = ["🍒", "🍋", "🔔", "⭐", "🍉"]
    text = random.choices(symbols, k=3)
    return text


def display_reels(reels):
    print(*reels, sep="|")


def calculate_payout(reels, bet):
    won = 0
    for i in reels:
        if reels.count(i) == 2:
            won = 2
        if reels.count(i) == 3:
            won = 3
    if won >= 2:
        print(f"You won ${bet * won}")
        return (bet * won) - bet
    else:
        print("You lost!")
        return -bet


def main():
    balance = get_starting_balance()
    print(
        f"Welcome to the slot Machine Game!\nYou start with a balance of ${balance}")
    while balance > 0:
        print(f"\nCurrent balance: ${balance}")
        bet = get_bet_amount(balance)
        reels = spin_reels()
        display_reels(reels)
        balance += calculate_payout(reels, bet)
        if balance <= 0:
            print("You are out of money! Game over.")
            break
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print(f"You walk away with ${balance}.")
            break


if __name__ == "__main__":
    main()
