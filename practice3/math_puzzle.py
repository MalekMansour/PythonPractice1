import random

def generate_equation(difficulty):
    if difficulty == 'easy':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif difficulty == 'normal':
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
    elif difficulty == 'hard':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
    else:
        raise ValueError("Invalid difficulty level!")
    
    operator = random.choice(['+', '-', '*', '/'])
    
    # Avoid division by zero
    if operator == '/' and num2 == 0:
        num2 = random.randint(1, 100)
    
    equation = f"{num1} {operator} {num2}"
    result = eval(equation)
    return equation, result

def main():
    print("Welcome to the Math Puzzle Game!")
    while True:
        print("Choose your difficulty: easy, normal, or hard")
        difficulty = input("Difficulty: ").lower()
        if difficulty not in ['easy', 'normal', 'hard']:
            print("Invalid difficulty level! Please choose again.")
            continue
        
        print(f"You've chosen {difficulty} difficulty. Solve the equations to win!")
        score = 0
        rounds_played = 0
        while rounds_played < 10:
            equation, correct_answer = generate_equation(difficulty)
            print(f"Equation: {equation}")
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'exit':
                print("Thanks for playing!")
                return
            
            try:
                user_answer = float(user_answer)
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
