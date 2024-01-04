def shop():
  money = 100.0
  while True:
    if money <= 0:
       print("You ran out of money")
       quit()
    else:   
        print("Your Money: ", money)
        print("Welcome to the Donut Shop!")
        print("1. Plain, 2. Chocolate, 3. Vanilla, 4. Honey Glaze")
        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            print("1 Plain Donut")
            money -= 3.50
        elif user_choice == 2:
            print("1 Chocolate Donut")
            money -= 3.75
        elif user_choice == 3:
            print("1 Vanilla Donut")
            money -= 4.0
        elif user_choice == 4:
            print("1 Honey Glaze Donut")
            money -= 4.50
        else:
            print("Invalid Choice")
shop()
