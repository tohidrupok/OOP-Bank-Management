class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.total_balance = 1000
        self.total_loan = 0
        self.loan_system = True

    def check_total_balance(self):
        return self.total_balance

    def check_total_loan(self):
        return self.total_loan

    def on_loan_system(self):
        self.loan_system = True

    def off_loan_system(self):
        self.loan_system = False
