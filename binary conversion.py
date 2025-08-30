n = int(input("Enter a decimal number"))
bits = []
for weight in [8, 4, 2, 1]:             
    if n >= weight:                  
        bits.append('1')
        n -= weight
    else:
        bits.append('0')
binary = ''.join(bits).lstrip('0') or '0'
print(f"Binary: {binary}")







