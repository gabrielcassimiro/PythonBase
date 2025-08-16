#Sample study on using OOP in Python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def info(self):
        print(f"Name: {self.name}\nAge: {self.age}")
    pass

class Account:
    def __init__(self, person: Person, amount):
        self.person = person
        self._amount = amount #Private variable

    def account_info(self):
        print(f"Owner: {self.person.name}, Amount: {self._amount}")

    def deposit(self, amount):
        self._amount += amount

    def withdraw(self, amount):
        self._amount -= amount

    def manual_deposit(self):
        try:
            amount = int(input("What is the deposit amount: "))
            CustomExceptions.valid_deposit(amount)
            self._amount += amount
            self.account_info()
        except DepositNotValid as ex:
            print(ex)
        except ValueError:
            print("Invalid input.")

    def manual_withdraw(self):
        try:
            amount = int(input("What is the withdrawal amount: "))
            CustomExceptions.valid_withdraw(amount, self._amount)
            self._amount -= amount
            self.account_info()
        except WithdrawNotValid as ex:
            print(ex)
        except ValueError:
            print("Invalid input.")
    pass

class CheckingAccount(Account):
    def __init__(self, person: Person, amount):
        super().__init__(person, amount)
        self.type = "checking"

    def info(self):
        print(f"Owner: {self.person.name}, Amount: {self._amount}, Type: {self.type}")
    pass


#Creating Custom Exception
class DepositNotValid(Exception):
    def __init__(self, message="Invalid deposit amount."):
        super().__init__(message)
    pass

#Creating Custom Exception
class WithdrawNotValid(Exception):
    def __init__(self, message="Invalid Withdraw amount."):
        super().__init__(message)
    pass

#Class that have all custom exception validations
class CustomExceptions:

    #Declare a static function
    @staticmethod
    def valid_deposit(amount):
        if amount < 0:
            raise DepositNotValid("Deposit cannot be negative.")
        elif amount == 0:
            raise DepositNotValid("Deposit cannot be zero.")

    @staticmethod
    def valid_withdraw(amount, total_amount):
        if amount == 0:
            raise WithdrawNotValid("Withdraw cannot be zero.")
        if amount > total_amount:
            raise WithdrawNotValid("You don't have this amount.")
    pass


def opp_examples():
    print("OOP examples below")
    person = Person("John", 20)
    account = CheckingAccount(person, 100)

    person.info()
    account.info()
    account.deposit(55)
    account.info()
    account.withdraw(80)
    account.info()

    account.manual_deposit()
    account.manual_withdraw()
    print("___________________________________")

