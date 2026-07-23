rows = 5  # Number of rows for the pyramid

for i in range(rows):
    # 1. Print leading spaces for alignment
    print(" " * (rows - i - 1), end="")

    # 2. Print increasing characters starting from 'A'
    for j in range(i + 1):
        print(chr(ord("A") + j), end="")

    # 3. Print decreasing characters
    for j in range(i - 1, -1, -1):
        print(chr(ord("A") + j), end="")

    # Move to the next line
    print()

# TODO: Prompt the user to enter the number of rows and store it in rows
rows = 5

# TODO: Use nested loops to print the hollow diamond pattern

# Upper half of the diamond
for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end="")
    
    # Print stars and inner spaces
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower half of the diamond
for i in range(rows, 0, -1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end="")
    
    # Print stars and inner spaces
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()