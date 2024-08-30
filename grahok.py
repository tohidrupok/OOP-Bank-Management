from user import User
from history import History

import os

class Grahok(User):
    def __init__(self, username, password, bank) -> None:
        super().__init__(username, password)
        self.balance = 0
        self.bank = bank
        self.history = []
        self.load_data()  # Try to load data if the file exists

    def save_data(self):
        """Save user data to a file"""
        filename = f"{self.username}.txt"
        with open(filename, 'w') as file:
            file.write(f"{self.username},{self.password},{self.balance}\n")
            for record in self.history:
                file.write(f"{record.name},{record.amount},{record.widthraw},{record.diposit},{record.transfer},{record.lone}\n")

    def load_data(self):
        """Load user data from a file"""
        filename = f"{self.username}.txt"
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                lines = file.readlines()
                user_data = lines[0].strip().split(',')
                self.username = user_data[0]
                self.password = user_data[1]
                self.balance = float(user_data[2])

                for line in lines[1:]:
                    data = line.strip().split(',')
                    history = History(data[0], float(data[1]), float(data[2]), float(data[3]), float(data[4]), float(data[5]))
                    self.history.append(history)


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.bank.total_balance += amount
            history = History(self.username, self.check_balance(), 0, amount, 0, 0)
            self.history.append(history)
            self.save_data()  # Save data after the transaction

    def withdrawa(self, amonunt):
        if self.balance > amonunt:
            self.balance -= amonunt
            self.bank.total_balance -= amonunt
            history = History(self.username, self.check_balance(), amonunt, 0, 0, 0)
            self.history.append(history)
            self.save_data()  # Save data after the transaction
            return True
        else:
            return False

    def check_balance(self):
        return self.balance

    def take_lone(self, amount):
        capacity = self.balance * 2
        if capacity >= amount:
            self.balance += amount
            self.bank.total_balance -= amount
            self.bank.total_loan += amount
            history = History(self.username, self.check_balance(), 0, 0, 0, amount)
            self.history.append(history)
            self.save_data()  # Save data after the transaction
            print('Loan Done and amount is:', amount)
        else:
            print(f'Sorry!\nYour Current Amount is: {self.balance}\nYour Maximum Loan Limit is: {capacity}')

    def transfer_amount(self, other_user, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_user.deposit(amount)
            history = History(self.username, self.check_balance(), 0, 0, amount, 0)
            self.history.append(history)
            self.save_data()  # Save data after the transaction
            return True
        else:
            return False

    def history_transaction(self):
        if not self.history:
            print("No transaction history available.")
            return

        print("\n" + "=" * 60)
        print(f"{'Transaction History':^60}")
        print("=" * 60)

        for Day, report in enumerate(self.history, start=1):
            print(f"\n{'-' * 60}")
            print(f"Day {Day}:")
            print(f"{'User Name:':<15} {report.name}")
            print(f"{'Amount:':<15} {report.amount}")
            print(f"{'Withdraw:':<15} {report.widthraw}")
            print(f"{'Deposit:':<15} {report.diposit}")
            print(f"{'Transfer:':<15} {report.transfer}")
            print(f"{'Loan:':<15} {report.lone}")
            print(f"{'-' * 60}")

        print("=" * 60)

