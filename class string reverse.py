<<<<<<< Updated upstream
class Reverse:
    def __init__(self, s=""):
        self.s = s
    def rev(self):
        return self.s[::-1]

r = Reverse(input("Enter word: "))
=======
class Reverse:
    def __init__(self, s=""):
        self.s = s
    def rev(self):
        return self.s[::-1]

r = Reverse(input("Enter word: "))
>>>>>>> Stashed changes
print(r.rev())