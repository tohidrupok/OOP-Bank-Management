from system import system

def print_main_menu():
    print("\n" + "="*40)
    print("        Welcome to Bank Management")
    print("="*40)
    print("1. Create an Account")
    print("2. Login to Your Account")
    print("3. Exit")
    print("="*40)

if __name__ == "__main__":
    system = system()
    while True:
        print_main_menu()
        user_input = int(input("Enter Your Option (1-3): "))
        if user_input == 3:
            print("\nThank you for using Bank Management System!")
            print("Goodbye!\n")
            break
        elif user_input == 1:
            system.create_account()
        elif user_input == 2:
            system.login()
        else:
            print("\nInvalid option! Please try again.\n")
