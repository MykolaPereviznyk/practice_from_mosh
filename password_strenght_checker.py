import re

data_balls = {
    1: "Very Weak",
    2: "Weak",
    3: "Medium",
    4: "Hard",
    5: "Very Hard"
}


def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search('[A-Z]', password):
        strength += 1
    if re.search('[a-z]', password):
        strength += 1
    if re.search('[0-9]', password):
        strength += 1
    if re.search('[@#$%+=!]', password):
        strength += 1
    return strength


def main():
    password = input("Enter a password: ")
    balls = check_password_strength(password)
    print(f"Password strength: {data_balls[balls]}")


if __name__ == "__main__":
    main()
