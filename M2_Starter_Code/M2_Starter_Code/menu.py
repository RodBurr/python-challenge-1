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
print("Welcome to Glue Sniffers' Snack Shack!!")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("What menu will you be choosing from? ")
    print("~" * 42)

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
    print("~" * 42)

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
            print(f"\nWhat {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # |Items                      |Price")
            print("~" * 42)
    
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 25 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 25 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            print( "~" * 42)

            # 2. Ask customer to input menu item number
            menu_select = input("Please select item number.: ")

            # 3. Check if the customer typed a number
            if menu_select.isdigit():
                # Convert to integer
                menu_select = int(menu_select)  

                # 4. Check if the menu selection is in the menu items
                if menu_select in menu_items.keys():
                    # Store item
                    item = menu_items[menu_select]  
                    # Store the item name
                    item_name = item["Item name"]  
                    item_price = item["Price"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"\nHow many {item_name} do you want?: ")

                    # Check if the quantity is a number, default to 1 if not
                    if not quantity.isdigit():
                        print("Error, defaulting to 1.")
                        quantity = 1
                    else:
                        quantity = int(quantity)

                    # Add the item name, price, and quantity to the order list
                    order.append({
                        "Item name": item_name,
                        "Price": item_price,
                        "Quantity": quantity
                    })
                    print(f"\nAdded {quantity} {item_name} to your order.")
                    
    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to order anything else? (Y)es or (N)o ")

        # 5. Check the customer's input
        match keep_ordering.lower():
            case 'y':
                place_order = True
                break # Keep ordering
            case 'n':
                place_order = False
                break # Exit ordering loop
            case _:
                print("Error. Please type 'Y' for yes or 'N' for no.")
# Print out the customer's order
print("Thank you for your order!!!:")
print("~" * 42)

print("Item                     | Quantity | Price")

# 6. Loop through the items in the customer's order
for item in order:
    # 7. Store the dictionary items as variables
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    item_name_spaces = " " * (25 - len(item_name))
    price_spaces = " " * (5 - len(f"${price:.2f}"))

    # 9. Create space strings
    formatted_item = f"{item_name}{item_name_spaces}| {quantity}        | ${price:.2f}{price_spaces} "

    # 10. Print the item name, price, and quantity
    print(formatted_item)
# 11. Calculate the cost of the order using list comprehension
total_price = sum(item["Price"] * item["Quantity"] for item in order)
print("~" * 42)
print(f"\nTotal: ${total_price:.2f}")
print("Thank you for purchasing from Glue Sniffers!")
