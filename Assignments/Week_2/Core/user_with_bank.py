from BankAccount import BankAccount #Syntax: from path, here we're in teh same directory | relative paths, consider the project root folder
import os
class User():
    
    
    def transfer(s)
        

    def __init__(self, fname, lname, email):
        
        self.fname = fname
        self.lname = lname
        self.email = email
        
        self.account = {}
        self.ac_index = 0
        self.action_index = ''
        self.ac_id = ''

    def open_account(self, rate = 0.07, bal = 0):
        #Adding a Key to the Account Dictionary consisting of key(a/c ID, and Value BankAccount Instance)
        #Account IDs are 3 digit regardless with Zeros Tacked on to any index generate allowint for up to 999 accounts per user following this format
        self.ac_index += 1
        self.account[f'{(self.ac_index):03d}'] = BankAccount(rate, bal)
        return self

    def print_ac_list(self):
        print(self.account)
        return self
    
    #This Function Returns a valid account ID used as an index in selecting an account on deposit or withdraw from
    def pick_account(self, action):
        if len(self.account) > 0: 
            action = action
            ctr = 0
            print('\n')
            for key in self.account:
                ctr += 1
                print(f'Account ID: {key}   Balance: {self.account[key].balance}    Interest Rate: {(self.account[key].int_rate * 100):.2f}% ')
            if action == 'w':
                print('\nSelect Account Withdraw (W) FROM...', end = '')
            else:
               print('\nSelect Account Deposit TO...', end = '') 
            #try:
            print(end='')
            
            loop = 0
            print('\nexit/quit to log out\n')
            self.ac_id = input('Please Enter Account ID:    ')
            try:
                if (int(self.account[self.ac_id].int_rate)):
                    print ('Valid Index')
                    return self.ac_id
            except Exception as e:
                print('Incorrect Account, Logging Out...')
                return '000'
    
    def make_deposit(self, amount):
       
        if self.pick_account('d') == '000':
            exit()
        else:
            print(f'Depositing USD {amount} in Account {self.ac_id}')
            self.account[self.ac_id].deposit(amount)
            print('-'*30)
            print(f'Account ID: {self.ac_id}   New ',end='')
            self.account[self.ac_id].display_account_info()
        return self

    
    def make_withdrawal(self, amount):

        if self.pick_account('w') == '000':
            exit()
        else:
            print(f'Withdrawing USD {amount} in Account {self.ac_id}')
            self.account[self.ac_id].withdraw(amount)
            print('-'*30)
            print(f'Account ID: {self.ac_id}   New ',end='')
            self.account[self.ac_id].display_account_info()
        return self
            
    
            
    def display_user_balance(self, display = False):
        self.pick_account()
        self.account[self.ac_id].display_account_info(display)
        return self
    

user1 = User('Sam', 'Keiru', 'sam@migui.io')
print('\nAccount Holder: ',user1.fname, user1.lname, user1.email)
user1.open_account(0.07,12000).open_account(0.07,13228.90)
user1.make_deposit(500)
user1.make_withdrawal(400)

print('THe End!')
