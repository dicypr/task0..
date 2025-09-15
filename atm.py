class ATM():
    def __init__(self,bankbalance=0,pin="1234"):
        self.bankbalance=bankbalance
        self.pin=pin

    def check_pin(self, input_pin):
        if self.pin ==  input_pin:
            return True
        else:
            print("INVALID PIN")
            return False
        
    def display_balance(self):
        print(f"Your current balance is: ${self.bankbalance:,.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.bankbalance += amount
            print(f"\n ${amount:,.2f}.")
        else:
            print(" amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print(" amount must be positive.")
        elif amount > self.bankbalance:
            print("\nInsufficient funds.")
        else:
            self.bankbalance -= amount
            print(f"\n withdrew ${amount:,.2f}.")

atm = ATM()

print(" ATM ")

input_pin = input("Enter PIN: ")

if atm.check_pin(input_pin):
    while(True):
        atm.display_balance()
    
        choice = input("\nDo you want to (1) Deposit or (2) Withdraw? or (3)exit ")

        if choice == '1':
            try:
                deposit_amount = float(input("Enter amount to deposit: $"))
                atm.deposit(deposit_amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
    
        elif choice == '2':
            try:
                withdraw_amount = float(input("Enter amount to withdraw: $"))
                atm.withdraw(withdraw_amount)
            except ValueError:
                print("enter a number.")

        elif choice == '3':
            break
    
        else:
            print("cancelled.")
        
        print("\n--- Transaction Complete ---")
        atm.display_balance()

else:
    print("Incorrect PIN")
