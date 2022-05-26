from organism import Organism
from utils.direction import Direction


class Animal(Organism):
    def __init__(self, position, world):
        super().__init__(position, world)
        self.width_limit = world.columns - 1
        self.height_limit = world.rows - 1
        self.direction = Direction
        self.is_animal = True

    def action(self, *args, **kwargs):
        super().action()
        self.world.clear_position(self.position.x, self.position.y)
        self.direction = Direction.get_random_direction()
        if self.direction == Direction.UP.value:
            self.move_up()
        elif self.direction == Direction.DOWN.value:
            self.move_down()
        elif self.direction == Direction.RIGHT.value:
            self.move_right()
        elif self.direction == Direction.LEFT.value:
            self.move_left()

    def turn_back(self):
        if self.direction == Direction.UP.value:
            self.move_down()
        elif self.direction == Direction.DOWN.value:
            self.move_up()
        elif self.direction == Direction.RIGHT.value:
            self.move_left()
        elif self.direction == Direction.LEFT.value:
            self.move_right()

    def move_down(self):
        if self.position.x < self.height_limit:
            self.position.x += 1

    def move_right(self):
        if self.position.y < self.width_limit:
            self.position.y += 1

    def move_left(self):
        if self.position.y > 0:
            self.position.y -= 1

    def move_up(self):
        if self.position.x > 0:
            self.position.x -= 1

    def collision(self, *args, **kwargs):
        enemy = self.world.board[self.position.x][self.position.y]
        if enemy is not None:
            if type(self) is type(enemy):
                friend = enemy
                self.turn_back()
                self.world.board[self.position.x][self.position.y] = self
                self.reproduce(friend)
            else:
                if not enemy.is_animal:
                    enemy.extra_behavior(self)
                self.fight(enemy)
        else:
            # field is empty
            self.world.board[self.position.x][self.position.y] = self

