class Student:
    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def introduce(self):
        print(f"Hi, I am {self.name}.")
        
student1 = Student("Madhura", 22, "Computer Science")
print(student1.name)
student1.introduce()

    