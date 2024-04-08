def main():
    # Get the grocery list dictionary and sort it alphabetically
    grocery_dict = dict(sorted(get_list().items()))

    # Iterate through the sorted dictionary
    for item in grocery_dict.keys():
        # Print the item along with its count
        print(grocery_dict[item], item)

def get_list():
    grocery_dict = {}  # Initialize an empty dictionary to store grocery items and their counts
    while True:
        try:
            # Get input from user, convert it to uppercase, and remove leading/trailing whitespace
            grocery_items = input().upper().strip()
            if grocery_items in grocery_dict:
                # If the item already exists in the dictionary, increment its count
                grocery_dict[grocery_items] += 1
            else:
                # If the item is not in the dictionary, add it with count 1
                grocery_dict[grocery_items] = 1
        except EOFError:
            break  # Exit the loop if EOF (Ctrl-D) is encountered
    return grocery_dict  # Return the populated grocery list dictionary

main()  # Call the main function to start the program
