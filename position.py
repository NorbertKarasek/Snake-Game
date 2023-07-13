class Position:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __eq__(self, other):
        return isinstance(other, Position) and self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x} {self.y})"
        __repr__ == __str__