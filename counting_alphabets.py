ch = input("Enter any character: ")

# Check if it's a single character
if len(ch) == 1:
    # Use comparison operators to check if it's an alphabet
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        print("It is an alphabet.")
    else:
        print("It is not an alphabet.")
else:
    print("Please enter only one character.")