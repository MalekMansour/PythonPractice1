# This program prompts the user to input a string containing a bunch of letters. 
# It then counts the occurrences of each letter (case-insensitive), organizes them alphabetically, and prints out the count of each letter.
def count_and_sort_letters(input_string):
    # Convert input string to lowercase to make case-insensitive
    input_string = input_string.lower()
    
    # Initialize a dictionary to store letter counts
    letter_counts = {}
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a letter
        if char.isalpha():
            # Increment the count for this letter in the dictionary
            letter_counts[char] = letter_counts.get(char, 0) + 1
    
    # Sort the dictionary by keys (letters)
    sorted_letter_counts = sorted(letter_counts.items())
    
    # Print the sorted letter counts
    for letter, count in sorted_letter_counts:
        print(f"{letter}: {count}")

# Ask the user for input
user_input = input("Enter a bunch of letters: ")

# Call the function to count and sort letters
count_and_sort_letters(user_input)
