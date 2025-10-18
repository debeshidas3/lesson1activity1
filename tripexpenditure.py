hotel=float(input("enter hotel cost per day:"))
days=int(input("enter number of days stayed:"))
flight=float(input("enter flight ticket cost:"))
vehicle=float(input("enter total vehicle rent:"))
hotelcost=hotel*days
totaltrip=hotelcost+flight+vehicle
print("total trip expenditure=",totaltrip)