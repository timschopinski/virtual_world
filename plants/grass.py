from plant import Plant
import pygame
import os


class Grass(Plant):

    def __init__(self, position, world):
        super().__init__(position, world)
        self.AVATAR_WIDTH = self.world.field_width * 0.5
        self.AVATAR_HEIGHT = self.world.field_height * 0.5
        self.AVATAR = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/plants/", "grass.png")),
                                             (self.AVATAR_WIDTH, self.AVATAR_HEIGHT))

    def __str__(self):
        return 'Grass'
