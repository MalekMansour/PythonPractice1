# SHARP CALCULATOR
# Translates the amount of "#" into numbers and performs the calculation

def calculate_expression(expression):
    replaced_expression = ""
    current_count = 0

    for char in expression:
        if char == '#':
            current_count += 1
        else:
            if current_count > 0:
                replaced_expression += str(current_count)
                current_count = 0
            replaced_expression += char

    if current_count > 0:
        replaced_expression += str(current_count)

    result = eval(replaced_expression)
    return result

if __name__ == "__main__":
    user_input = input("Enter the expression (e.g., #### + ##): ")

    try:
        answer = calculate_expression(user_input)
        print(f"The answer is: {answer}")
    except (SyntaxError, NameError):
        print("Invalid input. Please use the specified format (# for counting, + for addition).")
