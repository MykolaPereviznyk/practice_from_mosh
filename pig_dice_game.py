import random


def roll_die():
    return random.randint(1, 6)


def get_score(player_score):
    roll = roll_die()
    print(f"You rolled a {roll}")
    if roll == 1:
        return 0
    return player_score + roll


def playing(current_player, name_player):
    print(f"\nPlayer {name_player}'s turn")
    current_player = get_score(current_player)
    for i in range(2):
        if str(input("Roll again? (y/n): ")).upper() == "Y":
            current_player = get_score(current_player)
        else:
            return current_player
    print(f"\nYou scored {current_player} points this turn.")
    return current_player


def main():
    scores = [0, 0]
    while True:
        for i in range(2):
            scores[i] = playing(scores[i], i + 1)
            if scores[i] >= 100:
                print(f"player {i + 1} wins!")
                return
        print(
            f"Current: Player 1: {scores[0]}, Player 2: {scores[1]}")


if __name__ == "__main__":
    main()

