<<<<<<< Updated upstream
# Prompt the user for a single character
ch = input("Enter a single character: ")

# Verify input length
if len(ch) != 1:
    print("❗ Please enter exactly one character.")
else:
    ascii_val = ord(ch)
=======
# Prompt the user for a single character
ch = input("Enter a single character: ")

# Verify input length
if len(ch) != 1:
    print("❗ Please enter exactly one character.")
else:
    ascii_val = ord(ch)
>>>>>>> Stashed changes
    print(f"The ASCII value of '{ch}' is: {ascii_val}")