try:
    name = input("Please enter your name: ")
    print("The name entered is", name)

    age = int(input("Please enter your age: "))
    if age < 0 or age > 150:
        print("Error: Age out of range")
    else:
        print("The age entered is", age)
        print(f"{age} is", "EVEN" if age % 2 == 0 else "ODD")

except ValueError:
    print("Error: Please enter a valid number for age.")
