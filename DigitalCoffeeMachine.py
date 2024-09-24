# Importing libraries.
import menu
import time

# Variable to extract and list beverages.
beverages = list(menu.coffee_menu)

# Thought it would make it more realistic.
switch = input("Press Enter to switch on! : ")

# If you 'switch' it on.
if switch.lower() == '':
    print("\nCoffee Menu:")
    number = 0
    # Goes through every item in list.
    for beverage in beverages:
        number += 1                                 # Number of index.
        print(f"({number}) {beverage['name']}")     # Prints every beverage available on menu next to its index.
    # Error handling.
    try:
        choice = int(input("Press the button for your choice ('e.g. 1, 2 or 3') : ")) - 1

        if 0 < choice <= len(beverages):
            drink = beverages[choice]
            print(f"You have chosen {drink['name']}\n"
                  f"Preparing drink...\n")

            # Add function for checking resources.
            time.sleep(2)

            print(f"{drink['name']} is R{float(drink['price']):.2f}"
                  f"")
        else:
            print("Invalid choice. Please select a number from the menu.")

    except ValueError as ve:
        print(f"Please press only the number that is displayed next to your beverage ({ve}).")
