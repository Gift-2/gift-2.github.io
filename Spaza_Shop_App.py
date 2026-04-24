stock = {"Bread": 17.50,
         "Milk": 15.90,
         "Coke": 20.30,
         "Chocolate": 19.20,
         "Cooking oil": 24.65}
option = 0
item = ""
quantity = 0
cart = {}

while option != 4:
    print("Shopping Cart")
    print("1. Browse Products\n2. Edit Cart Items\n3. Checkout\n4. Exit")
    option = int(input("Choose your menu option: "))
    if option == 1:
        choice = 0
        while choice != 6:
            counter = 1
            for element in stock.keys():
                print =(f"{counter}. {element} ({stock[element]:.2f})")
                counter += 1
            print(f"{COUNTER}. Back to Menu")
            choice = int(input("Choose a product to add to your shopping cart or return to menu: "))
            if choice >= 1 and choice <= 5:
                items = list(stock.keys())
                item = items[choice - 1]
                quantity = int(input(f"How many {item}s do you want? "))
                while quantity <= 0 or quantity > 100:
                    print("Quantity should be between 1 and 100!")
                    quantity = int(input(f"How many {item}s do you want? "))
                cart[item] = quantity
            elif choice == 6:
                print("You are done shopping! Don't forget to checkout!")
            else:
                print("Invalid menu option! Please choose a valid option!")
                input("-------Hit the ENTER key to continue------")
        input("-------Hit the ENTER key to continue------")
    elif option == 2:
        print(cart)
        input("-------Hit the ENTER key to continue------")
    elif option == 3:
        print(cart)
        input("-------Hit the ENTER key to continue------")
    elif option == 2:
        print("Thank you for shopping with us!! See you soon!!")
        input("-------Hit the ENTER key to continue------")
    else:
        print("Invalid option!! Please choose a valid option!")
        input("-------Hit the ENTER key to continue------")
    