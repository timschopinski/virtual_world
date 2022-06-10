

class Point:
    def __init__(self, coordinates: tuple):
        self.x, self.y = coordinates

    def get_tuple(self) -> tuple:
        """ Returns Point coordinates as a tuple"""
        return self.x, self.y

    def update(self, x, y):
        """ Updates x and y Point coordinates(sets new values)"""
        self.x = x
        self.y = y

    def get_distance_between_points(self, other: 'Point') -> int:
        """ Returns rectilinear distance between two points """
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


if __name__ == '__main__':
    p = Point(1, 2)
    print(p)
    p = Point((1, 2))
    print(p)

