from plant import Plant
from animal import Animal
import pygame
import os


class Guarani(Plant):

    def __init__(self, position, world):
        super().__init__(position, world)
        self.strength = 0
        self.boost = 3
        self.AVATAR_WIDTH = self.world.field_width * 0.7
        self.AVATAR_HEIGHT = self.world.field_height * 0.5
        self.AVATAR = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/", "guarani.png")),
                                             (self.AVATAR_WIDTH, self.AVATAR_HEIGHT))

    def extra_behavior(self, enemy: 'Animal'):
        """Adds extra 3 points of strength"""
        enemy.strength += self.boost

    def __str__(self):
        return 'Guarani'
