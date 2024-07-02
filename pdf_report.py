import os
import webbrowser
from fpdf import FPDF

class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such as their names, their due amount and the period of the bill.
    """

    def __init__(self, filenames):
        # Initialize PdfReport with a filename
        self.filename = filenames

    def generate(self, flatmate_1, flatmate_2, bill):
        # Generate PDF report with details of flatmates and bill

        # Calculate amounts to be paid by each flatmate
        flatmate_1_pay = str(round(flatmate_1.pays(bill, flatmate_2),2))
        flatmate_2_pay = str(round(flatmate_2.pays(bill, flatmate_1),2))

        # Create a new PDF document
        pdf = FPDF( orientation = "P", unit = "pt", format = 'A4')
        pdf.add_page()

        # Add Icon
        try:
            pdf.image(os.path.join('resources', 'house.png'), w=50, h=50)
        except FileNotFoundError:
            print("Error: The file 'house.png' was not found in the resources folder.")
            return

        # Insert title in PDF
        pdf.set_font(family = "Times", size = 24, style = 'B')
        pdf.cell(w = 0, h=80, txt = "Split Bill", border = 0, align= 'C', ln=1)

        # Insert Period label and value
        pdf.set_font(family = "Times", size = 15, style = 'B')
        pdf.cell(w = 408, h=30, txt = "Duration", border = 0)
        pdf.cell(w = 130, h=30, txt = bill.period, border = 0, ln = 1)

        # Insert Expense Type label and value
        pdf.set_font(family="Times", size=15, style='B')
        pdf.cell(w=408, h=30, txt="Expense Type", border=0)
        pdf.cell(w=130, h=40, txt=bill.expense_type, border=0, ln=1)
        
        # Insert name and due amount of the first flatmate
        pdf.set_font(family = "Times", size = 12)
        pdf.cell(w = 150, h=25, txt = flatmate_1.name, border = 0)
        pdf.cell(w = 130, h=25, txt = flatmate_1_pay, border = 0, ln = 1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w = 150, h=25, txt = flatmate_2.name, border = 0)
        pdf.cell(w = 130, h=25, txt = flatmate_2_pay, border = 0, ln=1)

        # Set author information for the PDF
        pdf.set_author('SHUBHAM VAISHNAV')

        # Define output path for the generated PDF report
        output_path = os.path.join('resources', 'output', self.filename)
        try:
                pdf.output(output_path)
                webbrowser.open(output_path)
        except PermissionError:
                print("Permission error: Unable to write to the file. Please check file permissions.")
        except OSError as e:
                print(f"OS error: {e}")