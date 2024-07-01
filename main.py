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

    def pays(self, bill):
        pass


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such as their names, their due amount and the period of the bill.
    """

    def __init__(self, filenames):
        self.filename = filenames

    def generate(self, flatmate_1, flatemate_2, bill):
        pass