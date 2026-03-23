class bank_account:
    def __init__(self,acc_number,acc_holder,balance):
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.__balance = balance

    def deposit(self,amount):
        self.__balance = self.__balance + amount
        print("amount deposited:",amount)

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance = self.__balance -amount
            print("amount withdrawn: ",amount)

        else:
            print("insufficient balance")

    def display_balance(self):
        print("current balance: ",self.__balance)

acc1 = bank_account(1010,'ravi',50000)
acc1.display_balance()
acc1.deposit(2000)
acc1. withdraw(1000)
acc1.display_balance()