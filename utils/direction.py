from enum import Enum
import random


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    @staticmethod
    def get_random_direction():
        return random.choice(list(Direction))
