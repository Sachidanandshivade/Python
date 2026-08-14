# 1. Method Overriding (run-time polymorphism)

class Animal:
    def sound(self):  # overridden method
        print("Animal makes sound")

class dog(Animal):
    def sound(self):
        super().sound()
        print("Dog makes sound like bow bow")  # overriding method

d = dog()
d.sound()


def add(self,*numbers):
    # 'numbers' becomes a tuple of all passed positional arguments
    return sum(numbers)

# You can pass any number of arguments:
print(add(10, 20))       # Output: 30
print(add(10, 20, 30))   # Output: 60
print(add(0))            # Output: 0
            # Output: 0

# 3. Duck Typing (If it looks like a duck and quacks like a duck, it is a duck)

class Dog:
    def swim(self):
        print("Dog Swims")

class Duck:
    def swim(self):
        print("Duck Swims")

# Function is using Duck Typing
def make_swim(obj):
    obj.swim()

d = Dog()
dc = Duck()

make_swim(d)
make_swim(dc)


class Parrot:
    def fly(self):
        print("Parrot is flying high in the sky!")

class Airplane:
    def fly(self):
        print("Airplane is taking off!")

# Function using duck typing
def make_it_fly(thing):
    thing.fly()

# Creating instances
parrot = Parrot()
airplane = Airplane()

# Passing different objects to the same function
make_it_fly(parrot)    # Output: Parrot is flying high in the sky!
make_it_fly(airplane)  # Output: Airplane is taking off!