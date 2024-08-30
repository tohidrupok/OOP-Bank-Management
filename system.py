from grahok import Grahok
from admin import Admin
from bank import Bank
import os

class system:
    def __init__(self):
        self.user_list = []
        self.admin_list = []
        self.bank = Bank("MyBank")

    def create_account(self):
        self.print_box("1. Create Admin Account\n2. Create User Account")
        a = int(input("Please select an option: "))
        if a == 2:
            name = input("Please enter your username: ")
            password = input("Please create a secure password: ")

            user = self.find_user(name, password)
            if user:
                self.print_box("User already exists. Please log in.")
                return
            new_account = Grahok(name, password, self.bank)
            new_account.save_data()  
            self.user_list.append(new_account)
            self.print_box("Congratulations! You are now a valued member of our bank.")
        elif a == 1:
            name = input("Please enter your admin username: ")
            password = input("Please set a secure password: ")
            admin_account = Admin(name, password)
            self.admin_list.append(admin_account)
            self.print_box("Congratulations! You have been successfully added as a new administrator.")

    def login(self):
        username = input("Please enter your username: ")
        password = input("Please create a secure password: ")

        admin = self.find_admin(username, password)
        user = self.find_user(username, password)
        
        if user:
            user.load_data()  
            if user.password == password:  
                self.user_menu(user)
            else:
                self.print_box("The password you entered is incorrect. Please try again.")
        elif admin:  
            self.admin_menu(admin)
        else:
            self.print_box("No matching user or administrator found. Please check your credentials and try again.")

    def find_user(self, username, password=None):
        filename = f"{username}.txt"
        if os.path.exists(filename):
            user = Grahok(username, password, self.bank)
            return user
        return None
   
    def admin_menu(self, admin):
        while True:
            self.print_box("Salman F.Rahman Bank\n\n\n 1. View Total Available Balance\n2. View Total Loan Amount\n3. Enable Loan System\n4. Disable Loan System\n5. Exit")

            choice = input("Select an option: ")
            if choice == "5":
                break
            elif choice == "1":
                total_balance = admin.check_total_balance(self.bank)
                self.print_box(f"Total Available Balance: ${total_balance:.2f}")
            elif choice == "2":
                total_loan = admin.check_total_loan(self.bank)
                self.print_box(f"Total Loan Amount: ${total_loan:.2f}")
            elif choice == "3":
                admin.enable_loan_feature(self.bank)
                self.print_box("Loan system has been enabled.")
            elif choice == "4":
                admin.disable_loan_feature(self.bank)
                self.print_box("Loan system has been disabled.")
                
    def user_menu(self, user):
        while True:
            self.print_box("Welcome to the Banking Management System\nYour Financial Partner for Success\n\n\n\n1. Check Balance\n2. Deposit Amount\n3. Withdraw Amount\n4. Transfer Amount\n5. Transaction History\n6. Take a Loan\n7. Exit") 

            a = input("Enter Your Option: ")
            if a == "7":
                break
            elif a == "1":
                balance = user.check_balance()
                self.print_box(f"Available Balance: {balance}")
            elif a == "2":
                amount = int(input("Deposit Amount: "))
                user.deposit(amount)
                self.print_box("Successfully deposited.")
            elif a == "3":
                amount = int(input("Withdraw Amount: "))
                if user.withdrawa(amount):
                    self.print_box("Withdrawn successfully.")
                else:
                    self.print_box("Sorry, not enough balance.")
            elif a == "4":
                friend_name = input("Enter the account username: ")
                friend = self.find_friend(friend_name)
                if friend:
                    amount = int(input("Enter Transfer Amount: "))
                    if user.transfer_amount(friend, amount):
                        self.print_box("Transferred successfully.")
                    else:
                        self.print_box("Sorry, not enough balance.")
                else:
                    self.print_box("Friend not found.")
            elif a == "5":
                user.history_transaction()
            elif a == "6":
                if self.bank.loan_system:
                    amount = int(input("Enter Loan Amount: "))
                    user.take_lone(amount)              
                else:
                    self.print_box("Loan feature is currently disabled by the admin.")
                    

    def find_friend(self, username):
        for person in self.user_list:
            if person.username == username:
                return person
        return None
    
    def find_admin(self, username, password):
        for person in self.admin_list:
            if person.username == username and person.password == password:
                return person
        return None

    def print_box(self, text):
        lines = text.split('\n')
        width = max(len(line) for line in lines) + 4  
        height_padding = 3  

        
        print("\n" + "╭" + "─" * width + "╮")

        
        for _ in range(height_padding):
            print("│" + " " * width + "│")

        # Text with side borders
        for line in lines:
            print(f"│ {line.center(width-2)} │")
        
        # Bottom padding for a taller look
        for _ in range(height_padding):
            print("│" + " " * width + "│")

        # Bottom rounded corners
        print("╰" + "─" * width + "╯\n")






