# Palindrome Checker

def palindrome_check():
    while True:
        my_list = input("Input an array of numbers or letters: ")
        print (my_list)
        reversed_list = my_list[::-1]
        
        if reversed_list == my_list:
            print("It is a Palindrome")
        else:
            print("It is not a Palindrome")

palindrome_check()
