import re

def main():
    standard_date()

def standard_date():
    # List of months
    list_months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date:").strip()  # Prompt user for input
            m, d, y = re.split("/| |, ", date)  # Split date into month, day, and year

            if d.isnumeric() and int(d) <= 31:  # Check if day is numeric and within range
                if m.isalpha() and m in list_months and "," in date and "/" not in date:
                    # Check if month is alphabetic, exists in list of months, and the format is month day, year
                    print(f"{y}-{list_months.index(m)+1:02}-{int(d):02}")  # Print ISO 8601 formatted date
                    break  # Exit loop
                elif m.isnumeric() and int(m) <= 12:
                    # Check if month is numeric and within range
                    print(f"{y}-{int(m):02}-{int(d):02}")  # Print ISO 8601 formatted date
                    break  # Exit loop
                else:
                    pass  # Ignore invalid input
            else:
                pass  # Ignore invalid input
        except TypeError:
            pass  # Ignore type errors

main()  # Call the main function to start the program
