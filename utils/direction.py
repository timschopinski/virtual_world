from enum import Enum
from random import randint


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    @classmethod
    def get_random_direction(cls):
        return randint(1, 4)
