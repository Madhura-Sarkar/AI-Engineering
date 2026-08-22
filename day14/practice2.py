class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
        
developer1 = Developer("Madhura", "30000", "Python")

print(developer1.name)
print(developer1.salary)
print(developer1.programming_language)
