student = ("Sachi", 22, "Banglore")
print(student)
print(type(student))
print(student[0])

# student[1] = 23
# print(student)

#converting list to tuple
#using tuple constructor

data = [1,2,4,5]
t = tuple(data)
print(type(t))
print(t)

person = ("Sachi",23,"student")
name,age,role = person
print(name, type(name))
print(age, type(age))
print(role, type(role))


#sets
my_set = {1, 2, 3, 4}
print(my_set)

another_set = set([1, 2, 2, 3])
print(another_set)

s = {1, 2, 3}
s.add(4)
print(s)

s.remove(2)
s.discard(10)

print(3 in s)

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

