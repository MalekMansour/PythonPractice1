import random

class Player:
    def __init__(self):
        self.food = random.randint(7, 9)
        self.water = random.randint(5, 6)
        self.days_survived = 0

    def eat(self):
        if self.food > 0:
            self.food -= 1
            print("You ate some food.")
        else:
            print("You have no food to eat.")

    def drink(self):
        if self.water > 0:
            self.water -= 1
            print("You drank some water.")
        else:
            print("You have no water to drink.")

    def eat_and_drink(self):
        self.eat()
        self.drink()

    def status(self):
        print(f"Days Survived: {self.days_survived}")
        print(f"Food remaining: {self.food}")
        print(f"Water remaining: {self.water}")

    def survive_day(self, action):
        print("\nDay", self.days_survived + 1)
        if action == 1:
            self.eat()
        elif action == 2:
            self.drink()
        elif action == 3:
            self.eat_and_drink()
        else:
            print("You did nothing.")

        self.days_survived += 1
        self.status()


def main():
    player = Player()

    while True:
        action = input("\nWhat would you like to do today? (1 for food, 2 for water, 3 for both, 4 for nothing): ")
        if action not in ['1', '2', '3', '4']:
            print("Invalid action. Please choose again.")
            continue

        action = int(action)
        player.survive_day(action)

        if player.food <= 0 and player.water <= 0:
            print("You ran out of food and water. Game over!")
            break


if __name__ == "__main__":
    main()
