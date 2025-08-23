num=input("enter a number")
length=len(num)
if length<3:
   print("no middle digits")
else:
    if length%2==0:
       d1=int(num[length//2-1])
       d2=int(num[length//2])
       product=d1*d2
       print("middle digits are",d1,"and",d2) 
    else:
        d=int(num[length//2])
        product=d
        print("middle digit is",d)
    print("product",product)           