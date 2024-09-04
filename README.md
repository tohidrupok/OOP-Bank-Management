Report on Bank Management System Project
1. Introduction
The Bank Management System project is an object-oriented programming (OOP) application designed to simulate the core functionalities of a banking system. The system allows users to create accounts, manage their finances, and interact with an administrator for higher-level operations. The project implements several classes to represent different entities within the system, such as users, administrators, and the bank itself.

2. System Design
The system is designed using Python's OOP principles. The main components of the system are:

System Class: Manages the overall functionality, including user and admin account creation, login, and user interactions.
Grahok Class: Represents a bank user with capabilities such as checking balance, depositing, withdrawing, transferring money, and taking loans.
Admin Class: Represents an administrator with the ability to view the bank’s total balance, monitor loan amounts, and enable or disable the loan system.
Bank Class: Represents the bank, holding the total balance, total loans, and the loan system's status.
History Class: Records and manages transaction history for users.
User Class: A base class for Grahok and Admin, storing common attributes like username and password.
3. Key Functionalities
Account Creation:

Users can create accounts by providing a username and password. If the account already exists, they are prompted to log in instead.
Admins can also create accounts with similar procedures, and are added to a separate list of administrators.
Login:

Both users and admins can log in to the system by providing valid credentials. Upon successful login, they are redirected to their respective menus.
User Menu:

Check Balance: Allows users to view their current account balance.
Deposit Amount: Users can deposit money into their accounts, increasing both their balance and the bank's total balance.
Withdraw Amount: Users can withdraw money from their accounts, decreasing both their balance and the bank's total balance.
Transfer Amount: Users can transfer money to another user's account if they have sufficient funds.
Transaction History: Users can view a detailed history of their transactions.
Take a Loan: Users can apply for a loan based on their current balance and the bank's loan system status.
Admin Menu:

View Total Available Balance: Displays the bank's total available balance.
View Total Loan Amount: Displays the total amount of loans issued by the bank.
Enable/Disable Loan System: Allows admins to toggle the availability of the loan feature for users.
4. Implementation Details
Data Persistence: User data is stored in individual text files named after their usernames. This data includes their username, password, balance, and transaction history. Admin data is not persisted to files.
Transaction History: Each transaction (deposit, withdrawal, transfer, loan) is recorded in the user's history, allowing them to review past actions.
Loan System: The loan feature is conditionally available based on the user's current balance and the admin's settings. Loans are limited to twice the user's balance.
5. Challenges and Solutions
Data Consistency: Ensuring that user data is consistently saved and loaded across sessions was a critical challenge. This was addressed by implementing save and load functions in the Grahok class, which are called after every transaction.
User Interface: The system provides a basic terminal-based user interface, using custom functions to display information within styled text boxes for a polished appearance.
6. Conclusion
The Bank Management System project successfully implements a range of functionalities typical of a banking system. By adhering to OOP principles, the system is modular and extensible, allowing for future enhancements. The project demonstrates a solid understanding of class design, inheritance, data management, and user interaction within a Python application.

7. Future Work
Enhancing Security: Future improvements could include encrypting user passwords and securing the data storage mechanism.
Adding More Features: Additional features like interest calculation, account statements, and multi-currency support could be implemented.
User Interface Upgrade: The user interface could be improved with a graphical interface or a web-based application for better usability.
This report summarizes the design, implementation, and functionality of the Bank Management System, highlighting the key components and features that make it a functional and educational project in object-oriented programming.


Tohidul Islam Rupok
Batch: D77 
tohidrupok@students.diu.ac
Dept.CSe, DIU(Dhaka)



# © 2024 tohidrupok
# This code is licensed under the Falcon Squad License. It's open for You.
