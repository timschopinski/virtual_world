from animal import Animal
import pygame
import os


class Wolf(Animal):

    def __init__(self, position, world):
        super().__init__(position, world)
        self.strength = 9
        self.initiative = 5
        self.WOLF_SIZE_WIDTH = self.world.field_width
        self.WOLF_SIZE_HEIGHT = self.world.field_height * 0.75
        self.AVATAR = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/", "wolf.png")),
                                             (self.WOLF_SIZE_WIDTH, self.WOLF_SIZE_HEIGHT))

    def __str__(self):
        return 'Wolf'

    def draw(self):
        organism_position = (self.position.y * self.world.field_width + 5, self.position.x * self.world.field_height + self.world.field_height/2 - 10)
        self.world.window.blit(self.AVATAR, organism_position)

