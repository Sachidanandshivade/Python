class Student:
    # class attribute - used when every object has/share same value
    institute = "Kodnest"
    def __init__(self,name,age):
        #instance attributes - use when each object has own values 
        self.name = name
        self.age = age
        

    def study(self):
        print(f"{self.name} is studying at {self.institute}.")  

s1 = Student("Alice", 20) 
s1.study()