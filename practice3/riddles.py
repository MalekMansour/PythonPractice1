import random

def riddle1():
    print("Riddle 1: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
    answer = input("Your answer: ").lower()
    if answer == "echo":
        print("Congratulations! You solved the riddle.")
    else:
        print("Sorry, that's not correct.")

def riddle2():
    print("Riddle 2: What has keys but can't open locks?")
    answer = input("Your answer: ").lower()
    if answer == "keyboard":
        print("Congratulations! You solved the riddle.")
    else:
        print("Sorry, that's not correct.")

def riddle3():
    print("Riddle 3: The more you take, the more you leave behind. What am I?")
    answer = input("Your answer: ").lower()
    if answer == "footsteps":
        print("Congratulations! You solved the riddle.")
    else:
        print("Sorry, that's not correct.")

riddles = [riddle1, riddle2, riddle3]
random.shuffle(riddles)

for riddle_func in riddles:
    riddle_func()
