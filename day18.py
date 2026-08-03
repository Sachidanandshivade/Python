class Mentor:
    name = "Gamana"
    age = 23
    skill = "python"

    def teach(self):
        print("Mentor teaches")

    def groom(self):
        print("Mentor grooms")


# Creating an object of Mentor
m = Mentor()

# Accessing attributes
print(f"{m.name}, {m.age}, {m.skill}")

# Calling methods
m.teach()
m.groom()