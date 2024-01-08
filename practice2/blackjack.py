import random
import time

# List of hands possible
cards =("2", "3", "4", "5", "6", "7", "8", "9", "10", "11" )

# Set the username
print('Welcome to BlackJack')
setusername = input('Set your Username: ')
time.sleep(0.50)

# variables
balance = 1000
username = setusername
random_hand1 = random.choice(cards) 
random_hand2 = random.choice(cards)
user_hand = [random_hand1]
dealer_hand = [random_hand2]
card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "11": 11}

# User choose to start the game or quit
print((f'Username: {username}' ))
print('1: Start Game')
print('2: Quit')

while True:
    choice = input("Enter your choice: ")
    if choice == '2':
        print("Quitting... ")
        quit()
    if choice == '1':
        break
    else:
        print('Invalid choice. Please enter 1 or 2.')

# If user starts the game
print('Entering Blackjack...')
time.sleep(1.5)

# betting the money
while True:
    try:
        bet = int(input(f'You have {balance} coins. Place your bet: '))
        if bet > balance:
            print("You don't have enough coins. ")
        else:
            break
    except ValueError:
        print('Invalid. Enter a valid number of coins. ')

print("Shuffling Deck... ")           
time.sleep(1.5)          
print((f"Your hand: {user_hand} "))
print((f"Dealer's hand: {dealer_hand[0]} + ? "))

# hit or stand
user_hand_value = card_values[user_hand[0]]
while True:
    usermove = input("Hit or Stand?: ").lower()
    move = usermove

    if move == "hit":
        new_card = random.choice(cards)
        user_hand.append(new_card)
        user_hand_value += card_values[new_card]
        print(f"Your hand: {user_hand} ({user_hand_value})")
        if user_hand_value > 21:
            print("Bust! You lose.")
            balance -= bet
            print((f"You now have {balance} coins "))
            break

    elif move == "stand":
        print("Dealer's hand: ", dealer_hand)
        dealer_hand_value = card_values[dealer_hand[0]]
        while dealer_hand_value < 17:
            dealer_new_card = random.choice(cards)
            dealer_hand.append(dealer_new_card)
            dealer_hand_value += card_values[dealer_new_card]
            print("Dealer hits: ", dealer_new_card)
            time.sleep(1)

        print("Dealer's hand: ", dealer_hand, "(", dealer_hand_value, ")")
        if dealer_hand_value > 21:
            print("Dealer busts! You win.")
            balance += bet
            print((f"You now have {balance} coins "))
        elif dealer_hand_value < user_hand_value:
            print("You win!")
            balance += bet
            print((f"You now have {balance} coins "))
        elif dealer_hand_value > user_hand_value:
            print("Dealer wins. You lose.")
            balance -= bet
            print((f"You now have {balance} coins "))
        else:
            print("It's a tie.")
            print((f"You now have {balance} coins "))
        break

    else:
        print('Invalid. Enter Hit or Stand. ')
