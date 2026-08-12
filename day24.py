# OPERATOR OVERLOADING - dunder methods, magic methods

print(3 + 5) # 8
print("gamana" + "Reddy")

class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks

s1 = Student(30) # self
s2 = Student(50) # other
print(s1)
print(s2)
print(s1 + s2) # 80