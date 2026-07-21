# 1. No Input & No Output
def add1():
    a = 10
    b = 20
    print(a + b)

# 2. Input & No Output
def add2(a, b):
    print(a + b)

# 3. No Input & Has Output
def add3():
    a = 10
    b = 40
    return a + b

# 4. Input & Has Output
def add4(a, b):
    c = a + b
    return c


# --- Function Calls ---

print("1. No i/p & No o/p:")
add1()  # Output: 30

print("\n2. i/p & No o/p:")
add2(100, 200)  # Output: 300

print("\n3. No i/p & o/p:")
res = add3()
print(res)  # Output: 50

print("\n4. i/p & o/p:")
print(add4(30, 30))  # Output: 60


# return multiple expression
def calculate(a, b):
    return a + b, a - b, a * b, a % b

x, y, z, m = calculate(20, 10)

print("Addition:", x)
print("Subtraction:", y)
print("Multiplication:", z)
print("Modulos:", m)

print("-------------------")

# return multiple values
def student():
    return "Rahul", 21, "Bangalore"

name, age, city = student()

print("Name:", name)
print("Age:", age)
print("City:", city)

# function overloading - function with same name but different parameters not possible
# Default arguments
def add(a, b, c = 0, d = 0):
    return a + b + c + d

print(add(10, 20)) # 30
print(add(10, 20, 30)) # 60
print(add(10, 20, 30, 40)) # 100