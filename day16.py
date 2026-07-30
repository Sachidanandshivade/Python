# set - unordered, homo/hetero, does not allow duplicates, no indexing, mutable
set1 = {"apple", "banana", "Grapes", "apple"}
print(set1, type(set1))

# set1[2] = "apple"
set1.add("pineapple")
set1.remove("apple")
set1.discard("apple")
set1.pop() # random
print(set1, len(set1))

# print(set1[1])

set2 = {"Gamana", 23, True, 4.6, 6 + 5j, 1} # True , 1
print(set2, type(set2))


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# a.update(b)
# print(a)

seta = a.union(b) # a | b
print(seta)

setb = a.intersection(b) # a & b
print(setb) #{3, 4}

setc = a.difference(b) # a - b
print(setc) #{1, 2}
print(a)

# a.difference_update(b) # changes in original set
# print(a)

setd = a.symmetric_difference(b) # a ^ b
print(setd) #{1, 2, 5, 6}

letters = set("python")
print(letters)

student = {
    "name": "Sachi",
    "age": 23,
    "City": "Benagluru"
}

print(student["name"])
student["phone"] = "9353947020"
print(student)

#Nested Dict
students = {
    "student1" : {
        "name": "Rahul",
        "age": 34,
        "city": "Bangalore"
    },
    "student2" : {
        "name": "Rahul",
        "age": 34,
        "city": "Bangalore"
    }
}
print(students)