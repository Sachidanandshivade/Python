class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Role: {self.role}")

    def project(self):
        print("Project: Basic")


class Developer(Employee):
    def project(self):
        print("Project: Development")

    def work_hours(self):
        print("Work hours: 10")


class Tester(Employee):
    def project(self):
        print("Project: Testing")

    def work_hours(self):
        print("Work hours: 14")


# --- Developer Instance ---
d = Developer("Alex", 70000, "Developer")
d.info()         # Inherited method
d.project()      # Overridden method
d.work_hours()   # Specialized method

print("---")

# --- Tester Instance ---
t = Tester("Sam", 60000, "Tester")
t.info()         # Inherited method
t.project()      # Overridden method
t.work_hours()   # Specialized method


class Employee:
    def login(self):
        print("Employee logged in successfully.")

class Developer(Employee):
    pass

# --- Usage ---
dev = Developer()
dev.login()  # Inherited from Employee



class GrandParent:
    def __init__(self):
        self.land = "10 Acres"

class Parent(GrandParent):
    def __init__(self):
        super().__init__()
        self.house = "Villa"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.bike = "Sports Bike"

# --- Usage ---
c = Child()
print(f"Child has access to: Land ({c.land}), House ({c.house}), Bike ({c.bike})")



class Employee:
    def company_policy(self):
        print("Work hours: 9 AM to 5 PM")

class Developer(Employee):
    pass

class Tester(Employee):
    pass

class HR(Employee):
    pass

# --- Usage ---
d = Developer()
t = Tester()
h = HR()

d.company_policy()
t.company_policy()
h.company_policy()


class GrandParent:
    def legacy(self):
        print("Family Values")

class Father(GrandParent):
    pass

class Mother:
    def care(self):
        print("Motherly Care")

class Child(Father, Mother):  # Combines Multilevel (GrandParent -> Father -> Child) and Multiple (Father + Mother -> Child)
    pass

# --- Usage ---
c = Child()
c.legacy()  # From GrandParent via Father
c.care()    # From Mother