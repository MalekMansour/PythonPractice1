import os
import random

class Player:
    def __init__(self):
        self.food = random.randint(7, 9)
        self.water = random.randint(5, 6)
        self.days_without_food = 0
        self.days_without_water = 0
        self.days_survived = 0

    def eat(self):
        if self.food > 0:
            self.food -= 1
            self.days_without_food = 0  # Reset days without food
            print("You ate some food.")
        else:
            print("You have no food to eat.")
            self.days_without_food += 1

    def drink(self):
        if self.water > 0:
            self.water -= 1
            self.days_without_water = 0  # Reset days without water
            print("You drank some water.")
        else:
            print("You have no water to drink.")
            self.days_without_water += 1

    def eat_and_drink(self):
        self.eat()
        self.drink()

    def status(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
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
        self.check_survival()

    def choose_crate(self):
        choice = input("\nYou survived 10 days! Choose a crate (1, 2, 3) or type 'nothing': ")
        if choice == 'nothing':
            print("You chose not to take anything from the crates.")
            return

        crate_number = int(choice)
        if crate_number in [1, 2, 3]:
            food_found = random.randint(1, 10)
            water_found = random.randint(1, 10)
            self.food += food_found
            self.water += water_found
            print(f"You found {food_found} food and {water_found} water in crate {crate_number}!")
        else:
            print("Invalid choice. You chose not to take anything from the crates.")

    def check_survival(self):
        if self.days_without_water >= 6:
            print("You died of dehydration. Game over!")
            exit()
        elif self.days_without_food >= 8:
            print("You died of starvation. Game over!")
            exit()

    def reset_days_without_food(self):
        self.days_without_food = 0

    def reset_days_without_water(self):
        self.days_without_water = 0


def main():
    player = Player()

    while True:
        action = input("\nWhat would you like to do today? (1 for food, 2 for water, 3 for both, 4 for nothing): ")
        if action not in ['1', '2', '3', '4']:
            print("Invalid action. Please choose again.")
            continue

        action = int(action)
        if action in [1, 2, 3]:
            if action == 1:
                player.eat()
                player.reset_days_without_food()
            elif action == 2:
                player.drink()
                player.reset_days_without_water()
            elif action == 3:
                player.eat_and_drink()
                player.reset_days_without_food()
                player.reset_days_without_water()
        elif action == 4:
            print("You did nothing.")

        player.days_survived += 1
        player.check_survival()
        player.status()

        if player.days_survived % 10 == 0:
            player.choose_crate()


if __name__ == "__main__":
    main()
