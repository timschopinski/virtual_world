from animal import Animal
import pygame
from random import randrange
import os


class Turtle(Animal):

    def __init__(self, position, world):
        super().__init__(position, world)
        self.strength = 2
        self.initiative = 1
        self.has_special_collision = True
        self.chance_to_move = 25  # %
        self.AVATAR_WIDTH = self.world.field_width * 0.8
        self.AVATAR_HEIGHT = self.world.field_height * 0.4
        self.AVATAR = pygame.transform.scale(pygame.image.load(os.path.join("gui/assets/animals/", "turtle.png")),
                                             (self.AVATAR_WIDTH, self.AVATAR_HEIGHT))

    def action(self):
        if self.chance_to_move > randrange(100):
            super().action()
        else:
            self.world.clear_position(self.position.x, self.position.y)
            self.extra_action_behavior()
            self.age += 1

    def extra_collision_behavior(self, enemy: Animal):
        if not self.is_alive or not enemy.is_alive:
            return
        if enemy.strength < 5 and enemy.is_animal:
            enemy.turn_back()
            self.world.board[enemy.position.x][enemy.position.y] = enemy
        elif not enemy.is_animal:
            self.eat_enemy(enemy)
        else:
            self.die(enemy)

    def __str__(self):
        return 'Turtle'

