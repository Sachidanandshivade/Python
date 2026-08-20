# User Defined Exception Handler

print("Program Started")
try:
    x = int(input("Enter the Number"))
    a = 10
    print(a / x) # Exception
    lst = [1, 2, 3, 4] # 0 1 2 3
    print(lst[6])
except ZeroDivisionError:
    print("Cannot divide by Zero")
except IndexError:
    print("The Index is Out of the range")
except ValueError:
    print("Please enter Interger")
except Exception as e:
    print(e) # General Exception at last

print("Program Ended")


# try - except - else - finally

try:
    a = 10
    b = 2
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by Zero")
else:
    print("Result: ", result)
finally:
    print("Exceution Completed")