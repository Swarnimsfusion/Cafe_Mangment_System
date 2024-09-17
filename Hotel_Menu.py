# Defining the Menu Of Cafe.
menu = {
    'Tea': 20,
    'Coffee': 40,
    'Cold Coffee': 60,
    'Salad': 80,
    'Pizza': 110,
    'Burger': 80,
    'Pasta': 110,
}

# Greeting
print("Welcome To Radhe Radhe Cafe")
print("Tea: 20\n\nCoffee: 40\n\nCold Coffee: 60\n\nSalad: 80\n\nPizza: 110\n\nBurger: 80\n\nPasta: 110\n\n")

# Total bill count
order_total = 0

# First item
item_1 = input("Enter The Name Of Item You Want To Order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Order item {item_1} is not available in the menu.")

# Ask for more items
another_order = input("Do you want anything else? (Yes/No): ")
if another_order.lower() == "yes":
    item_2 = input("Enter the 2nd Order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order.")
    else:
        print(f"Item {item_2} is not available.")
elif another_order.lower() != "no":
    print("Invalid response. Please enter 'Yes' or 'No'.")

# Print total amount
print(f"The total amount of items is: {order_total}")
