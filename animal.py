from organism import Organism
from utils.direction import Direction
from utils.point import Point

class Animal(Organism):
    def __init__(self, position, world):
        super().__init__(position, world)
        self.width_limit = world.columns - 1
        self.height_limit = world.rows - 1
        self.direction = Direction
        self.is_animal = True
        self.chance_to_reproduce = 50  # %

    def action(self):
        super().action()
        self.world.clear_position(self.position.x, self.position.y)
        self.direction = Direction.get_random_direction()
        self.move()

    def set_direction_to_position(self, target: Point):
        """Sets the direction to reach the given target"""
        if target is None:
            self.direction = None
            return
        if target.x < self.position.x:
            self.direction = Direction.UP
        elif target.x > self.position.x:
            self.direction = Direction.DOWN
        elif target.y > self.position.y:
            self.direction = Direction.RIGHT
        elif target.y < self.position.y:
            self.direction = Direction.LEFT
        else:
            self.direction = None

    def move(self):
        """ Changes the position in depending on the direction """
        if self.direction == Direction.UP:
            self.move_up()
        elif self.direction == Direction.DOWN:
            self.move_down()
        elif self.direction == Direction.RIGHT:
            self.move_right()
        elif self.direction == Direction.LEFT:
            self.move_left()

    def turn_back(self):
        """ Moves one field back"""
        if self.direction == Direction.UP:
            self.move_down()
        elif self.direction == Direction.DOWN:
            self.move_up()
        elif self.direction == Direction.RIGHT:
            self.move_left()
        elif self.direction == Direction.LEFT:
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

    def extra_collision_behavior(self, enemy):
        pass

    def collision(self):
        enemy = self.world.board[self.position.x][self.position.y]
        if enemy is not None:
            if type(self) is type(enemy):
                friend = enemy
                self.turn_back()
                self.world.board[self.position.x][self.position.y] = self
                self.reproduce(friend)
            elif self.has_special_collision or enemy.has_special_collision:
                self.extra_collision_behavior(enemy)
                enemy.extra_collision_behavior(self)
            else:
                if self.is_alive and enemy.is_alive:
                    self.fight(enemy)
        else:
            # field is empty
            self.world.board[self.position.x][self.position.y] = self

