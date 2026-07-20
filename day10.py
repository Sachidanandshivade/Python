# Syntax to define a function (0 to n parameters)
# def function_name(parameters):
    # body
    # pass  # Place your code block here

# Syntax to call the function
# function_name()

def add():
    a = 10
    b = 20
    c = a + b
    print(c)

add()   

# WAF to find square of a number
def square(num):
    return num ** 2

# WAF to find largest of 3 numbers
def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# WAF to find cube of a number
def cube(num):
    return num ** 3


# --- Testing the functions ---
print("Square of 5 is:", square(5))
print("Largest of 10, 25, and 15 is:", find_largest(10, 25, 15))
print("Cube of 3 is:", cube(3))