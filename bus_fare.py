class child:
      def __init__(self,name,age,grade):
          self.name = name
          self.age = age
          self.grade = grade           
class Vehicle:
      def __init__(self,name,max_speed,mileage):
          self.name = name
          self.max_speed = max_speed
          self.mileage = mileage
class Bus(Vehicle):
    pass          

school_bus = Bus("School volvo",180,12)
print("vehicle name:",school_bus.name,"speed:",school_bus.max_speed,"mileage:",school_bus.mileage)

people = 50
fare_per_person = 100

total_fare = people * fare_per_person
final_fare = total_fare

print("Total fare:", total_fare)
print("Final fare:", final_fare)
