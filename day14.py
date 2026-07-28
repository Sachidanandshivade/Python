fruit_list = ["apple", "banana", "cherry", "date", "elderberry"];
print(fruit_list);
print(fruit_list[1]);

fruit_list[2] = "coconut";
print(fruit_list);

fruit_list.append("fig");
print(fruit_list);

fruit_list.remove("apple");
print(fruit_list);

fruit_list.pop(0);
del fruit_list[1];
print(fruit_list);

del fruit_list; #delete complete list no thing called fruit_list

numbers = [10, 20, 30]
print(len(numbers))
print(max(numbers), min(numbers))
print(sum(numbers))

# Sorting lists
numbers = [5, 2, 0, 1]
numbers.sort()
print(numbers)

# Reverse sorting
numbers.sort(reverse=True)
# numbers.reverse()
print(numbers)

# membership operator
numbers = [5, 2, 8, 1, 3]
print(5 in numbers)
print(10 not in numbers)

colors = ["red", "yellow", "Green", "red"]
for c in colors:
    print(c, end=" ")

colors = ["red", "yellow", "Green", "red"]
favcolors = colors.copy()
print(favcolors)
print(colors)

colors = ["red", "yellow", "Green", "red"]
print(colors.index("yellow"))
print(colors.count("red"))

words = input().split()
print(words)
print(words[1])

#Nested Lists
#index        0             1               2
#sub index    0    1        0    1          0    1
students = [["Abhi", 23], ["Bhavya", 34], ["Chitra", 25]]
print(students[0])
print(students[1][0])
print(students[2][1])

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])       # [20, 30, 40]
print(numbers[-4:-1])     # [30, 40, 50]
print(numbers[::-1])      # [60, 50, 40, 30, 20, 10]
print(numbers[::-2])      # [60, 40, 20]
print(numbers[::2])       # [10, 30, 50]