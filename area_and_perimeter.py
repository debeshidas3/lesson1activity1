<<<<<<< Updated upstream
<<<<<<< Updated upstream
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def perimeter(self):
        return 2 * 3.14 * self.r

r = float(input("Enter radius: "))
c = Circle(r)

print("Area =", c.area())
=======
=======
>>>>>>> Stashed changes
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def perimeter(self):
        return 2 * 3.14 * self.r

r = float(input("Enter radius: "))
c = Circle(r)

print("Area =", c.area())
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
print("Perimeter =", c.perimeter())