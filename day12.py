# Selection Statements

# if
age = 10
if age >= 18:
    print("Eligible to vote")

print("Thank you")


# if-else
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

print("Thank you")

# elif ladder example
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("fail")


# Nested if example
age = 20
has_voter_id = True

if age >= 18:
    print("You are an adult.")
    
    # Outer condition passed, now check inner condition
    if has_voter_id:
        print("Eligible to vote.")
    else:
        print("Please apply for a voter ID to vote.")
else:
    print("Not eligible to vote (Underage).")


# match
day = 4
match day:
    case 1: print("Mon")
    case 2: print("Tue")
    case 3: print("Wed")
    case 4: print("Thu")
    case 5: print("Fri")
    case _: print("Invalid day")

# match month example
month = 1

match month:
    case 3 | 4 | 5:
        print("Summer")
    case 6 | 7 | 8:
        print("Rainy")
    case 9 | 10 | 11 | 12:
        print("Winter")
    case 1 | 2:
        print("Autumn")
    case _:
        print("Invalid month")










# looping
# for 0 to 5 (012345) (1, 6)
for i in range(1, 6):
    print(i)

# first 5 numbers
for i in range(5):
    print(i)

# even numbers( 2 4 6 8 10)
for num in range(1, 11):
    if num % 2 == 0:
        print(num)

# while
i = 0
while i <= 4:
    print(i)
    i += 1


