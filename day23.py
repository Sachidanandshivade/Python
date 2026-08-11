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