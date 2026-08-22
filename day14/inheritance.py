class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    # pass
    
    def bark(self):
        print("Dog barks")
        

dog = Dog()
dog.speak()
dog.bark()

# method overriding 
animal = Animal()
dog = Dog()

animal.speak() # Animal makes a sound 
dog.speak() # Dog Barks 
# The Dog class overrode the parent's speak() method. 



# __init__() 
class Person:
    def __init__(self, name):
        self.name = name
    
class Student(Person):
    def study(self):
        print(f"{self.name} is studying")
        
student1 = Student("Madhura")

print(student1.name)
student1.study()

#super()
class People:
    def __init__(self, name):
        self.name = name

class Good(People):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course
        
people = Good("Madhura", "AI Engineering")

print(people.name)
print(people.course)