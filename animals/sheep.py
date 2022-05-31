from animal import Animal
import pygame
import os


class Sheep(Animal):

    def __init__(self, position, world):
        super().__init__(position, world)
        self.strength = 4
        self.initiative = 4
        self.AVATAR_WIDTH = self.world.field_width * 0.8
        self.AVATAR_HEIGHT = self.world.field_height * 0.4
        self.AVATAR = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/animals/", "sheep.png")),
                                             (self.AVATAR_WIDTH, self.AVATAR_HEIGHT))

    def __str__(self):
        return 'Sheep'
