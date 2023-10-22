BASE_URL = "https://www.booking.com/"

# Input for destination
DESTINATION = input("Enter your destination: ").capitalize()

# Input for check-in date
check_in = input("Enter a date for check in (e.g., 2023-12-5): ")
CHECK_IN_YEAR, CHECK_IN_MONTH, CHECK_IN_DAY = check_in.split('-')

# Input for check-out date
check_out = input("Enter a date for check out (e.g., 2023-12-30): ")
CHECK_OUT_YEAR, CHECK_OUT_MONTH, CHECK_OUT_DAY = check_out.split('-')

# Input for the number of results to display
LIMIT_SEARCH = int(input("How many hotel results would you like to see: "))

# Input for currency choice
CURRENCY = input("Choose your preferred currency (USD / EURO / ILS): ").upper()

# Input for the maximum price per night
MAX_PRICE = int(input("Enter the maximum price per night: "))

# 2 adults · 0 children · 1 room
travelers = input("Please enter the number of travelers in the format 'adults-children-rooms' : ")
ADULTS, CHILDREN, ROOMS = map(int, travelers.split('-'))
if CHILDREN == 1 :
    CHILDREN_AGE = int(input("Enter child age (1 to 17): "))

