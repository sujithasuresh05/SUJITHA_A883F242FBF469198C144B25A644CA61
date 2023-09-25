class BankAccount:
    def __init__(self, account_number, account_holder_name):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = 0
    
    def deposit(self, amount):
        self.__account_balance += amount
    def withdraw(self, amount):
        if self.__account_balance >= amount:
            self.__account_balance -= amount
        else:
            print("Insufficient balance.")
    def display_balance(self):
        print("Account Balance:", self.__account_balance)
      

# Create an instance of the BankAccount class
account = BankAccount(account_number="123456789", account_holder_name="jenifar")
# Test deposit functionality
account.deposit(1000)
account.display_balance()  # Output: Account Balance: 1000
# Test withdrawal functionality
#account.withdraw(500)
#account.display_balance()  # Output: Account Balance: 500
#account.withdraw(1000)  # Output: Insufficient balance.