import random

def generate_equation(difficulty):
    """Generate a random equation based on difficulty."""
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
    print("Choose your difficulty: easy, normal, or hard")
    difficulty = input("Difficulty: ").lower()
    if difficulty not in ['easy', 'normal', 'hard']:
        print("Invalid difficulty level! Please choose again.")
        return
    
    print(f"You've chosen {difficulty} difficulty. Solve the equations to win!")
    score = 0
    while True:
        equation, correct_answer = generate_equation(difficulty)
        print(f"Equation: {equation}")
        user_answer = input("Your answer: ")
        if user_answer.lower() == 'exit':
            print("Thanks for playing!")
            break
        try:
            user_answer = float(user_answer)
            if user_answer == correct_answer:
                score += 1
                print("Correct!")
            else:
                print(f"Sorry, the correct answer was {correct_answer}")
            print(f"Your current score: {score}\n")
        except ValueError:
            print("Please enter a valid number or 'exit' to quit.\n")

if __name__ == "__main__":
    main()
