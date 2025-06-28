height=int(input("enter the height"))
weight=int(input("enter the weight"))
bmi=weight/(height/100)**2
print("your bmi is", bmi)
if bmi<=25:
   print("you are healthy")
else:
    print("you are obese")    
