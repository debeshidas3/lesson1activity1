num = int(input("Enter an ASCII value (0–127): "))
if 0 <= num <= 127:
    print(f"The character for ASCII {num} is: '{chr(num)}'")
else:
    print("Please enter a value between 0 and 127.")
