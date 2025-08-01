medical=input("do you have a medical conditon Y or N")
attendance=int(input("enter the attendance"))
if medical=='Y':
   print("you are allowed")
else:
    if attendance >=75: 
       print("allowed")
    else:
        print("not allowed")       