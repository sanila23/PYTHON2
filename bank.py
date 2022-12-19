class Bank_Account():
    def __init__(self):
        self.balance= 0
        print("Hello!! Welcome to depsit and withdrawal section")
    def deposit(self):
        amount=float(input("Enter the amount to deposit:"))
        self.balance+=amount
        print("\n Amount deposited:",amount)
    def withdraw(self):
        amount = float(input("Enter the amount to withdraw:"))
        if self.balance>=amount:
            self.balance-=amount
            print("\n Withdrawed:", amount)
        else:
            print("\n Insufficent balance!!")
    def display(self):
        print("\n Net available balance=",self.balance)
z=Bank_Account()
z.deposit()
z.withdraw()
z.display()