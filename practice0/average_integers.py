number = int(input("Input a number: "))
if number <= 1:
    print("Number has to be bigger than 1.")
else:
    total = 0
    for i in range(1, 1+number):
        total += i
    
    print("Sum:",total)
    average = total / number
    print("Average:", average)
