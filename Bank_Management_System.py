class Account:
    def __init__(self):
        self.Accounts = {}
        self.load_Accounts()
    def load_Accounts(self):
        with open('Allaccounts.txt', 'r') as f:
            lines = f.read().splitlines() 
        for i in range(0, len(lines), 3):
            account_number = int(lines[i])  
            name = lines[i + 1]  
            balance = int(lines[i + 2]) 
            self.Accounts[account_number] = {'Name': name, 'Balance': balance}
            
    def Create_Account(self):
        
        Account_Number = int(input("Enter your Account Number : "))
        file_name= str(Account_Number)
        name = input(" Enter your name : ")
        initial_balance=int(input('Enter the initial Deposit : '))
        self.Accounts[Account_Number] = {'Name' : name,'Balance' : initial_balance}
        with open(file_name,'w') as f:
            f.write(f'Account No:{Account_Number} Name:{name} ')
        print('Account Created Successfully')
       
        with open('Allaccounts.txt','a') as file:
            file.write(f'{Account_Number}\n{name}\n{initial_balance}\n')
        print(self.Accounts)
        
    def Deposit(self):
        Account_Number = int(input('Enter you Account Number : '))
        file_name = str(Account_Number)
        if Account_Number not in self.Accounts:
            print('Incorrect Account Number')
            return
        Amount = int(input('Enter the Amount to deposit : '))
        self.Accounts[Account_Number]['Balance']+=Amount  
        print(f'{Amount} Deposited to your account')
        with open(file_name,'a') as f:
            f.write(f'\n  Credited : +{Amount} ')
        
          
    def Withdraw(self):
        Account_Number = int(input('Enter your Account Number'))
        file_name = str(Account_Number)
        if Account_Number not in self.Accounts:
            print('Incorrect Account Number')
            return
        Amount = int(input('Enter the Amount to Withdraw'))
        if Amount > self.Accounts[Account_Number]['Balance']:
            print('Insufficient Money')
            return
        self.Accounts[Account_Number]['Balance'] -= Amount
        print(f'-{Amount} withdrawn from your account')
        with open(file_name,'a') as f:
            f.write(f'\n  Withdrawn : -{Amount} ')
        
    def Transaction_History(self):
        Account_Number=int(input('Enter your Account Number : '))
        file_name=str(Account_Number)
        with open(file_name,'r') as f:
            print(f.read())
        current_balance=self.Accounts[Account_Number]['Balance']
        print(f'Current Account Balance is {current_balance}')
            
Bank = Account()
while True:
    print("\n Main menu \n 1.New Account \n 2.Deposit \n 3.Withdraw \n 4.Show Transaction history \n 5.exit")
    print()
    Choice = int(input())
    if Choice == 1:
        Bank.Create_Account()
    elif Choice == 2:
        Bank.Deposit()
    elif Choice == 3:
        Bank.Withdraw()
    elif Choice == 4:
        Bank.Transaction_History()
    elif Choice == 5:
        break
    else:
        print("  Invalid Input ")
           