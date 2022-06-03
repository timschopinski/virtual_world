from plant import Plant
import pygame
import os


class Dandelion(Plant):

    def __init__(self, position, world):
        super().__init__(position, world)
        self.chance_to_spread = 5  # %
        self.AVATAR_WIDTH = self.world.field_width * 0.7
        self.AVATAR_HEIGHT = self.world.field_height * 0.5
        self.AVATAR = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/plants/", "borsch.png")),
                                             (self.AVATAR_WIDTH, self.AVATAR_HEIGHT))

    def action(self):
        super().action()
        [self.try_to_spread() for _ in range(3)]

    @staticmethod
    def get_description():
        return """Tries to spread three times per round."""

    def __str__(self):
        return 'Borsch'
