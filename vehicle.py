class Vehicle:
    def __init__(self,maxspeed,fuel_type):
        self.maxspeed = maxspeed
        self.fuel_type = fuel_type

def show_info(self):
# Default behavior (can be used by all subclasses)
        print(f"Max Speed: {self.maxspeed} km/h")
        print(f"Fuel Type: {self.fuel_type}")

class BMW(vehicle):  
    pass  
        print("The maxspeed of BMW is {maxspeed} km/h")
        print("The fuel_type of BMW is {fuel_type}")

class Ferrari(vehicle):
    pass
        print("The maxspeed of ferrari is {maxspeed}km/h")
        print("The fuel_type of ferrari is {fuel_type}")        

# create objects
car1 = BMW(240, "Petrol")
car2 = Ferrari(350, "Petrol")

# polymorphic behavior: same method name, different output
for car in (car1, car2):
    car.show_info()        