from plant import Plant
from animals.cyber_sheep import CyberSheep
import pygame
import os


class Borsch(Plant):

    def __init__(self, position, world):
        super().__init__(position, world)
        self.strength = 0
        self.boost = 3
        self.has_special_collision = True
        self.chance_to_spread = 5  # %
        self.AVATAR_WIDTH = self.world.field_width * 0.7
        self.AVATAR_HEIGHT = self.world.field_height * 0.5
        self.AVATAR = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/plants/", "borsch.png")),
                                             (self.AVATAR_WIDTH, self.AVATAR_HEIGHT))

    def extra_action_behavior(self):
        """ Kills all neighbour organisms """
        [self.remove_organism(neighbour) for neighbour in self.get_all_neighbours()
         if neighbour and type(self) is not type(neighbour) and not isinstance(neighbour, CyberSheep)]

    def extra_collision_behavior(self, enemy):
        """ Removes the enemy after collision. This method is called when collision happens """
        if not self.is_alive or not enemy.is_alive:
            return
        if not isinstance(enemy, CyberSheep):
            self.remove_organism(enemy)
            self.world.info.add_comment(
                f'{enemy}[{enemy.position.x}][{enemy.position.y}] dies after eating {self}[{self.position.x}][{self.position.y}]')
        super().extra_collision_behavior(enemy)

    @staticmethod
    def get_description():
        return """Kills all animals in the neighborhood except Cyber Sheep."""

    def __str__(self):
        return 'Borsch'
