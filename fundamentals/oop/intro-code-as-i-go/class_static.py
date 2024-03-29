class BankAccount:
    # Declaring a class attribute
    # Shared among all bank accounts
    bank_name = "First National Dojo"		
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

adriensAccount = BankAccount(.01, 20000)
sadiesAccount = BankAccount(.04, 34000)
adriensAccount.bank_name = "Dojo Credit Union"
    
print(adriensAccount.bank_name)
# output: Dojo Credit Union
    
print(sadiesAccount.bank_name)
# output: First National Dojo

BankAccount.bank_name = "Bank of Dojo"

print(adriensAccount.bank_name)
print(sadiesAccount.bank_name)