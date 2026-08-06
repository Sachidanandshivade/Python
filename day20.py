class Student:
    # class attribute - used when every object has/share same value
    institute = "Kodnest"
    def __init__(self,name,age):
        #instance attributes - use when each object has own values 
        self.name = name
        self.age = age
        

    def study(self):
        print(f"{self.name} is studying at {self.institute}.")  

    @staticmethod
    def trip(student):
        print(f"{student.name} likes to go on a trip")
    
    
s1 = Student("Alice", 20) 
s1.study()


   
stu1 = Student(name="Akhil", age=20)
print(f"{stu1.name} is {stu1.age} years old and studies at {Student.institute}")
stu1.study()

stu2 = Student("Abhi", 23)
print(f"{stu2.name} is {stu2.age} years old and studies at {Student.institute}")
stu2.study()

Student.trip(stu1)