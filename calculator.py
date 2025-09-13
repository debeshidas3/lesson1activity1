def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
print("please select the operation")
print("a.add")
print("b.subtract")
print("c.multiply")
print("d.divide")
choice=input("please enter your choice(a/b/c/d)")
num1=int(input("please enter the first number"))
num2=int(input("pleasem enter the second number"))
if choice=='a':
   print(add(num1,num2))
elif choice=='b':
     print(subtract(num1,num2))
elif choice=='c':
    print(multiply(num1,num2))
elif choice=='d':
     print(divide(num1,num2))
else:
    print("invalid")                