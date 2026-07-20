# operators

# Arithmetic operators: +, -, *, /, %, **, //
# Assignment operators: =, +=, -=, *=, /=, %=, **=, //=
# Comparison operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not
# Identity operators: is, is not
# Bitwise operators: &, |, ^, ~, <<, >>
# Shift operators: <<, >>
# Membership operators: in, not in

# More Tricky Programs on Python Operators

print("1.", 5 + 2 * 3) #
print("2.", (5 + 2) * 3) #

print("3.", 10 / 4) #
print("4.", 10 // 4) #
print("5.", 10 % 4) #

print("6.", 2 ** 3 ** 2) #

print("7.", True + 5) #
print("8.", False * 10) #

print("9.", 10 and 0) #
print("10.", 10 and 5) #

print("11.", 0 or 5) #
print("12.", 0 or 5 or 10) #

print("13.", not 0) #
print("14.", not 10) #

print("15.", 5 > 3 > 1) #
print("16.", 5 > 3 < 4) #

print("17.", 5 == 5.0) #
print("18.", 5 is 5.0) #

print("19.", -5 % 3) #
print("20.", 5 % -3) #

x = 10
x += 5
print("21.", x) #

x *= 2
print("22.", x) #

print("23.", 4 + 3 * 2 ** 2) #
print("24.", (4 + 3) * 2 ** 2) #

print("25.", True == 1) #
print("26.", False == 0) #

print("27.", 3 <= True) #

print("28.", bool(0)) #
print("29.", bool(-1)) #

print("30.", not True == False) #