class A:
    def show(self):
        print("This is A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# Creating an instance
d = D()
d.show()
print(D.mro())


# super keyword - Always refers to parent class (constructor, method)
# super().method

class A:
    def show(self):
        print("This is parent")

class B(A):
    def show(self):
        super().show()
        print("This is child")

b = B()
b.show()

print("---------constructor------------")

class A:
    def __init__(self, name):
        self.name = name
        print("This is parent con", name)

class B(A):
    def __init__(self):
        super().__init__(name="GAmana")
        print("This is child con")

b = B()

class A:

    def show(self):

        print("A")





class B(A):

    def show(self):

        print("B")





class C(A):

    def show(self):

        print("C")





class D(B, C):

    def show(self):

        print("D")





class E(C, A):

    def show(self):

        print("E")





class F(D, E):

    def show(self):

        print("F")





obj = F()

obj.show()



print(F.mro())