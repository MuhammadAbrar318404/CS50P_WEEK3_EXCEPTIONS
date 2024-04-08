# CS50P_WEEK3_EXCEPTIONS
This is week3 of the CS50P which was about the exception, this repo contains the project files that i have designed to implement the theoretical knowledge  


## Fuel Gauge (fuel.py)

The `fuel.py` script prompts the user for a fraction formatted as X/Y, where each of X and Y is an integer, and outputs the fuel level as a percentage rounded to the nearest integer. It indicates "E" if 1% or less fuel remains, "F" if 99% or more fuel remains, and prompts the user again if X or Y is not an integer, X is greater than Y, or Y is 0.

---

## Felipe's Taqueria Order Placer (taqueria.py)

The `taqueria.py` script enables a user to place an order at Felipe's Taqueria by prompting them for items, one per line, until the user inputs Ctrl-D. After each inputted item, it displays the total cost of all items inputted so far, formatted to two decimal places.

---

## Grocery List Generator (grocery.py)

The `grocery.py` script prompts the user for items, one per line, until the user inputs Ctrl-D. It then outputs the user's grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.

---

## Date Formatter (outdated.py)

The `outdated.py` script prompts the user for a date in month-day-year order (e.g., 9/8/1636 or September 8, 1636) and converts it to ISO 8601 format (YYYY-MM-DD), which is an international standard for date formatting.
