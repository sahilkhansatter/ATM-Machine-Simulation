class ATM:
    def __init__(self, pin):
        """Initialize the ATM with a starting balance, pin, and an empty transaction history."""
        self.balance = 0
        self.pin = pin
        self.transaction_history = []
    
    def check_pin(self, pin_input):
        """Check if the entered PIN is correct."""
        return self.pin == pin_input
    
    def balance_inquiry(self):
        """Return the current balance."""
        return self.balance
    
    def deposit(self, amount):
        """Deposit a specified amount and record the transaction."""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            print(f"Deposit successful! Current balance: {self.balance}")
        else:
            print("Invalid deposit amount!")
    
    def withdraw(self, amount):
        """Withdraw a specified amount if sufficient balance is available and record the transaction."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            print(f"Withdrawal successful! Current balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount!")
    
    def change_pin(self, old_pin, new_pin):
        """Change the PIN if the old PIN is correct."""
        if self.check_pin(old_pin):
            self.pin = new_pin
            self.transaction_history.append("PIN changed")
            print("PIN successfully changed!")
        else:
            print("Incorrect old PIN!")
    
    def show_transaction_history(self):
        """Display the transaction history."""
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

# Main simulation function
def atm_simulation():
    print("Welcome to the ATM!")
    pin = int(input("Please set your initial PIN: "))
    atm = ATM(pin)
    
    while True:
        print("\nATM Menu:")
        print("1. Balance Inquiry")
        print("2. Cash Deposit")
        print("3. Cash Withdrawal")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            entered_pin = int(input("Enter your PIN: "))
            if atm.check_pin(entered_pin):
                print(f"Your balance is: {atm.balance_inquiry()}")
            else:
                print("Incorrect PIN!")
        
        elif choice == 2:
            entered_pin = int(input("Enter your PIN: "))
            if atm.check_pin(entered_pin):
                amount = float(input("Enter the amount to deposit: "))
                atm.deposit(amount)
            else:
                print("Incorrect PIN!")
        
        elif choice == 3:
            entered_pin = int(input("Enter your PIN: "))
            if atm.check_pin(entered_pin):
                amount = float(input("Enter the amount to withdraw: "))
                atm.withdraw(amount)
            else:
                print("Incorrect PIN!")
        
        elif choice == 4:
            entered_pin = int(input("Enter your old PIN: "))
            if atm.check_pin(entered_pin):
                new_pin = int(input("Enter your new PIN: "))
                atm.change_pin(entered_pin, new_pin)
            else:
                print("Incorrect PIN!")
        
        elif choice == 5:
            entered_pin = int(input("Enter your PIN: "))
            if atm.check_pin(entered_pin):
                atm.show_transaction_history()
            else:
                print("Incorrect PIN!")
        
        elif choice == 6:
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid option! Please try again.")

# Run the simulation
atm_simulation()
