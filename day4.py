# [ Source Code ] (.py) 
#        │
#        ▼
# [ Python Compiler ]  ──► Generates Bytecode & Saves as a (.pyc) file
#        │
#        ▼
# [ Python Virtual Machine (PVM) ] ──► Interprets line-by-line into Machine Code (0s and 1s)
#        │
#        ▼
# [ Microprocessor (CPU) ] ──► Executes the program

# variable is a name given to the memory location in order to store data in a RAM (Random Access Memory) of a computer. It is a symbolic name that represents a memory location where data can be stored and retrieved during program execution.
from h11 import Data


a =10
print(a)
b="sachi"
print(f"My name is {b}")

x = str(3)
y = int(3)
z = float(3)

print(x, y, z,type(x), type(y), type(z))

p,q,r = 10, 20, 30
print(p,q,r)

# single line comment

""" this is a multi line or block comment """

# data types in python are:
# 1. Numeric Data Types: int, float, complex
# 2. Text Data Type: str
# 3. Boolean Data Type: bool
# 4. Sequence Data Types: list, tuple, range
# 5. Mapping Data Type: dict
# 6. Set Data Types: set, frozenset

