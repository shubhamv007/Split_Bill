from utils import get_float, get_int, get_non_empty_string, validate_period
from bill import Bill
from flatmate import flatmate
from pdf_report import PdfReport

def main():
    # Get the bill amount from the user
    amount = get_float("Hey user, Enter the bill amount: ")

    # Get the bill period from the user with validation
    while True:
        period = input("What is the bill period? E.g. December 2023: ")
        if validate_period(period):
            break
        else:
            print("Invalid period format. Please enter the period in the format: Month Year")

     # Get the type of expense from the user
    expense_type = get_non_empty_string("What type of expense is this? E.g. Rent, Utilities, Groceries: ")
    
    # Get details of the first flatmate
    name_1 = get_non_empty_string("What is your name? ")
    days_in_house_1 = get_int(f"How many days did {name_1} stay in the house during the {expense_type.lower()} bill period? ")

    # Get details of the second flatmate
    name_2 = get_non_empty_string("What is the name of other flatmate? ")
    days_in_house_2 = get_int(f"How many days did {name_2} stay in the house during the {expense_type.lower()} bill period? ")

    # Create instances of Bill and flatmates
    bill = Bill(amount, period, expense_type)
    flatmate1 = flatmate(name_1, days_in_house_1)
    flatmate2 = flatmate(name_2, days_in_house_2)

    # Calculate and display each flatmate's payment
    print(f"{flatmate1.name} pays: {flatmate1.pays(bill, flatmate2):.2f} ")
    print(f"{flatmate2.name} pays: {flatmate2.pays(bill, flatmate1):.2f} ")

    # Generate PDF report
    pdf_report = PdfReport(filenames=f"{bill.period}_{bill.expense_type}.pdf")
    try:
        pdf_report.generate(flatmate1, flatmate2, bill)
    except Exception as e:
        print(f"Error occurred while generating the PDF report: {e}")

if __name__ == "__main__":
    main()