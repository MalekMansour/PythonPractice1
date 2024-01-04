# Multiples
user_number1 = int(input("Enter the first number: "))
user_number2 = int(input("Enter the second number: "))

remainder = user_number1 % user_number2

if remainder == 0:
    print(user_number1, "is a multiple of", user_number2)
else:
    print(user_number1, "is NOT a multiple of", user_number2)

print("The remainder is", remainder)
