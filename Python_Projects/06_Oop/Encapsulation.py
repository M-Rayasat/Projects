class Account:
    def __init__(self, balance):
        self.__balance = balance     # private attribute

    def get_balance(self):           # controlled exposure
        return self.__balance

    def deposit(self, amount):       # controlled modification
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

acc = Account(1000)
print(acc.get_balance())     # 1000
acc.deposit(500)
print(acc.get_balance())     # 1500