import random

def generate_equation():
    """Generate a random equation for the game."""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    
    # Avoid division by zero
    if operator == '/' and num2 == 0:
        num2 = random.randint(1, 10)
    
    equation = f"{num1} {operator} {num2}"
    result = eval(equation)
    return equation, result

def main():
    print("Welcome to the Math Puzzle Game!")
    print("Solve the equations to win!")
    score = 0
    while True:
        equation, correct_answer = generate_equation()
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
