class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        
    def start(self):
        print("Vehicle is starting")
    
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        
    def drive(self):
        print(f"{self.brand} {self.model} Car is driving")

car1 = Car("Honda", "civic")

print(car1.brand)
print(car1.model)

car1.start()
car1.drive()