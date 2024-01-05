temp = float(input("Enter a temperature: "))
temp_type = input("Was it (F)ahrenheit or (C)elsius?: ").upper()
if temp_type == "F":
    C = (temp - 32) * 5/9
    print(temp, "Fahrenheit in Celsius is", C)
else:
    F = (temp * 9/5) + 32
    print(temp, "Celsius in Fahrenheit is", F)
