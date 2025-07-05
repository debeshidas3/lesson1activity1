print("Welcome to the Grading System!")

# Taking marks of 5 subjects

marks1 = int(input("Enter marks for Subject 1: "))

marks2 = int(input("Enter marks for Subject 2: "))

marks3 = int(input("Enter marks for Subject 3: "))

marks4 = int(input("Enter marks for Subject 4: "))

marks5 = int(input("Enter marks for Subject 5: "))

# Calculate average

average = (marks1 + marks2 + marks3 + marks4 + marks5) / 5

# Show average marks

print("Average Marks:", average)

# Grading System

if average >= 91 and average <= 100:

grade = "A1"

elif average >= 81 and average <= 90:

grade = "A2"

elif average >= 71 and average <= 80:

grade = "B1"

elif average >= 61 and average <= 70:

grade = "B2"

elif average >= 51 and average <= 60:

grade = "C1"

elif average >= 41 and average <= 50:

grade = "C2"

elif average >= 33 and average <= 40:

grade = "D"

elif average >= 21 and average <= 32:

grade = "E1"

else:

grade = "E2"

# Show grade

print("Your Grade is:", grade)

