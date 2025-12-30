class ATM:
    def __init__(self):
        self.balance = 0
        self.amount_deposit = 0
        self.amount_withdraw = 0
        self.activite = True

    def start(self):
        self.activite = True
        while self.activite:
            print("Welcome to the ATM!")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            self.option = int(input("Please choose an option: "))

            match self.option:
                case 1:
                    self.check_balance()
                case 2:
                    self.deposit()
                case 3:
                    self.withdraw()
                case 4:
                    self.exit()

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self):
        while True:
            try:
                self.amount_deposit = int(
                    input("Enter the amount to deposit: "))
                if self.amount_deposit > 0:
                    break
                print("Deposit amount must be positive.")
            except ValueError:
                print("Please enter a valid number.")
        self.balance += self.amount_deposit
        print(f"Successfully deposited ${self.amount_deposit}.0.")

    def withdraw(self):
        while True:
            try:
                self.amount_withdraw = int(
                    input("Enter the amount to withdraw: "))
                if self.amount_withdraw > 0:
                    if self.amount_withdraw <= self.balance:
                        break
                    print("Insufficient funds.")
                else:
                    print("Withdrawal amount must be positive.")
            except ValueError:
                print("Please enter a valid number.")

        self.balance -= self.amount_withdraw
        print(f"Successfully withdrew ${self.amount_withdraw}.0.")

    def exit(self):
        self.activite = False


if __name__ == "__main__":
    atm = ATM()
    atm.start()
