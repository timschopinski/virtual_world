from plant import Plant
import pygame
import os


class Grass(Plant):

    def __init__(self, position, world):
        super().__init__(position, world)
        self.strength = 0
        self.GRASS_SIZE_WIDTH = self.world.field_width * 0.7
        self.GRASS_SIZE_HEIGHT = self.world.field_height * 0.5
        self.AVATAR = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/", "grass.png")),
                                             (self.GRASS_SIZE_WIDTH, self.GRASS_SIZE_HEIGHT))

    def __str__(self):
        return 'Grass'

    def draw(self):
        organism_position = (self.position.y * self.world.field_width + 10, self.position.x * self.world.field_height
                             + self.world.field_height/2 - 2)
        self.world.window.blit(self.AVATAR, organism_position)

