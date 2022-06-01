class Square:
    def __init__(self, side, math):
        self.side = side
        self.math_util = math

    def area(self):
        return self.math_util.power(self.side, 2)

    def circumference(self):
        return self.math_util.add(2 * self.side, 2 * self.side)
