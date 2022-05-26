

class Point:
    def __init__(self, *args, **kwargs):
        if len(args) == 2:
            self.x, self.y = args
        elif len(args) == 1 and len(args[0]) == 2:
            self.x, self.y = args[0]
        else:
            raise Exception('To many arguments to unpack')


    def get_tuple(self) -> tuple:
        return self.x, self.y

    def update(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


if __name__ == '__main__':
    p = Point(1, 2)
    print(p)
    p = Point((1, 2))
    print(p)

