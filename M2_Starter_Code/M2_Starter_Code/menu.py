# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order = []

# Launch the store and present a greeting to the customer
print("Welcome to Glue Sniffers' Snack Shop!!")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("\nWhat menu will you be choosing from? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(str(i) + ":" + key)
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Enter Menu Number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"\nYou entered {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item #   Item name                 Price")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # 2. Ask customer to input menu item number
            menu_selection = input("\nWhat would you like?: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert to integer
                menu_selection = int(menu_selection)  

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items.keys():
                    # Store item
                    item = menu_items[menu_selection]  
                    # Store the item name
                    item_name = item["Item name"]  
                    item_price = item["Price"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {item_name} you want? (default 1): ")

                    # Check if the quantity is a number, default to 1 if not
                    if not quantity.isdigit():
                        print("Invalid quantity, defaulting to 1.")
                        quantity = 1
                    else:
                        quantity = int(quantity)

                    # Add the item name, price, and quantity to the order list
                    order.append({
                        "Item name": item_name,
                        "Price": item_price,
                        "Amount": quantity
                    })
                    print(f"Added {quantity} x {item_name} to your order.")
                    
    while True:
        # Ask the customer if they would like to order anything else
        cont_ordering = input("\nWould you like to keep ordering? (Y)es or (N)o ").lower()

        # 5. Check the customer's input
        if cont_ordering == 'y':
            break  # Keep ordering
        elif cont_ordering == 'n':
            place_order = False
            break  # Exit ordering loop
        else:
            print("Invalid input. Please type 'Y' for yes or 'N' for no.")

# Print out the customer's order
print("\nThis is what you ordered.:\n")

print("Item name                | Amount | Price")

# 6. Loop through the items in the customer's order
for item in order:
    # 7. Store the dictionary items as variables
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Amount"]

    # 8. Calculate the number of spaces for formatted printing
    item_name_spaces = " " * (25 - len(item_name))
    price_spaces = " " * (7 - len(f"${price:.2f}"))

    # 9. Create space strings
    formatted_item = f"{item_name}{item_name_spaces}| {quantity}      | ${price:.2f}{price_spaces} "

    # 10. Print the item name, price, and quantity
    print(formatted_item)

# 11. Calculate the cost of the order using list comprehension
total_price = sum(item["Price"] * item["Amount"] for item in order)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Total: ${total_price:.2f}")
print("Thank you for purchasing from Glue Sniffers!")
