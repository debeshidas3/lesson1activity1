class C:
    def __init__(self, v: int): self.v = v

    def next(self):
        r = self.v
        self.v -= 1
        return r