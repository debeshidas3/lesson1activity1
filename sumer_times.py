# Ask the user to input the temperature
temperature = int(input("Enter the current temperature in Celsius: "))

# Decision using conditional statements
if temperature >= 25:
    print("It's warm. Rohan can wear light and soft clothes.")
elif temperature >= 15 and temperature < 25:
    print("It's a bit cool. Rohan should wear a light jacket.")
else:
    print("It's cold. Rohan should wear a pullover or warm clothes.")