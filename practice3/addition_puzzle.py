import random

def generate_addition(difficulty):
    if difficulty == 'easy':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif difficulty == 'normal':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
    elif difficulty == 'hard':
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
    else:
        raise ValueError("Invalid difficulty level!")
    
    equation = f"{num1} + {num2}"
    result = num1 + num2
    return equation, result

def main():
    print("Welcome to the Addition Math Puzzle Game!")
    while True:
        print("Choose your difficulty: easy, normal, or hard")
        difficulty = input("Difficulty: ").lower()
        if difficulty not in ['easy', 'normal', 'hard']:
            print("Invalid difficulty level! Please choose again.")
            continue
        
        print(f"You've chosen {difficulty} difficulty. Solve the additions to win!")
        score = 0
        rounds_played = 0
        while rounds_played < 10:
            equation, correct_answer = generate_addition(difficulty)
            print(f"Equation: {equation}")
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'exit':
                print("Thanks for playing!")
                return
            
            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    score += 1
                    print("Correct!")
                else:
                    print(f"Sorry, the correct answer was {correct_answer}")
                rounds_played += 1
                print(f"Your current score: {score}\n")
            except ValueError:
                print("Please enter a valid number or 'exit' to quit.\n")
        
        print("You've completed 10 rounds!")
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != 'yes':
            print("Thanks for playing!")
            return

if __name__ == "__main__":
    main()
