import random

def riddle1():
    print("Riddle 1: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
    answer = input("Your answer: ").lower()
    if answer == "echo":
        print("Congratulations! You solved the riddle.")
        return True
    else:
        print("Sorry, that's not correct.")
        return False

def riddle2():
    print("Riddle 2: What has keys but can't open locks?")
    answer = input("Your answer: ").lower()
    if answer == "keyboard":
        print("Congratulations! You solved the riddle.")
        return True
    else:
        print("Sorry, that's not correct.")
        return False

def riddle3():
    print("Riddle 3: The more you take, the more you leave behind. What am I?")
    answer = input("Your answer: ").lower()
    if answer == "footsteps":
        print("Congratulations! You solved the riddle.")
        return True
    else:
        print("Sorry, that's not correct.")
        return False

def play_again():
    choice = input("Do you want to play again? (yes/no): ").lower()
    return choice == "yes"

# List of riddles
riddles = [riddle1, riddle2, riddle3]

play = True
while play:
    # Shuffle the list of riddles
    random.shuffle(riddles)

    # Ask the user to solve each riddle
    for riddle_func in riddles:
        solved = riddle_func()
        if not solved:
            break
    
    play = play_again()

print("Thank you for playing!")
