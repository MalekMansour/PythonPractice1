numbers = [1, 2, 3, 4, 5]

# Accessing elements
print(numbers[0])  # Output: 1
print(numbers[2])  # Output: 3
print(numbers[-1]) # Output: 5

numbers = [1, 2, 3, 4, 5]

# Modifying elements
numbers[2] = 10
print(numbers)  # Output: [1, 2, 10, 4, 5]

numbers.append(6) # Adds 6 to the end
print(numbers) # Output: [1, 2, 10, 4, 5, 6]

more_numbers = [7, 8, 9]
combined = numbers + more_numbers
print(combined)  # Output: [1, 2, 10, 4, 5, 6, 7, 8, 9]

length = len(combined)
print(length) # Output: 9
