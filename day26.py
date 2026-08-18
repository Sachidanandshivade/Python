from abc import ABC, abstractmethod


class Vechile(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vechile):
    def start(self):
        print("Car starts")

    def stop(self):
        print("Car stops")


class Autocar(Car):
    def start(self):
        print("Auto Car starts")

    def stop(self):
        print("Auto Car stops")


# Creating child object using parent reference concept
v: Vechile = Autocar()
v.start()
v.stop()


# Encapsulation is a core idea in object-oriented programming (OOP).
# It bundles data (attributes) and the methods that operate on that data into a single unit called a class.
# attr - Private(__), access (getters and setters), public, protected(_)

class Bank:
    def __init__(self):
        self.__balance = 25000  # private variable

    # getter
    def get_balance(self):
        print(f"The balance is {self.__balance}")

    # setter
    def set_balance(self, new_balance):
        if new_balance < 0:
            print("No balance")
        else:
            self.__balance = new_balance


b = Bank()
# print(b.__balance) # not directly accessed (getter and setter)
b.get_balance()
b.set_balance(100000)
b.get_balance()