data = {'Codignal': 3, 'is': 2, 'best': 2, 'for': 2, 'coding':1}

n = int(input("Please enter the value: "))

if n in data.values():
    count = sum(1 for v in data.values() if v == n)
   #  freq = [x * x for x in range(n + count)]
    print(f"The frequency of {n} is {count}")
   #  print("Frequency list:", freq)
else:
    print(f"The value {n} is not in the dictionary values.")

 