from bill import Bill
from flatmate import flatmate
from pdf_report import PdfReport

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")
def main():
    amount = float(input("Hey user, Enter the bill amount: "))
    period = input("What is the bill period? E.g. December 2020: ")

    name_1 = input("What is your name? ")
    days_in_house_1 = int(input(f"How many days did {name_1} stay in the house during the bill period? "))

    name_2 = input("What is the name of other flatmate? ")
    days_in_house_2 = int(input(f"How many days did {name_2} stay in the house during the bill period? "))

    the_bill = Bill(amount, period)
    flatmate1 = flatmate(name_1, days_in_house_1)
    flatmate2 = flatmate(name_2, days_in_house_2)

    print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, flatmate2))
    print(f"{flatmate2.name} pays: ", flatmate2.pays(the_bill, flatmate1))

    pdf_report = PdfReport(filenames=f"{the_bill.period}.pdf")
    pdf_report.generate(flatmate1, flatmate2, the_bill)

if __name__ == "__main__":
    main()