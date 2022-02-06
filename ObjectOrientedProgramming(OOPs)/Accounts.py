# '__main__' is the name of the environment where top-level code is run.
# “Top-level code” is the first user-specified Python module that starts running.
# It's “top-level” because it imports all other modules that the program needs.
# Sometimes “top-level code” is called an entry point to the application.

# Single underscores are a Python naming convention indicating a name is meant for internal use. (_balance, _transaction_list)
# It is generally not enforced by the Python interpreter and meant as a hint to the programmer only.
# Python mangles the name of class attributes both methods and variables that start with two underscores

# Name Mangling in Python -
# In name mangling process any identifier with two leading underscore and one trailing underscore is textually replaced with _classname__identifier where classname is the name of the current class.
# It means that any identifier of the form __geek (at least two leading underscores or at most one trailing underscore) is replaced with _classname__geek, where classname is the current class name with leading underscore(s) stripped.
# if the attribute name with 2 underscores doesn't result in the name being mangled, so names are only mangled if they start with two underscores and end with no more than a single underscore
# So, init method is not mangled

import datetime
import pytz


class Account:
    """simple account class with balance"""

    @staticmethod                                       # static method is shared by all instances of the class, so making the method static is simple,
    def _current_time():                                    # we just remove the self parameter and put and annotation before the method definition
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):          # '__init__' method is used to initialize the class & it's extremely rare to create a class without providing an init method.
        self.name = name                                # Notice that all the methods takes 'self' as their 1st parameter.
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self.name)       # whenever we want to refer to the 'data attributes', we have to use the form.self

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "Deposited"
            else:
                tran_type = "Withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    ved = Account("Ved", 0)
    ved.show_balance()

    ved.deposit(1000)
    # ved.show_balance()
    ved.withdraw(500)
    # ved.show_balance()

    # ved.withdraw(2000)
    ved.show_transactions()

    steph = Account("Steph", 800)
    steph.__balance = 90
    steph.deposit(8000)
    steph.withdraw(987)
    steph.show_transactions()
    steph.show_balance()
    print(steph.__dict__)



























































































