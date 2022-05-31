from organism import Organism
from utils.point import Point
from gui.animation import Animation
from typing import List
import pygame
import os


class Skill:

    animations = [
        pygame.image.load(os.path.join("gui/assets/animations/explosion", "explosion_1.png")),
        pygame.image.load(os.path.join("gui/assets/animations/explosion", "explosion_2.png")),
        pygame.image.load(os.path.join("gui/assets/animations/explosion", "explosion_3.png")),
        pygame.image.load(os.path.join("gui/assets/animations/explosion", "explosion_4.png")),
        pygame.image.load(os.path.join("gui/assets/animations/explosion", "explosion_5.png")),
        pygame.image.load(os.path.join("gui/assets/animations/explosion", "explosion_6.png")),
    ]

    def __init__(self, owner: Organism, duration: int = 5, cooldown: int = 5):
        self.owner = owner
        self.duration = duration
        self.cooldown = cooldown
        self.is_active = False
        self.is_animating = False
        self.explosions: List[Animation] = []

    def activate(self):
        """ Activates the skill"""
        if self.cooldown == 5:
            self.is_active = True
            self.owner.world.info.add_comment(f"{self.owner} power '{self}' has been activated")
        else:
            self.owner.world.info.add_comment(f"{self.owner} power '{self}' can be activated again in {5 - self.cooldown} rounds")

    def action(self):
        """ Kills all neighbours """
        x = self.owner.position.x
        y = self.owner.position.y
        enemy_position = Point(x - 1, y)
        if x > 0:
            if not self.owner.world.is_field_empty(enemy_position):
                self.owner.world.remove_organism_on_field(enemy_position)
                self.create_animation(enemy_position)
        if x < self.owner.world.rows - 1:
            enemy_position.update(x + 1, y)
            if not self.owner.world.is_field_empty(enemy_position):
                self.owner.world.remove_organism_on_field(enemy_position)
                self.create_animation(enemy_position)
        if y > 0:
            enemy_position.update(x, y - 1)
            if not self.owner.world.is_field_empty(enemy_position):
                self.owner.world.remove_organism_on_field(enemy_position)
                self.create_animation(enemy_position)
        if y < self.owner.world.columns - 1:
            enemy_position.update(x, y + 1)
            if not self.owner.world.is_field_empty(enemy_position):
                self.owner.world.remove_organism_on_field(enemy_position)
                self.create_animation(enemy_position)

    def update(self):
        """ Updates duration, is_active and cooldown status"""
        if self.duration == 0:
            self.is_active = False
        if self.is_active:
            self.cooldown -= 1
            self.duration -= 1
        else:
            if self.cooldown < 5:
                self.cooldown += 1
            self.duration = 5

    def create_animation(self, position: Point):
        y = position.y * self.owner.world.field_width
        x = position.x * self.owner.world.field_height
        self.explosions.append(Animation(self.animations.copy(), Point(y - 340, x)))
        self.is_animating = True

    def draw_explosion(self):
        for explosion in self.explosions:
            explosion.draw(self.owner.world.window)
        if all([explosion.is_end_of_animation for explosion in self.explosions]):
            self.explosions.clear()
            self.is_animating = False

    def __str__(self):
        return 'Burning'



