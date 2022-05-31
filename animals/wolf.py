from animal import Animal
import pygame
import os


class Wolf(Animal):

    def __init__(self, position, world):
        super().__init__(position, world)
        self.strength = 9
        self.initiative = 5
        self.AVATAR_WIDTH = self.world.field_width
        self.AVATAR_HEIGHT = self.world.field_height * 0.75
        self.AVATAR = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/", "wolf.png")),
                                             (self.AVATAR_WIDTH, self.AVATAR_HEIGHT))

    def __str__(self):
        return 'Wolf'
