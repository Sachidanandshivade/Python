# Defining length and breadth as floats
length = 7.3
breadth = 5.5

# Calculating area
area = length * breadth
print("Area of rectangle:", area)

# In Python, bool() converts values to True or False. 
# Empty inputs or 0 evaluate to False, while non-empty inputs evaluate to True.
status_input = input("Is the student placed? (Press Enter for False, or type anything for True): ")
is_placed = bool(status_input)

print("Placed status:", is_placed)

# Taking real and imaginary parts as input (converting to float or int)
real_part = float(input("Enter real part: "))  # Example: 5
img_part = float(input("Enter imaginary part: "))  # Example: 2

# Creating a complex number using complex(real, imaginary)
num = complex(real_part, img_part)

# Displaying the result and its type
print(num)        # Output will look like: (5+2j)
print(type(num))  # Output: <class 'complex'>