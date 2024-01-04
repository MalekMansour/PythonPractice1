import random

def get_choice():
    return input("Enter your choice (rock, paper, or scissors): ").lower()

def determine_winner(user, computer):
    if user == computer: return "It's a tie!"
    if (user == "rock" and computer == "scissors") or \
       (user == "paper" and computer == "rock") or \
       (user == "scissors" and computer == "paper"):
        return "You win!"
    return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_choice()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"You chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if input("Do you want to play again? (yes/no): ").lower() != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
