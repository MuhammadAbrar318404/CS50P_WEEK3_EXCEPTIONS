def main():
    # Call get_items function to start ordering process
    get_items("Items: ")

# Dictionary containing menu items and their prices
items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def get_items(x):
    bill = 0  # Initialize bill to keep track of total cost
    while True:
        try:
            items_var = input(x).title()  # Prompt user to enter item
            if items_var in items:  # Check if item is in the menu
                bill += items[items_var]  # Update total bill
                print(f"Total: ${bill:.2f}")  # Print total bill
            else:
                pass  # Ignore invalid items
        except EOFError:
            break  # End the loop when EOF (Ctrl-D) is encountered

main()  # Call the main function to start the program