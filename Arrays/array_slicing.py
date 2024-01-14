# Create a list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
subset1 = my_list[2:6]  # Elements at index 2, 3, 4, 5
print(subset1)  # Output: [2, 3, 4, 5]

# Omitting start or stop
subset2 = my_list[:5]  # Elements at index 0, 1, 2, 3, 4
subset3 = my_list[5:]  # Elements at index 5, 6, 7, 8, 9
print(subset2)  # Output: [0, 1, 2, 3, 4]
print(subset3)  # Output: [5, 6, 7, 8, 9]

# Using negative indices
subset4 = my_list[-3:]  # Elements at the last three indices
print(subset4)  # Output: [7, 8, 9]

# Using step
subset5 = my_list[1:9:2]  # Elements at index 1, 3, 5, 7
print(subset5)  # Output: [1, 3, 5, 7]

# Reverse a list using slicing
reversed_list = my_list[::-1]
print(reversed_list)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
