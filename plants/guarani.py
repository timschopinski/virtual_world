from plant import Plant
from animal import Animal
import pygame
import os


class Guarani(Plant):

    def __init__(self, position, world):
        super().__init__(position, world)
        self.strength = 0
        self.boost = 3
        self.GRASS_SIZE_WIDTH = self.world.field_width * 0.7
        self.GRASS_SIZE_HEIGHT = self.world.field_height * 0.5
        self.AVATAR = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/", "guarani.png")),
                                             (self.GRASS_SIZE_WIDTH, self.GRASS_SIZE_HEIGHT))

    def draw(self):
        organism_position = (self.position.y * self.world.field_width + 10, self.position.x * self.world.field_height
                             + self.world.field_height/2 - 2)
        self.world.window.blit(self.AVATAR, organism_position)

    def extra_behavior(self, enemy: 'Animal'):
        """Adds extra 3 points of strength"""
        enemy.strength += self.boost

    def __str__(self):
        return 'Guarani'
