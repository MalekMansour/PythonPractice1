# Basic Fighter Game with 6 characthers
# ARPG
import random
import time
# main menu
print("Welcome to ARPG Fighter 1")
# ARPG stands for Ayame, Ryuke, Power, Gud (assuming these are the main characthers)
characthers = ("Ayame ", "Akira", "Ryuke ", "Aiko", "Power", "Gud")
print("(1. Ayame) (2. Akira) (3. Ryuke) (4. Aiko) (5. Power) (6. Gud) ")
# The Attacks
attacks = ("Cyclone Kick", "Shadow Strike", "Blazing Inferno", "Thundering Fist", "Cosmic Wave", "Demon Slash", "Infernal Claw", "Dragon Fang", "Supernova Blast")
randomattack1 = random.choice(attacks)
randomattack2 = random.choice(attacks)
randomattack3 = random.choice(attacks)
randomattack4 = random.choice(attacks)
randomattack5 = random.choice(attacks)
# User picks a characther for himself
while True: 
    userpick = input("Pick your characther: ")
    if userpick == "1":
        print("You picked Ayame. ")
        break
    if userpick == "2":
        print("You picked Akira. ")
        break
    if userpick == "3":
        print("You picked Ryuke. ")
        break
    if userpick == "4":
        print("You picked Aiko. ")
        break
    if userpick == "5":
        print("You picked Power. ")
        break
    if userpick == "6":
        print("You picked Gud. ")
        break
    else:
        print("Invalid characther.")

# Pick a random fighter as opponent
opponent = random.choice(characthers)
print((f"Your opponent is {opponent}."))
# User picks between start the fight or quit
while True: 
    start = input("Would you like to start the fight? (y/n): ")
    if start == "n": 
        quit()
    if start == "y":
        print("Loading...")
        time.sleep(2)
        print("Fight Started! Go! ")
        break
    else:
        print("Invalid choice.")
# the fight starts
userhealth = 100
opponenthealth = 100
# the main game loop
print((f"Your health is {userhealth} "))
time.sleep(1)
print((f"{opponent} uses {randomattack5} "))
userhealth -= 20
if userhealth < 1:
 print((f"Game over. You lose. {opponent} has won the fight. "))
 quit()
    
time.sleep(1)
print((f"Your health is {userhealth} "))
time.sleep(1)

print("Your turn.")
userattack = input("Pick a move (1, 2, 3, 4): ")
if userattack == "1":
    print((f"You used {randomattack1} "))
    opponenthealth -= 10
if userattack == "2":
    print((f"You used {randomattack2} "))
    opponenthealth -= 20
if userattack == "3":
    print((f"You used {randomattack3} "))
    opponenthealth -= 30
if userattack == "4":
    print((f"You used {randomattack4} "))
    opponenthealth -= 40
time.sleep(1)

if opponenthealth < 1:
    print("K.O. You win! ")
    quit()
    
print((f"{opponent} has {opponenthealth} of health left. "))
#maingameloop2
time.sleep(1)
print((f"{opponent} uses {randomattack3} "))
userhealth -= 30

if userhealth < 1:
    print("Game over. You lose. ")
    quit()
    
print((f"Your health is {userhealth} "))
print("Your turn.")

userattack = input("Pick a move (1, 2, 3, 4): ")
if userattack == "1":
    print((f"You used {randomattack1} "))
    opponenthealth -= 10
if userattack == "2":
    print((f"You used {randomattack2} "))
    opponenthealth -= 20
if userattack == "3":
    print((f"You used {randomattack3} "))
    opponenthealth -= 30
if userattack == "4":
    print((f"You used {randomattack4} "))
    opponenthealth -= 40
time.sleep(1)

if opponenthealth < 1:
    print("K.O. You win! ")
    quit()
    
print((f"{opponent} has {opponenthealth} of health left. "))
#maingameloop3
time.sleep(1)
print((f"{opponent} uses {randomattack2} "))
userhealth -= 40

if userhealth < 1:
     print((f"Game over. You lose. {opponent} has won the fight. "))
     quit()

print((f"Your health is {userhealth} "))
print("Your turn.")

userattack = input("Pick a move (1, 2, 3, 4): ")
if userattack == "1":
    print((f"You used {randomattack1} "))
    opponenthealth -= 10
if userattack == "2":
    print((f"You used {randomattack2} "))
    opponenthealth -= 20
if userattack == "3":
    print((f"You used {randomattack3} "))
    opponenthealth -= 30
if userattack == "4":
    print((f"You used {randomattack4} "))
    opponenthealth -= 40
time.sleep(1)

if opponenthealth < 1:
    print("K.O. You win! ")
    quit()
    
print((f"{opponent} has {opponenthealth} of health left. "))
#maingameloop4
time.sleep(1)
print((f"{opponent} uses {randomattack4} "))
userhealth -= 20

if userhealth < 1:
    print((f"Game over. You lose. {opponent} has won the fight. "))
    quit()

print((f"Your health is {userhealth} "))
print("Your turn.")

userattack = input("Pick a move (1, 2, 3, 4): ")
if userattack == "1":
    print((f"You used {randomattack1} "))
    opponenthealth -= 10
if userattack == "2":
    print((f"You used {randomattack2} "))
    opponenthealth -= 20
if userattack == "3":
    print((f"You used {randomattack3} "))
    opponenthealth -= 30
if userattack == "4":
    print((f"You used {randomattack4} "))
    opponenthealth -= 40
time.sleep(1)

if opponenthealth < 1:
    print("K.O. You win! ")
    quit()
    
print((f"{opponent} has {opponenthealth} of health left. "))
# end
