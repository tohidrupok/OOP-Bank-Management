from user import User

class Admin(User):
    def __init__(self, username, password) -> None:
        super().__init__(username, password)

    def check_total_balance(self, bank):
        return bank.check_total_balance()

    def check_total_loan(self, bank):
        return bank.check_total_loan()

    def enable_loan_feature(self, bank):
        bank.on_loan_system()

    def disable_loan_feature(self, bank):
        bank.off_loan_system()
