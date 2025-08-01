name = input("Enter your name: ")
age = int(input("Enter your age: "))

if 10 <= age <= 20:
    print(f"✅ Welcome {name}, you are enrolled!")
else:
    print(f"❌ Sorry {name}, age not allowed.")
