def get_float(prompt):
    # Function to get a valid float input from the user
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("The amount must be greater than zero.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

def get_int(prompt):
    # Function to get a valid integer input from the user
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("The number of days must be non-negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid integer.")

def get_non_empty_string(prompt):
    # Function to get a non-empty string input from the user
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be empty or just whitespace. Please enter a valid string.")
            continue
        if all(char.isalpha() or char.isspace() for char in value):
            return value
        else:
            print("Invalid input. Please enter a string with alphabetic characters only.")

def validate_period(period):
    # Function to validate the period format (Month Year)
    parts = period.split()

    if len(parts) != 2:
        return False

    month, year = parts

    valid_months = [
        "january", "february", "march", "april",
        "may", "june", "july", "august",
        "september", "october", "november", "december"
    ]

    if month.lower() not in valid_months:
        return False

    if not year.isdigit() or len(year) != 4:
        return False
    
    if year == '0000' or year.startswith('0'):
            return False

    return True