from animal import Animal
import pygame
import os


class Fox(Animal):

    def __init__(self, position, world):
        super().__init__(position, world)
        self.strength = 3
        self.initiative = 7
        self.AVATAR_WIDTH = self.world.field_width * 0.6
        self.AVATAR_HEIGHT = self.world.field_height * 0.6
        self.AVATAR = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/animals/", "fox.png")),
                                             (self.AVATAR_WIDTH, self.AVATAR_HEIGHT))

    def action(self):
        self.age += 1
        self.world.clear_position(self.position.x, self.position.y)
        self.set_direction_to_position(self.get_empty_field(self.position))
        if self.direction is None:
            [self.set_direction_to_position(neighbour.position) for neighbour in self.get_all_neighbours() if neighbour.strength < self.strength or type(neighbour) is type(self)]
        self.move()

    def __str__(self):
        return 'Fox'

