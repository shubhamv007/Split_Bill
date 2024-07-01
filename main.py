from fpdf import FPDF

class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name 
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate_2):
        weight = self.days_in_house / (self.days_in_house + flatmate_2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such as their names, their due amount and the period of the bill.
    """

    def __init__(self, filenames):
        self.filename = filenames

    def generate(self, flatmate_1, flatemate_2, bill):
        pdf = FPDF( orientation = "P", unit = "pt", format = 'A4')
        pdf.add_page()

        # Insert title
        pdf.set_font(family = "Times", size = 24, style = 'B')
        pdf.cell(w = 0, h=80, txt = "Flatmate Bill", border = 1, align= 'C', ln=1)

        # Insert Period label and value
        pdf.cell(w = 100, h=40, txt = "Period", border = 1)
        pdf.cell(w = 130, h=40, txt = bill.period, border = 1)
        
        # Insert name and due amount of the first flatmate
        pdf.cell(w = 100, h=40, txt = flatmate_1.name, border = 1)
        pdf.cell(w = 130, h=40, txt = str(flatmate_1.pays(bill, flatemate_2)), border = 1)

        # Inserted Author
        pdf.set_author('SHUBHAM VAISHNAV')
        pdf.output(self.filename)