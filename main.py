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

    def generate(self, flatmate_1, flatmate_2, bill):

        flatmate_1_pay = str(round(flatmate_1.pays(bill, flatmate_2),2))
        flatmate_2_pay = str(round(flatmate_2.pays(bill, flatmate_1),2))

        pdf = FPDF( orientation = "P", unit = "pt", format = 'A4')
        pdf.add_page()

        # Add Icon
        pdf.image("house.png", w=50, h=50)

        # Insert title
        pdf.set_font(family = "Times", size = 24, style = 'B')
        pdf.cell(w = 0, h=80, txt = "Flatmate Bill", border = 0, align= 'C', ln=1)

        # Insert Period label and value
        pdf.set_font(family = "Times", size = "15", style = 'B')
        pdf.cell(w = 100, h=40, txt = "Period", border = 0)
        pdf.cell(w = 130, h=40, txt = bill.period, border = 0)
        
        # Insert name and due amount of the first flatmate
        pdf.set_font(family = "Times", size = "12")
        pdf.cell(w = 100, h=25, txt = flatmate_1.name, border = 0)
        pdf.cell(w = 130, h=25, txt = flatmate_1_pay, border = 0)

        # Insert name and due amount of the second flatmate
        pdf.cell(w = 100, h=25, txt = flatmate_2.name, border = 0)
        pdf.cell(w = 130, h=25, txt = flatmate_2_pay, border = 0)

        # Inserted Author
        pdf.set_author('SHUBHAM VAISHNAV')
        pdf.output(self.filename)