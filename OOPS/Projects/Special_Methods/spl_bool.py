class Balance:
    
    def __init__(self, account_number, account_name, initial_balance):
        self.account_number = account_number
        self.account_name = account_name
        self.initial_balance = initial_balance
        
    def add_balance(self, amount):
        self.initial_balance += amount
        
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds in the account")
            
    def __bool__(self):
        return self.initial_balance > 0
            
            
my_account = Balance("AZX34598", "Tom Brady", 0)

if my_account:  # we want this to be false if the account balance is zero
    print("Instance object is considered as true")
else:
    print("Instance object is considered as false")