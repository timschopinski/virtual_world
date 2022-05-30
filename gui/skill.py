from organism import Organism
from utils.point import Point
from gui.animation import Animation
import pygame
import os


class Skill:
    explosions = []
    is_animating = False
    animations = [
        pygame.image.load(os.path.join("gui/assets/animations", "explosion_1.png")),
        pygame.image.load(os.path.join("gui/assets/animations", "explosion_2.png")),
        pygame.image.load(os.path.join("gui/assets/animations", "explosion_3.png")),
        pygame.image.load(os.path.join("gui/assets/animations", "explosion_4.png")),
        pygame.image.load(os.path.join("gui/assets/animations", "explosion_5.png")),
        pygame.image.load(os.path.join("gui/assets/animations", "explosion_6.png")),
    ]

    def __init__(self, owner: 'Organism', duration: int = 5, cooldown: int = 5):
        self.owner = owner
        self.duration = duration
        self.cooldown = cooldown
        self.is_active = False
        self.animation_time = 4
        self.animation_time_counter = 0
        self.animation_index = 0

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
                self.animate_explosion(enemy_position)
        if x < self.owner.world.rows - 1:
            enemy_position.update(x + 1, y)
            if not self.owner.world.is_field_empty(enemy_position):
                self.owner.world.remove_organism_on_field(enemy_position)
                self.animate_explosion(enemy_position)
        if y > 0:
            enemy_position.update(x, y - 1)
            if not self.owner.world.is_field_empty(enemy_position):
                self.owner.world.remove_organism_on_field(enemy_position)
                self.animate_explosion(enemy_position)
        if y < self.owner.world.columns - 1:
            enemy_position.update(x, y + 1)
            if not self.owner.world.is_field_empty(enemy_position):
                self.owner.world.remove_organism_on_field(enemy_position)
                self.animate_explosion(enemy_position)

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

    def animation_cooldown(self):
        if self.animation_time_counter >= self.animation_time:
            self.animation_time_counter = 0
            self.animation_index += 1
        elif self.animation_time_counter > 0:
            self.animation_time_counter += 1

    def animate_explosion(self, position: Point):
        y = position.y * self.owner.world.field_width
        x = position.x * self.owner.world.field_height
        for animation in self.animations:
            explosion = Animation(animation, Point(y - 340, x))
            self.explosions.append(explosion)
            self.is_animating = True

    def draw_explosion(self):
        self.animation_cooldown()
        if self.animation_time_counter == 0:
            explosion = self.explosions[self.animation_index]
            self.owner.world.window.blit(explosion.img, (explosion.position.x, explosion.position.y))
            self.animation_time_counter = 1
        if self.animation_index >= len(self.explosions) - 1:
            self.animation_index = 0
            self.explosions.clear()
            self.is_animating = False

    def __str__(self):
        return 'Burning'



