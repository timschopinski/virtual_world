from animals.sheep import Sheep
from typing import List
from utils.direction import Direction
import plants
import pygame
import os


class CyberSheep(Sheep):

    def __init__(self, position, world):
        super().__init__(position, world)
        self.strength = 4
        self.initiative = 4
        self.AVATAR_WIDTH = self.world.field_width * 0.8
        self.AVATAR_HEIGHT = self.world.field_height * 0.4
        self.AVATAR = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/animals/", "cyber_sheep.png")),
                                             (self.AVATAR_WIDTH, self.AVATAR_HEIGHT))

    def get_all_borsch(self) -> List:
        """ Returns a list of Borsch objects in the world """
        return [borsch for borsch in self.world.organisms if isinstance(borsch, plants.borsch.Borsch)]

    def get_nearest_borsch(self):
        """ Returns the nearest Borsch """
        return min(self.get_all_borsch(), key=lambda borsch: self.position.get_distance_between_points(borsch.position), default=None)

    def action(self):
        self.age += 1
        if not self.get_all_borsch():
            print('super called')
            self.direction = Direction.get_random_direction()
        else:
            print('extra behavior called')
            self.extra_action_behavior()

        self.world.clear_position(self.position.x, self.position.y)
        self.move()

    def extra_action_behavior(self):

        nearest_borsch = self.get_nearest_borsch()
        if self.position.x > nearest_borsch.position.x:
            self.direction = Direction.UP
        elif self.position.x < nearest_borsch.position.x:
            self.direction = Direction.DOWN
        elif self.position.y > nearest_borsch.position.y:
            self.direction = Direction.LEFT
        elif self.position.y < nearest_borsch.position.y:
            self.direction = Direction.RIGHT

    @staticmethod
    def get_description():
        return """ Its primary goal is to eat Borsch. Always drives towards the nearest borscht and tries to eat it. If there is no borscht it pretends to be ordinary sheep"""

    def __str__(self):
        return 'Cyber_Sheep'
