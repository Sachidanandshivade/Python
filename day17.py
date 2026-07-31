# function to find square of a number
numbers = [1, 2, 3, 4, 5]
doubled = []
for num in numbers:
    doubled.append(num * num)
print(doubled)

# List Comprehension - listname = [expression for i in iterablelist]
doubled = [num * num for num in numbers]
print(doubled)

numbers = [1, 2, 3, 4, 5, 6]
res = [x if x % 2 == 0 else "Odd" for x in numbers]
print(res)

even = [n for n in numbers if n % 2 == 0]
print(even)

words = ["Apple","Mango","Pineapple"]
up = [(x.upper(),len(x)) for x in words ]
print(up)

mul = [5*x for x in range(1,11)]
print(mul)

items = ["Apple","","Mango","","Pineapple"]
fru = [x  for x in items if x != ""]
print(fru)