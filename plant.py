from organism import Organism
from random import randint
from utils.point import Point


class Plant(Organism):
    def __init__(self, position, world):
        super().__init__(position, world)
        self.initiative = 0
        self.strength = 0
        self.is_animal = False
        self.chance_to_spread = 50  # %

    def collision(self):
        super().collision()

    def extra_collision_behavior(self, enemy):
        self.die(enemy)

    def try_to_spread(self):
        if randint(1, 100) < self.chance_to_spread:
            if any(type(neighbour) == type(self) for neighbour in self.get_all_neighbours()):
                empty_field = self.get_empty_field(self.position)
                if empty_field is not None:
                    new_organism = self.__class__(empty_field, self.world)
                    self.world.info.add_comment(
                        f'A new {new_organism}[{new_organism.position.x}][{new_organism.position.y}] has grown')

    def action(self):
        super().action()
        self.try_to_spread()
