import random

data = {
    "r": ("Parer", "Rock"),
    "p": ("Scissors", "Paper"),
    "s": ("Rock", "Scissors")
}

short_choic = tuple(data.keys())
ask_continue = ("n", "y")

while True:
    user_chose = str(input("Rock, paper, or scissors? (r/p/s): ")).lower()

    if user_chose in short_choic:
        pc_chose = random.choice(["Rock", "Paper", "Scissors"])
        print(f"You chose {data[user_chose][1]}")
        print(f"Computer chose {pc_chose}")
        if data[user_chose][0] == pc_chose:
            print("You win")
        elif data[user_chose][1] == pc_chose:
            print("Tie!")
        else:
            print("You lose")

        con = str(input("Continue? (y/n): ")).lower()
        if con in ask_continue:
            if con == "y":
                pass
            else:
                break
        else:
            print("Invalid choice!")

    else:
        print("Invalid choice!")
