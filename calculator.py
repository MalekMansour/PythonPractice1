# Simple Calculator
user_number1 = int(input("Enter the first number: "))
user_number2 = int(input("Enter the second number: "))
user_choice = input("Add, Substract, Multiply, or Divide: ").lower()

if user_choice == "add":
    addition = (user_number1 + user_number2)
    print(user_number1, "+", user_number2, "=", addition)

if user_choice == "substract":
    substraction = user_number1 - user_number2
    print(user_number1, "-", user_number2, "=", substraction)

if user_choice == "multiply":
    multiplication = user_number1 * user_number2
    print(user_number1, "*", user_number2, "=", multiplication)

if user_choice == "divide":
    if user_number2 == 0:
        print("Cannot Divide by 0")
    else:
        division = user_number1 / user_number2
        print(user_number1, "/", user_number2, "=", division)
