def riddle():
    print("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
    answer = input("Your answer: ").lower()
    if answer == "echo":
        print("Congratulations! You solved the riddle.")
    else:
        print("Sorry, that's not correct. Try again!")
        riddle()

riddle()

