import random

def read_high_scores():
    try:
        with open("high_scores.txt", "r") as f:
            high_scores = [line.strip().split() for line in f]
            high_scores = [(name, int(tries)) for name, tries in high_scores]
    except FileNotFoundError:
        high_scores = []
    return sorted(high_scores, key=lambda x: x[1])

def save_high_scores(high_scores):
    with open("high_scores.txt", "w") as f:
        for name, tries in high_scores:
            f.write(f"{name} {tries}\n")

def play_game():
    name = input("Enter your name:\n ")
    number = random.randint(0, 30)
    attempts = 0

    print("I'm thinking of a number between 0 and 30.")

    while attempts < 10:
        try:
            guess = int(input("Enter your guess:\n "))
            attempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print("Congratulations! You guessed the number in", attempts, "attempts.")
                return (name, attempts)
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 30.")

    print("Sorry, you ran out of attempts. Better luck next time!")
    return None

def display_high_scores(high_scores):
    print("High Scores:")
    for i, (name, tries) in enumerate(high_scores[-10:]):
        print(f"{i + 1}. {name}: {tries} attempts")

def main():
    high_scores = read_high_scores()

    while True:
        print("\nWelcome to the guessing game!")
        print("1. Play")
        print("2. Score")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice:\n "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue

        if choice == 1:
            result = play_game()
            if result:
                high_scores.append(result)
                high_scores = high_scores[-10:]
                save_high_scores(high_scores)
        elif choice == 2:
            display_high_scores(high_scores)
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()