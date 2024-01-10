#Class BankAccount
class BankAccount:
  
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.07, balance = 10000, show_interest = True): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        self.show_interest = show_interest
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        # your code here
        return self
    def withdraw(self, amount):
        # your code here
        self.balance -= amount
        return self
    def display_account_info(self, display = True):
        # your code here
        self.show_interest = display
        if self.show_interest == True:
            return (f'Balance: {self.balance} Interest Rate: {self.int_rate * 100:.2f}% \n') #.2f within the f-string used to format the output of multiplication to 2 places
        else:
           #print(f'Balance: {self.balance} ')
           return print(f'Balance: {self.balance} \n') 
    def yield_interest(self):
        # your code here
        self.balance *= (1 + self.int_rate)
        return self.balance


my_account = BankAccount(0.065,493.5)
print()
print(my_account.display_account_info())
print('-'*30 + '\n')

my_account.deposit(5259.3).display_account_info(False)
my_account.withdraw(5259.3).display_account_info(False)
my_account.deposit(5259.3).display_account_info(False)
my_account.withdraw(5259.3).display_account_info(False)
