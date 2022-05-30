from animal import Animal
import pygame
import os


class Sheep(Animal):

    def __init__(self, position, world):
        super().__init__(position, world)
        self.strength = 4
        self.initiative = 4
        self.SHEEP_SIZE_WIDTH = self.world.field_width * 0.8
        self.SHEEP_SIZE_HEIGHT = self.world.field_height * 0.4
        self.AVATAR = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/", "sheep.png")),
                                             (self.SHEEP_SIZE_WIDTH, self.SHEEP_SIZE_HEIGHT))

    def draw(self):
        organism_position = (self.position.y * self.world.field_width + 3, self.position.x * self.world.field_height + self.world.field_height/2 + 8)
        self.world.window.blit(self.AVATAR, organism_position)

    def __str__(self):
        return 'Sheep'
