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
