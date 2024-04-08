def main():
    # Get the fuel as a fraction and convert it to percentage
    fuel = get_int() * 100

    # Check the fuel level and print the appropriate message
    if fuel <= 1:
        print("E")  # Empty
    elif 1 < fuel < 99:
        print(f"{round(fuel)}%")  # Print fuel percentage
    else:
        print("F")  # Full

def get_int():
    # Loop until a valid fraction is entered
    while True:
        try:
            # Get input as a fraction
            x, y = input("Fraction: ").split("/")
            x, y = int(x), int(y)
            # Check if the fraction is valid
            if x <= y:
                return x / y
            else:
                pass
        except (ValueError, ZeroDivisionError):
            pass  # Ignore invalid inputs

main()  # Call the main function
