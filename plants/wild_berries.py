from plant import Plant
from animal import Animal
import pygame
import os


class WildBerries(Plant):

    def __init__(self, position, world):
        super().__init__(position, world)
        self.has_special_collision = True
        self.AVATAR_WIDTH = self.world.field_width * 0.7
        self.AVATAR_HEIGHT = self.world.field_height * 0.5
        self.AVATAR = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/plants/", "guarani.png")),
                                             (self.AVATAR_WIDTH, self.AVATAR_HEIGHT))

    def extra_collision_behavior(self, enemy: 'Animal'):
        """"""
        if self.is_alive:
            self.die(enemy)
        if enemy.is_alive:
            self.remove_organism(enemy)

    def __str__(self):
        return 'Wild Berries'
