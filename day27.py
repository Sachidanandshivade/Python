# User Defined Exception Hndler

print("Program Started")
try:
    a = 10
    print(a / 0)  # Exception
except Exception as e:
    print(e.name)

print("Program Ended")