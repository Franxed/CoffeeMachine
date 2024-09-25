# Importing libraries.
import menu
import time

# Variable to extract and list beverages.
beverages = list(menu.coffee_menu)

# Coffe Machine's Resources.
coffee_m_resources = {
    "water": 1420,
    "coffee": 60,
    "sugar": 100,
    "milk": 300
}

# Thought it would make it more realistic.
switch = input("Press Enter to switch on! : ").lower()


# For admin to check resources.
def admin():
    print("\nResources:\n"
          f"Water: {coffee_m_resources['water']}ml\n"
          f"Coffee: {coffee_m_resources['coffee']}g\n"
          f"Sugar: {coffee_m_resources['sugar']}g\n"
          f"Milk: {coffee_m_resources['milk']}ml\n")
    exit()


# Function to display the coffee menu.
def display_menu():
    print("\nCoffee Menu:")
    for number, beverage in enumerate(beverages, start=1):
        print(f"({number}) {beverage['name']}")


# Function to get user's choice from the menu.
def get_user_choice():
    try:
        choice = int(input("Press the button for your choice ('e.g. 1, 2 or 3') : "))
        if 0 < choice <= len(beverages):
            return choice - 1
        else:
            print("Invalid choice. Please select a number from the menu.")
            return None
    except ValueError:
        print("Please press only the number that is displayed next to your beverage.")
        return None


# Function to check if resources are sufficient for the selected beverage.
def resource_check(drink):
    for ingredient, amount in drink['ingredients'].items():
        if ingredient in coffee_m_resources:
            if coffee_m_resources[ingredient] < amount:
                print(f"Sorry, not enough {ingredient}!")
                return False
    return True


# Function to prepare the drink.
def prepare_drink(drink):
    print(f"\nYou have chosen {drink['name']}\nPreparing drink...\n")

    for ingredient, amount in drink['ingredients'].items():
        if ingredient in coffee_m_resources:
            coffee_m_resources[ingredient] -= amount  # Deduct used ingredients
            print(f"{ingredient} used: {amount}ml/g")

    time.sleep(3)
    print(f"\n{drink['name']} is ready!")


def cash_change(drink):
    print(f"Price: R{float(drink['price']):.2f}")
    cash = float(input("Type Amount: R "))
    change = cash - float(drink['price'])
    if change >= 0:
        print(f"\nReturning change: R{change:.2f}")
        print("Thank you for ordering! Enjoy your day!\n")
        return change
    else:
        print("Insufficient funds. Please insert more money.")
        print(f"Required : R{change}")
        return None


# Main coffee machine function to control the flow.
def coffee_machine():
    while True:
        if switch == "":
            display_menu()                  # Display menu.
            choice = get_user_choice()      # Get user choice.

            if choice is not None:
                drink = beverages[choice]

                # Check if enough resources are available
                if resource_check(drink):
                    prepare_drink(drink)
                    cash_change(drink)
                    break
                else:
                    print(f"Cannot prepare {drink['name']} due to insufficient resources.")
                    continue

        elif switch == "admin":
            admin()

        else:
            print("Switching off.")
            break


# Call the main coffee machine function.
coffee_machine()
