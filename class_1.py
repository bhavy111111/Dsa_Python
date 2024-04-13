class Atm:

    def __init__(self):
        #self.pin = ''
        self.pin=''
        #self.balance=0
        self.balance=0
        self.menu()

    def menu(self):
        user_input=input('''
                    Hello, How would you like to proceed!
                    1. Enter 1 to create pin
                    2.Enter 2 to deposit
                    3.Enter 3 to withdrawl
                    4.Enter 4 to check the balance
                    5. Enter 5 to exit
''')
        if(user_input=='1'):  
            #print('Create_pin')
            self.create_pin()
        elif(user_input=='2'):
            self.deposit()
            #print('deposit_pin')
        elif(user_input=='3'):
            self.withrawl()
            #print('Wkkithraw_pin')
        elif(user_input=='4'):
            self.balance()
            #print('check the balance')
        else:
            print('Bye')
        
            


    def create_pin(self):
        self.pin = input('Enter the pin')
        print('Pin set successfully')

    def deposit(self):
        temp=input('Enter the pin')
        if(temp==self.pin):
            amount = int(input('eNTER THE AMOUTN'))
            self.balance = self.balance+amount
            print('Deposit')
        else:
            print('Incorrect pin')
                             

    def withrawl(self):
        temp = input('Enter the pin')
        if(temp==self.pin):
            amount = int(input('Enter the money'))
            if(amount < self.balance):
                self.balance-=amount
                print('Operation successfully')
            else:
                print('Insufficeint')
        else:
            print('Invalid')
    def balance(self):
        temp=input('Enter the pin')
        if(temp==self.pin):
            print(self.balance)
        else:
            print('Invalid')
                             
            



sbi=Atm()
sbi.__balance='6000'

#sbi.create_pin()







        

                
