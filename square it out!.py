n=int(input("enter the start range:"))
a=int(input("enter the end range:"))

squares = [x*x for x in range(n, a+1)]
evens   = [s for s in squares if s % 2 == 0]
odds    = [s for s in squares if s % 2 != 0]

print("Squares:", squares)
print("Even squares:", evens)
print("Odd squares:", odds)

    
        
