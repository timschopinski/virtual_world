from animal import Animal
import pygame
import random
import os
from utils.direction import Direction


class Antelope(Animal):

    def __init__(self, position, world):
        super().__init__(position, world)
        self.strength = 4
        self.initiative = 4
        self.chance_to_run_away = 50  # %
        self.has_special_collision = True
        self.AVATAR_WIDTH = self.world.field_width * 0.8
        self.AVATAR_HEIGHT = self.world.field_height * 0.8
        self.AVATAR = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/animals/", "antelope.png")),
                                             (self.AVATAR_WIDTH, self.AVATAR_HEIGHT))

    def action(self):
        self.age += 1
        self.world.clear_position(self.position.x, self.position.y)
        self.direction = Direction.get_random_direction()
        self.move()
        # self.collision()
        # if self.is_alive:
        #     self.world.clear_position(self.position.x, self.position.y)
        #     self.direction = Direction.get_random_direction()
        #     self.move()

    def extra_collision_behavior(self, enemy: Animal):
        if not self.is_alive or not enemy.is_alive:
            return
        if enemy.is_animal and random.randint(1, 100) < self.chance_to_run_away:
            empty_field = self.get_empty_field(self.position)
            if empty_field:
                self.position = empty_field
                self.world.board[empty_field.x][empty_field.y] = self
                self.world.board[enemy.position.x][enemy.position.y] = enemy
                self.world.info.add_comment(f'{self}[{self.position.x}][{self.position.y}] runs away from {enemy}')
                return
        self.fight(enemy)

    @staticmethod
    def get_description():
        return """Movement range is 2 fields."""

    def __str__(self):
        return 'Antelope'

