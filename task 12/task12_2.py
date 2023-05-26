class BankAccount:

    def __init__(self, name, number, password):
        self.owner_name = name
        self.account_number = number
        self.__balance = 0
        self.__password = password

    def get_balance(self, password):
        if self.__password == password:
            return self.__balance
        else:
            print("The password is incorrect. Try again, please.")

    def get_password(self, password):
        if self.__password == password:
            return self.__password
        else:
            print("The password is incorrect. Try again, please.")

    def change_balance(self, password, sum):
        if self.__password == password:
            if self.__balance + sum >= 0:
                self.__balance += sum
            else:
                print("Enter another sum, please.")
        else:
            print("The password is incorrect. Try again, please.")

    def change_password(self, password, new_password):
        if self.__password == password:
            self.__password = new_password
        else:
            print("The password is incorrect. Try again, please.")


q = BankAccount('Max', 1, 'crim')
print(q.get_balance('crim'))
q.change_balance('crim', 890)
print(q.get_balance('crim'))
