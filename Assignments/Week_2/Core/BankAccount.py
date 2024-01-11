#Class BankAccount
class BankAccount:
   #list to keep track of instances created
    instances=[]

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.07, balance = 10000, show_interest = True): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        self.show_interest = show_interest

        #add instance to list of instances on init
        BankAccount.instances.append(self)

        # don't worry about user info here; we'll involve the User class soon


    def deposit(self, amount):
        self.balance += amount
        # your code here
        return self
    

    def withdraw(self, amount):
        # your code here
        if self.balance < amount:
            print(f'Only {self.balance:.2f} is available for withdrawal.\n Withdrawing Remaining balance...\n {self.balance} Withdrawn')
            self.balance = 0
        else:
            self.balance -= amount
        return self
    

    def display_account_info(self, display = True):
        # your code here
        self.show_interest = display
        if self.show_interest == True:
            print(f'Balance: {self.balance:.2f} Interest Rate: {self.int_rate * 100:.2f}% \n') #.2f within the f-string used to format the output of multiplication to 2 places
        else:
           print(f'Balance: {self.balance:.2f} \n')

        return self
    

    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
        return self
    
    @classmethod
    def print_instances(cls):
        for i in range(len(cls.instances)):
            print(f'Balance: {cls.instances[i].balance:.2f} Interest: {cls.instances[i].int_rate}')
            #cls.instances.
        return cls.instances

#Commented to Allow for Next Assignment
'''
my_account_1=BankAccount()
my_account_2=BankAccount()

my_account_1.deposit(200).deposit(300).deposit(400).withdraw(1580.33).yield_interest().display_account_info(False)
my_account_2.deposit(7500).deposit(2200).withdraw(10000).withdraw(5000).withdraw(750.33).withdraw(2100.45).yield_interest().display_account_info(False)
BankAccount.print_instances()
print()
#my_account_1.display_account_info(False)
'''

'''
my_account = BankAccount(0.065,493.5)
print()
print(my_account.display_account_info())
print('-'*30 + '\n')

my_account.deposit(5259.3).display_account_info(False)
my_account.withdraw(5259.3).display_account_info(False)
my_account.deposit(5259.3).display_account_info(False)
my_account.withdraw(5259.3).display_account_info(False)
'''