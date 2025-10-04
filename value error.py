try:
   number=int(input("please enter a number"))
   print("the number entered is",number)
except ValueError ex:
       print("exception",ex)