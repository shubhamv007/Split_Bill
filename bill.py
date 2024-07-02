class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """

    def __init__(self, amount, period, expense_type):
        # Initialize Bill with amount and period
        self.amount = amount
        self.period = period
        self.expense_type = expense_type