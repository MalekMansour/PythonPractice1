import random
# suits and ranks
suits = ("♡", "♤", "♢", "♧")
ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
# choose a random card and shows it
Family = random.choice(suits)
No = random.choice(ranks)
print(No, Family)
