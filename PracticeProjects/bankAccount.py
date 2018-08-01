class Account(object):
    """This creates simple bank account"""
    def __init__(self, name, balance):
        #This method creates account with initial balance
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        #this method adds money to account
        if amount >0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        #this takes mones from account
        if 0<amount<= self.balance:
            self.balance -= amount
            self.show_balance()
        else:
            print("Amout cant be less then your current balance")
            self.show_balance()
    def show_balance(self):
        #this shows current balance
        print ("Balance is {0}".format(self.balance))
        #print self.balance

#If code is executed as main, then below gets executed.
if __name__ == '__main__':

    ali = Account("Ali",0)
    ali.show_balance()

    ali.deposit(10000)
    ali.withdraw(7500)
    ali.withdraw(500)
    ali.withdraw(1200)



